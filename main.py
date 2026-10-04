import os
import sqlite3
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from google.auth.transport import requests as grequests
from google.oauth2 import id_token

from gmail import create_flow, send_email


# School week configuration.
# The Monday that starts a known Week A.
WEEK_A_START = datetime(2026, 8, 10)

# Load environment variables from the .env file.
load_dotenv(override=True)

DATABASE = "prefectconnect.db"


def get_db():
    """Connect to the PrefectConnect SQLite database."""

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    return conn


def get_school_week(date):
    """Return whether the given date falls in Week A or Week B."""

    # Find the Monday of the week containing this date.
    monday = date - timedelta(days=date.weekday())

    # Calculate how many weeks have passed since Week A started.
    weeks_since_start = (
        monday.date() - WEEK_A_START.date()
    ).days // 7

    # Even weeks are Week A and odd weeks are Week B.
    if weeks_since_start % 2 == 0:
        return "A"

    return "B"


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


@app.route("/")
def index():
    """Display the login page."""

    user = session.get("user")

    return render_template(
        "index.html",
        user=user,
        client_id=GOOGLE_CLIENT_ID,
    )


@app.route("/dashboard")
def dashboard():
    """Display the dashboard and the user's next locker duty."""

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()

    user_id = session["user"]["user_id"]

    # Count active notices that this user has not read.
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM notice
        WHERE notice.is_active = 1
        AND notice.notice_id NOT IN (
            SELECT notice_id
            FROM notice_read
            WHERE user_id = ?
        )
        """,
        (user_id,),
    )

    notice_count = cursor.fetchone()[0]

    # Find the user's next locker duty.
    today = datetime.now()
    next_duty = None

    # Check the next 14 days.
    for days_ahead in range(14):
        check_date = today + timedelta(days=days_ahead)

        # Skip weekends.
        if check_date.weekday() >= 5:
            continue

        check_day = check_date.strftime("%A")
        check_week = get_school_week(check_date)

        cursor.execute(
            """
            SELECT
                locker_duty.day,
                locker_duty.week
            FROM locker_duty
            WHERE locker_duty.user_id = ?
            AND locker_duty.day = ?
            AND locker_duty.week = ?
            """,
            (
                user_id,
                check_day,
                check_week,
            ),
        )

        duty = cursor.fetchone()

        if duty is not None:
            next_duty = {
                "day": duty["day"],
                "week": duty["week"],
                "date": check_date.strftime("%d %B %Y"),
            }

            break

    db.close()

    return render_template(
        "dashboard.html",
        user=session["user"],
        notice_count=notice_count,
        next_duty=next_duty,
    )


@app.route("/locker-duty")
def locker_duty():
    """Display the locker duty roster."""

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()

    # Get locker duty assignments.
    cursor.execute(
        """
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
        """
    )

    duties = cursor.fetchall()

    # Get active users for the Add Person dropdown.
    cursor.execute(
        """
        SELECT user_id, name
        FROM users
        WHERE is_active = 1
        ORDER BY name
        """
    )

    users = cursor.fetchall()

    db.close()

    return render_template(
        "locker_duty.html",
        user=session["user"],
        duties=duties,
        users=users,
    )


@app.route("/add-locker-duty", methods=["POST"])
def add_locker_duty():
    """Add a person to the locker duty roster."""

    if "user" not in session:
        return redirect(url_for("index"))

    # Only admins can modify the roster.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    user_id = request.form["user_id"]
    week = request.form["week"]
    day = request.form["day"]

    db = get_db()
    cursor = db.cursor()

    # Check if this person is already assigned to this day.
    cursor.execute(
        """
        SELECT users.name
        FROM locker_duty
        JOIN users
            ON locker_duty.user_id = users.user_id
        WHERE locker_duty.user_id = ?
        AND locker_duty.week = ?
        AND locker_duty.day = ?
        """,
        (
            user_id,
            week,
            day,
        ),
    )

    existing_duty = cursor.fetchone()

    if existing_duty:
        error = (
            f"{existing_duty['name']} is already assigned to "
            f"{day}, Week {week}."
        )

        cursor.execute(
            """
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
            """
        )

        duties = cursor.fetchall()

        cursor.execute(
            """
            SELECT user_id, name
            FROM users
            WHERE is_active = 1
            ORDER BY name
            """
        )

        users = cursor.fetchall()

        db.close()

        return render_template(
            "locker_duty.html",
            user=session["user"],
            duties=duties,
            users=users,
            error=error,
        )

    # Check if the day already has two people.
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM locker_duty
        WHERE week = ? AND day = ?
        """,
        (
            week,
            day,
        ),
    )

    count = cursor.fetchone()[0]

    if count >= 2:
        error = (
            f"{day}, Week {week} already has two people assigned."
        )

        cursor.execute(
            """
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
            """
        )

        duties = cursor.fetchall()

        cursor.execute(
            """
            SELECT user_id, name
            FROM users
            WHERE is_active = 1
            ORDER BY name
            """
        )

        users = cursor.fetchall()

        db.close()

        return render_template(
            "locker_duty.html",
            user=session["user"],
            duties=duties,
            users=users,
            error=error,
        )

    # Add the new duty.
    cursor.execute(
        """
        INSERT INTO locker_duty (user_id, week, day)
        VALUES (?, ?, ?)
        """,
        (
            user_id,
            week,
            day,
        ),
    )

    db.commit()
    db.close()

    return redirect(url_for("locker_duty"))


