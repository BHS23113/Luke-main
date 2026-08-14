from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv(override=True)

DATABASE = "prefectconnect.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user, client_id=GOOGLE_CLIENT_ID)


# DASHBOARD ROUTE
@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("index"))

    return render_template(
        "dashboard.html",
        user=session["user"]
    )

@app.route("/locker-duty")
def locker_duty():

    if "user" not in session:
        return redirect(url_for("index"))

    return render_template("locker_duty.html", user=session["user"])

@app.route("/login", methods=["POST"])
def login():

    token = request.json.get("credential")

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            grequests.Request(),
            GOOGLE_CLIENT_ID
        )

        google_id = idinfo["sub"]
        email = idinfo["email"]
        name = idinfo.get("name")

        db = get_db()
        cursor = db.cursor()

        # Check if user exists
        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cursor.fetchone()

        # If the email isn't in the database, deny access
        if user is None:
            db.close()

            return jsonify({
                "status": "error",
                "redirect": "/403"
            }), 403

        # Store DB user in session
        session["user"] = {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"],
            "role": user["role"]
        }

        db.close()

        # UPDATED RESPONSE
        return jsonify({
            "status": "success",
            "redirect": "/dashboard"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 401
    
@app.route("/users")
def users():

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        ORDER BY name
    """)

    users = cursor.fetchall()

    db.close()

    return render_template(
        "users.html",
        user=session["user"],
        users=users
    )

@app.route("/delete-user/<int:user_id>", methods=["POST"])
def delete_user(user_id):

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    # Prevent an admin from deleting themselves
    if user_id == session["user"]["user_id"]:
        return redirect(url_for("users"))

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM users WHERE user_id = ?",
        (user_id,)
    )

    db.commit()
    db.close()

    return redirect(url_for("users"))

@app.route("/add-user", methods=["POST"])
def add_user():

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    name = request.form["name"]
    email = request.form["email"]
    role = request.form["role"]

    db = get_db()
    cursor = db.cursor()

    # Check if the email already exists
    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        db.close()
        return redirect(url_for("users"))

    # Add the new user
    cursor.execute(
        """
        INSERT INTO users (name, email, role)
        VALUES (?, ?, ?)
        """,
        (name, email, role)
    )

    db.commit()
    db.close()

    return redirect(url_for("users"))

@app.route("/edit-role/<int:user_id>", methods=["POST"])
def edit_role(user_id):

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    role = request.form["role"]

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE users
        SET role = ?
        WHERE user_id = ?
        """,
        (role, user_id)
    )

    db.commit()
    db.close()

    return redirect(url_for("users")) 
    
@app.route("/403")
def forbidden():

    return render_template("403.html"), 403


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

    