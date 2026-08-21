from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from dotenv import load_dotenv
import sqlite3
import os

from gmail import create_flow
from gmail import send_email

from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler


# ==============================
# SCHOOL WEEK CONFIGURATION
# ==============================

# The Monday that begins a known Week A.
# This is used to automatically determine whether a date is Week A or Week B.
WEEK_A_START = datetime(2026, 8, 10)


# ==============================
# APPLICATION CONFIGURATION
# ==============================

load_dotenv(override=True)

DATABASE = "prefectconnect.db"


# Connects to the SQLite database and allows rows to be accessed by column name.
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Determines whether a given date falls within Week A or Week B.
def get_school_week(date):

    # Find the Monday of the week containing this date.
    monday = date - timedelta(days=date.weekday())

    # Calculate how many weeks have passed since the starting Week A.
    weeks_since_start = (
        monday.date() - WEEK_A_START.date()
    ).days // 7

    # Even weeks are Week A and odd weeks are Week B.
    if weeks_since_start % 2 == 0:
        return "A"

    return "B"


app = Flask(__name__)

# Secret key is used by Flask to securely manage sessions.
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


# ==============================
# HOME PAGE
# ==============================

@app.route("/")
def index():

    user = session.get("user")

    return render_template(
        "index.html",
        user=user,
        client_id=GOOGLE_CLIENT_ID
    )


# ==============================
# DASHBOARD
# ==============================

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()

    user_id = session["user"]["user_id"]


    # ==============================
    # COUNT UNREAD NOTICES
    # ==============================

    # Count active notices that the current user has not read yet.
    cursor.execute("""
        SELECT COUNT(*)
        FROM notice
        WHERE notice.is_active = 1
        AND notice.notice_id NOT IN (
            SELECT notice_id
            FROM notice_read
            WHERE user_id = ?
        )
    """, (user_id,))

    notice_count = cursor.fetchone()[0]


    # ==============================
    # FIND NEXT LOCKER DUTY
    # ==============================

    today = datetime.now()

    next_duty = None

    # Check the next 14 days to find the user's next assigned duty.
    for days_ahead in range(0, 14):

        check_date = today + timedelta(days=days_ahead)

        # Skip Saturday and Sunday.
        if check_date.weekday() >= 5:
            continue

        check_day = check_date.strftime("%A")
        check_week = get_school_week(check_date)

        cursor.execute("""
            SELECT
                locker_duty.day,
                locker_duty.week
            FROM locker_duty
            WHERE locker_duty.user_id = ?
            AND locker_duty.day = ?
            AND locker_duty.week = ?
        """, (
            user_id,
            check_day,
            check_week
        ))

        duty = cursor.fetchone()

        # Stop searching once the next duty is found.
        if duty:
            next_duty = {
                "day": duty["day"],
                "week": duty["week"],
                "date": check_date.strftime("%d %B %Y")
            }

            break

    db.close()

    return render_template(
        "dashboard.html",
        user=session["user"],
        notice_count=notice_count,
        next_duty=next_duty
    )


# ==============================
# LOCKER DUTY
# ==============================

@app.route("/locker-duty")
def locker_duty():

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()

    # Retrieve all locker duty assignments.
    cursor.execute("""
        SELECT
            locker_duty.duty_id,
            locker_duty.user_id,
            locker_duty.week,
            locker_duty.day,
            users.name
        FROM locker_duty
        JOIN users
            ON locker_duty.user_id = users.user_id
        ORDER BY
            locker_duty.week,
            CASE locker_duty.day
                WHEN 'Monday' THEN 1
                WHEN 'Tuesday' THEN 2
                WHEN 'Wednesday' THEN 3
                WHEN 'Thursday' THEN 4
                WHEN 'Friday' THEN 5
            END
    """)

    duties = cursor.fetchall()

    # Retrieve active users for the Add Person dropdown.
    cursor.execute("""
        SELECT user_id, name
        FROM users
        WHERE is_active = 1
        ORDER BY name
    """)

    users = cursor.fetchall()

    db.close()

    return render_template(
        "locker_duty.html",
        user=session["user"],
        duties=duties,
        users=users
    )