@app.route("/delete-locker-duty/<int:duty_id>", methods=["POST"])
def delete_locker_duty(duty_id):
    """Remove a person from the locker duty roster."""

    if "user" not in session:
        return redirect(url_for("index"))

    # Only admins can remove people.
    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM locker_duty
        WHERE duty_id = ?
        """,
        (duty_id,),
    )

    db.commit()
    db.close()

    return redirect(url_for("locker_duty"))


def send_locker_duty_reminders():
    """Send reminders to users with duty on the next school day."""

    today = datetime.now()

    # Find the next school day.
    if today.weekday() == 4:
        next_duty_date = today + timedelta(days=3)
    elif today.weekday() == 5:
        next_duty_date = today + timedelta(days=2)
    elif today.weekday() == 6:
        next_duty_date = today + timedelta(days=1)
    else:
        next_duty_date = today + timedelta(days=1)

    next_day = next_duty_date.strftime("%A")
    next_week = get_school_week(next_duty_date)

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
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
        """,
        (
            next_week,
            next_day,
        ),
    )

    assignments = cursor.fetchall()

    if not assignments:
        db.close()

        print(
            f"No locker duty assignments found for "
            f"{next_day}, Week {next_week}."
        )

        return

    for assignment in assignments:
        duty_date = next_duty_date.strftime("%Y-%m-%d")

        cursor.execute(
            """
            SELECT id
            FROM reminder_log
            WHERE user_id = ?
            AND duty_date = ?
            """,
            (
                assignment["user_id"],
                duty_date,
            ),
        )

        already_sent = cursor.fetchone()

        if already_sent:
            print(
                f"Reminder already sent to "
                f"{assignment['name']} for {duty_date}"
            )

            continue

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
""",
        )

        cursor.execute(
            """
            INSERT INTO reminder_log (
                user_id,
                duty_date,
                sent_at
            )
            VALUES (?, ?, ?)
            """,
            (
                assignment["user_id"],
                duty_date,
                datetime.now().isoformat(),
            ),
        )

        db.commit()

        print(
            f"Locker duty reminder sent to "
            f"{assignment['name']} ({assignment['email']})"
        )

    db.close()


@app.route("/send-tomorrow-reminders")
def send_tomorrow_reminders():
    """Manually run the locker duty reminder system."""

    if "user" not in session:
        return redirect(url_for("index"))

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


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user using Google OAuth."""

    token = request.json.get("credential")

    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            grequests.Request(),
            GOOGLE_CLIENT_ID,
        )

        email = idinfo["email"]

        db = get_db()
        cursor = db.cursor()

        # Check if the user exists in the database.
        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,),
        )

        user = cursor.fetchone()

        # Deny access if the email is not registered.
        if user is None:
            db.close()

            return jsonify(
                {
                    "status": "error",
                    "redirect": "/403",
                }
            ), 403

        # Store the database user in the session.
        session["user"] = {
            "user_id": user["user_id"],
            "email": user["email"],
            "name": user["name"],
            "role": user["role"],
        }

        db.close()

        return jsonify(
            {
                "status": "success",
                "redirect": "/dashboard",
            }
        )

    except Exception as error:
        print("LOGIN ERROR:", error)

        return jsonify(
            {
                "status": "error",
                "message": str(error),
            }
        ), 401


# Gmail authorisation.

