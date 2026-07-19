from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
import sqlite3
import os
from dotenv import load_dotenv
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
    return render_template("index.html", user=user)


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

        # Create user if first login
        if user is None:
            cursor.execute("""
                INSERT INTO users (email, name, role)
                VALUES (?, ?, ?)
            """, (email, name, "prefect"))

            db.commit()

            cursor.execute(
                "SELECT * FROM users WHERE email=?",
                (email,)
            )
            user = cursor.fetchone()

        # Store DB user in session
        session["user"] = {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"]
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


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)