# ==============================
# ADD LOCKER DUTY
# ==============================

@app.route("/add-locker-duty", methods=["POST"])
def add_locker_duty():

    if "user" not in session:
        return redirect(url_for("index"))

    # Only administrators can modify the locker duty roster.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    user_id = request.form["user_id"]
    week = request.form["week"]
    day = request.form["day"]

    db = get_db()
    cursor = db.cursor()


    # Check whether this person is already assigned to the selected day.
    cursor.execute("""
        SELECT users.name
        FROM locker_duty
        JOIN users
            ON locker_duty.user_id = users.user_id
        WHERE locker_duty.user_id = ?
        AND locker_duty.week = ?
        AND locker_duty.day = ?
    """, (user_id, week, day))

    existing_duty = cursor.fetchone()

    if existing_duty:

        error = f"{existing_duty['name']} is already assigned to {day}, Week {week}."

        # Reload the current roster so it can be displayed with the error.
        cursor.execute("""
            SELECT
                locker_duty.duty_id,
                locker_duty.user_id,
                locker_duty.week,
                locker_duty.day,
                users.name
            FROM locker_duty
            JOIN users
                ON locker_duty.user_id = users.user_id
            ORDER BY
                locker_duty.week,
                CASE locker_duty.day
                    WHEN 'Monday' THEN 1
                    WHEN 'Tuesday' THEN 2
                    WHEN 'Wednesday' THEN 3
                    WHEN 'Thursday' THEN 4
                    WHEN 'Friday' THEN 5
                END
        """)

        duties = cursor.fetchall()

        cursor.execute("""
            SELECT user_id, name
            FROM users
            WHERE is_active = 1
            ORDER BY name
        """)

        users = cursor.fetchall()

        db.close()

        return render_template(
            "locker_duty.html",
            user=session["user"],
            duties=duties,
            users=users,
            error=error
        )


    # Check whether the selected day already has two people assigned.
    cursor.execute("""
        SELECT COUNT(*)
        FROM locker_duty
        WHERE week = ? AND day = ?
    """, (week, day))

    count = cursor.fetchone()[0]

    if count >= 2:

        error = f"{day}, Week {week} already has two people assigned."

        # Reload the roster so the error can be displayed on the page.
        cursor.execute("""
            SELECT
                locker_duty.duty_id,
                locker_duty.user_id,
                locker_duty.week,
                locker_duty.day,
                users.name
            FROM locker_duty
            JOIN users
                ON locker_duty.user_id = users.user_id
            ORDER BY
                locker_duty.week,
                CASE locker_duty.day
                    WHEN 'Monday' THEN 1
                    WHEN 'Tuesday' THEN 2
                    WHEN 'Wednesday' THEN 3
                    WHEN 'Thursday' THEN 4
                    WHEN 'Friday' THEN 5
                END
        """)

        duties = cursor.fetchall()

        cursor.execute("""
            SELECT user_id, name
            FROM users
            WHERE is_active = 1
            ORDER BY name
        """)

        users = cursor.fetchall()

        db.close()

        return render_template(
            "locker_duty.html",
            user=session["user"],
            duties=duties,
            users=users,
            error=error
        )


    # Add the new assignment to the database.
    cursor.execute("""
        INSERT INTO locker_duty (user_id, week, day)
        VALUES (?, ?, ?)
    """, (user_id, week, day))

    db.commit()
    db.close()

    return redirect(url_for("locker_duty"))


# ==============================
# DELETE LOCKER DUTY
# ==============================