@app.route("/gmail/authorize")
def gmail_authorize():
    """Start the Gmail OAuth authorisation process."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    flow = create_flow()

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        prompt="consent",
    )

    # Save OAuth information for the callback.
    session["gmail_state"] = state
    session["gmail_code_verifier"] = flow.code_verifier

    return redirect(authorization_url)


@app.route("/gmail/callback")
def gmail_callback():
    """Handle the Gmail OAuth callback."""

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

    with open("gmail_token.json", "w") as token:
        token.write(credentials.to_json())

    # Remove temporary OAuth data.
    session.pop("gmail_state", None)
    session.pop("gmail_code_verifier", None)

    return """
        <h1>Gmail Connected!</h1>
        <p>PrefectConnect can now send emails.</p>
        <a href="/dashboard">Return to Dashboard</a>
    """


@app.route("/assemblies")
def assemblies():
    """Display the assemblies page."""

    if "user" not in session:
        return redirect(url_for("index"))

    return render_template(
        "assembly.html",
        user=session["user"],
    )


@app.route("/notices")
def notices():
    """Display active notices and mark them as read."""

    if "user" not in session:
        return redirect(url_for("index"))

    db = get_db()
    cursor = db.cursor()

    # Get all active notices.
    cursor.execute(
        """
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
        """
    )

    notices = cursor.fetchall()

    user_id = session["user"]["user_id"]

    # Mark all active notices as read for this user.
    for notice in notices:
        cursor.execute(
            """
            INSERT OR IGNORE INTO notice_read
            (notice_id, user_id)
            VALUES (?, ?)
            """,
            (
                notice["notice_id"],
                user_id,
            ),
        )

    db.commit()
    db.close()

    return render_template(
        "notices.html",
        user=session["user"],
        notices=notices,
    )


@app.route("/add-notice", methods=["POST"])
def add_notice():
    """Create a new notice."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    title = request.form["title"].strip()
    content = request.form["content"].strip()

    if len(title) > 50 or len(content) > 500:
        return redirect(url_for("notices"))

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
        (
            title,
            content,
            user_id,
        ),
    )

    db.commit()
    db.close()

    return redirect(url_for("notices"))


@app.route("/delete-notice/<int:notice_id>", methods=["POST"])
def delete_notice(notice_id):
    """Deactivate a notice."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE notice
        SET is_active = 0
        WHERE notice_id = ?
        """,
        (notice_id,),
    )

    db.commit()
    db.close()

    return redirect(url_for("notices"))


@app.route("/users")
def users():
    """Display the user management page."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        ORDER BY name
        """
    )

    users = cursor.fetchall()

    db.close()

    return render_template(
        "users.html",
        user=session["user"],
        users=users,
    )


@app.route("/delete-user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    """Delete a user unless they are the current administrator."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    # Prevent an admin from deleting their own account.
    if user_id == session["user"]["user_id"]:
        error = "You cannot delete your own account."

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            ORDER BY name
            """
        )

        users = cursor.fetchall()

        db.close()

        return render_template(
            "users.html",
            user=session["user"],
            users=users,
            error=error,
        )

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE user_id = ?
        """,
        (user_id,),
    )

    db.commit()
    db.close()

    return redirect(url_for("users"))


@app.route("/add-user", methods=["POST"])
def add_user():
    """Add a new user to PrefectConnect."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    name = request.form["name"]
    email = request.form["email"]
    role = request.form["role"]

    db = get_db()
    cursor = db.cursor()

    # Check if the email already exists.
    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,),
    )

    existing_user = cursor.fetchone()

    if existing_user:
        db.close()
        return redirect(url_for("users"))

    # Add the new user.
    cursor.execute(
        """
        INSERT INTO users (name, email, role)
        VALUES (?, ?, ?)
        """,
        (
            name,
            email,
            role,
        ),
    )

    db.commit()
    db.close()

    return redirect(url_for("users"))


@app.route("/edit-role/<int:user_id>", methods=["POST"])
def edit_role(user_id):
    """Change a user's role unless the current admin is being demoted."""

    if "user" not in session:
        return redirect(url_for("index"))

    if session["user"]["role"] != "admin":
        return render_template("403.html"), 403

    role = request.form["role"]

    # Prevent an admin from removing their own admin privileges.
    if user_id == session["user"]["user_id"] and role != "admin":
        error = "You cannot remove your own admin privileges."

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            ORDER BY name
            """
        )

        users = cursor.fetchall()

        db.close()

        return render_template(
            "users.html",
            user=session["user"],
            users=users,
            error=error,
        )

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE users
        SET role = ?
        WHERE user_id = ?
        """,
        (
            role,
            user_id,
        ),
    )

    db.commit()
    db.close()

    return redirect(url_for("users"))


@app.route("/403")
def forbidden():
    """Display the access denied page."""

    return render_template("403.html"), 403


@app.route("/logout")
def logout():
    """Log the current user out."""

    session.clear()

    return redirect(url_for("index"))


if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    # Run locker duty reminders automatically at 4:00 PM Monday-Friday.
    scheduler.add_job(
        send_locker_duty_reminders,
        "cron",
        day_of_week="mon-fri",
        hour=16,
        minute=0,
    )

    scheduler.start()

    # Start the Flask development server.
    app.run(
        debug=True,
        use_reloader=False,
    )