@app.route("/delete-locker-duty/<int:duty_id>", methods=["POST"])
def delete_locker_duty(duty_id):

    if "user" not in session:
        return redirect(url_for("index"))

    # Only administrators can remove assignments.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        DELETE FROM locker_duty
        WHERE duty_id = ?
    """, (duty_id,))

    db.commit()
    db.close()

    return redirect(url_for("locker_duty"))


# ==============================
# LOCKER DUTY EMAIL REMINDERS
# ==============================

def send_locker_duty_reminders():

    today = datetime.now()


    # Determine the next school day.
    if today.weekday() == 4:       # Friday
        next_duty_date = today + timedelta(days=3)

    elif today.weekday() == 5:     # Saturday
        next_duty_date = today + timedelta(days=2)

    elif today.weekday() == 6:     # Sunday
        next_duty_date = today + timedelta(days=1)

    else:                          # Monday - Thursday
        next_duty_date = today + timedelta(days=1)


    next_day = next_duty_date.strftime("%A")
    next_week = get_school_week(next_duty_date)

    db = get_db()
    cursor = db.cursor()


    # Find everyone assigned to the next school day's locker duty.
    cursor.execute("""
        SELECT
            users.user_id,
            users.name,
            users.email,
            locker_duty.week,
            locker_duty.day
        FROM locker_duty
        JOIN users
            ON locker_duty.user_id = users.user_id
        WHERE locker_duty.week = ?
        AND locker_duty.day = ?
    """, (next_week, next_day))

    assignments = cursor.fetchall()


    # Stop if nobody is assigned to the next school day.
    if not assignments:
        db.close()

        print(
            f"No locker duty assignments found for "
            f"{next_day}, Week {next_week}."
        )

        return


    for assignment in assignments:

        duty_date = next_duty_date.strftime("%Y-%m-%d")


        # Check whether a reminder has already been sent for this duty date.
        cursor.execute("""
            SELECT id
            FROM reminder_log
            WHERE user_id = ?
            AND duty_date = ?
        """, (
            assignment["user_id"],
            duty_date
        ))

        already_sent = cursor.fetchone()


        # Prevent duplicate reminder emails.
        if already_sent:
            print(
                f"Reminder already sent to "
                f"{assignment['name']} for {duty_date}"
            )
            continue


        # Send the reminder email.
        send_email(
            assignment["email"],
            "PrefectConnect - Locker Duty Reminder",
            f"""Hi {assignment["name"]},

This is a reminder that you have locker duty coming up.

Day: {assignment["day"]}
Week: {assignment["week"]}

Please remember to attend your locker duty.

Thanks,
PrefectConnect
"""
        )


        # Record that the reminder has been sent.
        cursor.execute("""
            INSERT INTO reminder_log (
                user_id,
                duty_date,
                sent_at
            )
            VALUES (?, ?, ?)
        """, (
            assignment["user_id"],
            duty_date,
            datetime.now().isoformat()
        ))

        db.commit()

        print(
            f"Locker duty reminder sent to "
            f"{assignment['name']} ({assignment['email']})"
        )

    db.close()


# ==============================
# MANUAL REMINDER TEST
# ==============================

@app.route("/send-tomorrow-reminders")
def send_tomorrow_reminders():

    if "user" not in session:
        return redirect(url_for("index"))

    # Only administrators can manually run the reminder system.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    send_locker_duty_reminders()

    return """
        <h1>Locker Duty Reminders Sent!</h1>

        <p>
            The reminder system has been run successfully.
        </p>

        <a href="/dashboard">
            Return to Dashboard
        </a>
    """


# ==============================
# GOOGLE LOGIN
# ==============================

@app.route("/login", methods=["POST"])
def login():

    token = request.json.get("credential")

    try:

        # Verify the Google login token.
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


        # Check whether the Google account exists in PrefectConnect.
        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cursor.fetchone()


        # Deny access if the account is not registered.
        if user is None:
            db.close()

            return jsonify({
                "status": "error",
                "redirect": "/403"
            }), 403


        # Store the user's information in the Flask session.
        session["user"] = {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"],
            "role": user["role"]
        }

        db.close()

        return jsonify({
            "status": "success",
            "redirect": "/dashboard"
        })


    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 401


# ==============================
# GMAIL AUTHORISATION
# ==============================

@app.route("/gmail/authorize")
def gmail_authorize():

    if "user" not in session:
        return redirect(url_for("index"))

    # Only administrators can connect Gmail.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    flow = create_flow()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent"
    )


    # Store OAuth information so the callback can restore the flow.
    session["gmail_state"] = state
    session["gmail_code_verifier"] = flow.code_verifier

    return redirect(authorization_url)


@app.route("/gmail/callback")
def gmail_callback():

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    flow = create_flow()

    # Restore the code verifier generated during authorisation.
    flow.code_verifier = session.get("gmail_code_verifier")

    flow.fetch_token(
        authorization_response=request.url
    )

    credentials = flow.credentials


    # Save the Gmail credentials so the app can send emails later.
    with open("gmail_token.json", "w") as token:
        token.write(credentials.to_json())


    # Remove temporary OAuth information from the session.
    session.pop("gmail_state", None)
    session.pop("gmail_code_verifier", None)

    return """
        <h1>Gmail Connected!</h1>
        <p>PrefectConnect can now send emails.</p>
        <a href="/dashboard">Return to Dashboard</a>
    """


# ==============================
# ASSEMBLIES
# ==============================

@app.route("/assemblies")
def assemblies():

    if "user" not in session:
        return redirect(url_for("index"))

    return render_template(
        "assembly.html",
        user=session["user"]
    )


# ==============================
# NOTICES
# ==============================

@app.route("/notices")
def notices():

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()


    # Retrieve all active notices.
    cursor.execute("""
        SELECT
            notice.notice_id,
            notice.title,
            notice.content,
            notice.created_at,
            users.name AS author
        FROM notice
        JOIN users
            ON notice.created_by = users.user_id
        WHERE notice.is_active = 1
        ORDER BY notice.created_at DESC
    """)

    notices = cursor.fetchall()


    # Get the current user's ID.
    user_id = session["user"]["user_id"]


    # Mark each active notice as read for this user.
    for notice in notices:

        cursor.execute("""
            INSERT OR IGNORE INTO notice_read
            (notice_id, user_id)
            VALUES (?, ?)
        """, (notice["notice_id"], user_id))

    db.commit()
    db.close()

    return render_template(
        "notices.html",
        user=session["user"],
        notices=notices
    )


@app.route("/add-notice", methods=["POST"])
def add_notice():

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    title = request.form["title"].strip()
    content = request.form["content"].strip()


    # Limit the length of notices.
    if len(title) > 50 or len(content) > 500:
        return redirect(url_for("notices"))

    # Limit the number of lines in a notice.
    if content.count("\n") >= 8:
        return redirect(url_for("notices"))


    user_id = session["user"]["user_id"]

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO notice (title, content, created_by)
        VALUES (?, ?, ?)
        """,
        (title, content, user_id)
    )

    db.commit()
    db.close()

    return redirect(url_for("notices"))


@app.route("/delete-notice/<int:notice_id>", methods=["POST"])
def delete_notice(notice_id):

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    # Soft-delete the notice by making it inactive.
    cursor.execute(
        """
        UPDATE notice
        SET is_active = 0
        WHERE notice_id = ?
        """,
        (notice_id,)
    )

    db.commit()
    db.close()

    return redirect(url_for("notices"))


# ==============================
# USER MANAGEMENT
# ==============================

@app.route("/users")
def users():

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    # Retrieve all registered users.
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


    # Prevent administrators from deleting their own account.
    if user_id == session["user"]["user_id"]:

        error = "You cannot delete your own account."

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
            users=users,
            error=error
        )


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


    # Prevent duplicate accounts from being created.
    cursor.execute(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        db.close()
        return redirect(url_for("users"))


    # Add the new user to the database.
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


    # Prevent administrators from removing their own admin privileges.
    if user_id == session["user"]["user_id"] and role != "admin":

        error = "You cannot remove your own admin privileges."

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
            users=users,
            error=error
        )


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


# ==============================
# ERROR / LOGOUT
# ==============================

@app.route("/403")
def forbidden():

    return render_template("403.html"), 403


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


# ==============================
# START APPLICATION
# ==============================

if __name__ == "__main__":

    scheduler = BackgroundScheduler()

    # Automatically run the locker duty reminder at 4:00 PM Monday-Friday.
    scheduler.add_job(
        send_locker_duty_reminders,
        "cron",
        day_of_week="mon-fri",
        hour=16,
        minute=0
    )

    scheduler.start()

    # Start the Flask development server.
    app.run(
        debug=True,
        use_reloader=False
    )