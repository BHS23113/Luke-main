Commit: 2d5f9ce
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:49:42 2026 +1200
Message: removed test bit
---
 main.py | 18 ------------------
 1 file changed, 18 deletions(-)

diff --git a/main.py b/main.py
index 0bc1710..2420acb 100644
--- a/main.py
+++ b/main.py
@@ -360,24 +360,6 @@ def send_locker_duty_reminders():
 
     assignments = cursor.fetchall()
 
-    print("========== REMINDER RUN ==========")
-    print("Assignments found:", len(assignments))
-
-    for assignment in assignments:
-        print(
-            "USER:",
-            assignment["user_id"],
-            "| NAME:",
-            assignment["name"],
-            "| EMAIL:",
-            assignment["email"],
-            "| WEEK:",
-            assignment["week"],
-            "| DAY:",
-            assignment["day"]
-        )
-
-    print("==================================")
 
     if not assignments:
         db.close()

Commit: 09dad20
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:47:49 2026 +1200
Message: set final time
---
 main.py | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 4a13975..0bc1710 100644
--- a/main.py
+++ b/main.py
@@ -857,8 +857,8 @@ if __name__ == "__main__":
         send_locker_duty_reminders,
         "cron",
         day_of_week="mon-fri",
-        hour=4,
-        minute=41
+        hour=16,
+        minute=0
     )
 
     scheduler.start()

Commit: dbe031a
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:46:04 2026 +1200
Message: removed extra send
---
 main.py | 4 ----
 1 file changed, 4 deletions(-)

diff --git a/main.py b/main.py
index 89be8a6..4a13975 100644
--- a/main.py
+++ b/main.py
@@ -451,10 +451,6 @@ PrefectConnect
 
     db.close()
 
-    print(
-        f"Locker duty reminder sent to "
-        f"{assignment['name']} ({assignment['email']})"
-    )
 
 @app.route("/send-tomorrow-reminders")
 def send_tomorrow_reminders():

Commit: f058b02
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:42:13 2026 +1200
Message: changing time to test extra send bug
---
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/main.py b/main.py
index 4c8641f..89be8a6 100644
--- a/main.py
+++ b/main.py
@@ -862,7 +862,7 @@ if __name__ == "__main__":
         "cron",
         day_of_week="mon-fri",
         hour=4,
-        minute=35
+        minute=41
     )
 
     scheduler.start()

Commit: 0dd0b44
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:39:07 2026 +1200
Message: debug
---
 main.py | 19 +++++++++++++++++++
 1 file changed, 19 insertions(+)

diff --git a/main.py b/main.py
index 234a5af..4c8641f 100644
--- a/main.py
+++ b/main.py
@@ -360,6 +360,25 @@ def send_locker_duty_reminders():
 
     assignments = cursor.fetchall()
 
+    print("========== REMINDER RUN ==========")
+    print("Assignments found:", len(assignments))
+
+    for assignment in assignments:
+        print(
+            "USER:",
+            assignment["user_id"],
+            "| NAME:",
+            assignment["name"],
+            "| EMAIL:",
+            assignment["email"],
+            "| WEEK:",
+            assignment["week"],
+            "| DAY:",
+            assignment["day"]
+        )
+
+    print("==================================")
+
     if not assignments:
         db.close()
 

Commit: 2a29753
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:32:51 2026 +1200
Message: test.2
---
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/main.py b/main.py
index bbc842d..234a5af 100644
--- a/main.py
+++ b/main.py
@@ -843,7 +843,7 @@ if __name__ == "__main__":
         "cron",
         day_of_week="mon-fri",
         hour=4,
-        minute=30
+        minute=35
     )
 
     scheduler.start()

Commit: daaafa0
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:31:25 2026 +1200
Message: change time
---
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/main.py b/main.py
index d360ea5..bbc842d 100644
--- a/main.py
+++ b/main.py
@@ -843,7 +843,7 @@ if __name__ == "__main__":
         "cron",
         day_of_week="mon-fri",
         hour=4,
-        minute=29
+        minute=30
     )
 
     scheduler.start()

Commit: 66ff87e
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:28:03 2026 +1200
Message: test
---
 main.py | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 86386ab..d360ea5 100644
--- a/main.py
+++ b/main.py
@@ -842,8 +842,8 @@ if __name__ == "__main__":
         send_locker_duty_reminders,
         "cron",
         day_of_week="mon-fri",
-        hour=16,
-        minute=0
+        hour=4,
+        minute=29
     )
 
     scheduler.start()

Commit: e464f48
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:26:42 2026 +1200
Message: added schedlur
---
 main.py | 15 +++++++++++++--
 1 file changed, 13 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 8f88783..86386ab 100644
--- a/main.py
+++ b/main.py
@@ -835,6 +835,17 @@ def logout():
 
 
 if __name__ == "__main__":
-    app.run(debug=True)
 
-    
\ No newline at end of file
+    scheduler = BackgroundScheduler()
+
+    scheduler.add_job(
+        send_locker_duty_reminders,
+        "cron",
+        day_of_week="mon-fri",
+        hour=16,
+        minute=0
+    )
+
+    scheduler.start()
+
+    app.run(debug=True, use_reloader=False)
\ No newline at end of file

Commit: d2b8fb6
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:25:59 2026 +1200
Message: completed func
---
 main.py | 49 +++++++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 47 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index a71a39e..8f88783 100644
--- a/main.py
+++ b/main.py
@@ -346,6 +346,7 @@ def send_locker_duty_reminders():
 
     cursor.execute("""
         SELECT
+            users.user_id,
             users.name,
             users.email,
             locker_duty.week,
@@ -359,17 +360,39 @@ def send_locker_duty_reminders():
 
     assignments = cursor.fetchall()
 
-    db.close()
-
     if not assignments:
+        db.close()
+
         print(
             f"No locker duty assignments found for "
             f"{next_day}, Week {next_week}."
         )
+
         return
 
     for assignment in assignments:
 
+        duty_date = next_duty_date.strftime("%Y-%m-%d")
+
+        cursor.execute("""
+            SELECT id
+            FROM reminder_log
+            WHERE user_id = ?
+            AND duty_date = ?
+        """, (
+            assignment["user_id"],
+            duty_date
+        ))
+
+        already_sent = cursor.fetchone()
+
+        if already_sent:
+            print(
+                f"Reminder already sent to "
+                f"{assignment['name']} for {duty_date}"
+            )
+            continue
+
         send_email(
             assignment["email"],
             "PrefectConnect - Locker Duty Reminder",
@@ -387,11 +410,33 @@ PrefectConnect
 """
         )
 
+        cursor.execute("""
+            INSERT INTO reminder_log (
+                user_id,
+                duty_date,
+                sent_at
+            )
+            VALUES (?, ?, ?)
+        """, (
+            assignment["user_id"],
+            duty_date,
+            datetime.now().isoformat()
+        ))
+
+        db.commit()
+
         print(
             f"Locker duty reminder sent to "
             f"{assignment['name']} ({assignment['email']})"
         )
 
+    db.close()
+
+    print(
+        f"Locker duty reminder sent to "
+        f"{assignment['name']} ({assignment['email']})"
+    )
+
 @app.route("/send-tomorrow-reminders")
 def send_tomorrow_reminders():
 

Commit: 0383e0d
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:02:10 2026 +1200
Message: added new table
---
 db.py | 10 ++++++++++
 1 file changed, 10 insertions(+)

diff --git a/db.py b/db.py
index 7541f6e..c8f4732 100644
--- a/db.py
+++ b/db.py
@@ -50,6 +50,16 @@ CREATE TABLE IF NOT EXISTS notice (
 )
 """)
 
+cursor.execute("""
+    CREATE TABLE IF NOT EXISTS reminder_log (
+        id INTEGER PRIMARY KEY AUTOINCREMENT,
+        user_id INTEGER NOT NULL,
+        duty_date TEXT NOT NULL,
+        sent_at TEXT NOT NULL,
+        UNIQUE(user_id, duty_date)
+    )
+""")
+
 
 # ==============================
 # NOTICE READ TABLE

Commit: cb523db
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 04:01:59 2026 +1200
Message: simplified route
---
 main.py | 65 ++++++++++++++++++++++++++++-------------------------------------
 1 file changed, 28 insertions(+), 37 deletions(-)

diff --git a/main.py b/main.py
index b1825c9..a71a39e 100644
--- a/main.py
+++ b/main.py
@@ -321,33 +321,24 @@ def delete_locker_duty(duty_id):
 
     return redirect(url_for("locker_duty"))
 
-@app.route("/send-tomorrow-reminders")
-def send_tomorrow_reminders():
-
-    if "user" not in session:
-        return redirect(url_for("index"))
-
-    if session["user"]["role"] != "admin":
-        return render_template("403.html"), 403
+def send_locker_duty_reminders():
 
     today = datetime.now()
 
     # Find the next school day
-    if today.weekday() == 4:  # Friday
+    if today.weekday() == 4:       # Friday
         next_duty_date = today + timedelta(days=3)
 
-    elif today.weekday() == 5:  # Saturday
+    elif today.weekday() == 5:     # Saturday
         next_duty_date = today + timedelta(days=2)
 
-    elif today.weekday() == 6:  # Sunday
+    elif today.weekday() == 6:     # Sunday
         next_duty_date = today + timedelta(days=1)
 
-    else:
-        # Monday → Thursday
+    else:                          # Monday - Thursday
         next_duty_date = today + timedelta(days=1)
 
     next_day = next_duty_date.strftime("%A")
-
     next_week = get_school_week(next_duty_date)
 
     db = get_db()
@@ -371,20 +362,11 @@ def send_tomorrow_reminders():
     db.close()
 
     if not assignments:
-        return f"""
-            <h1>No Locker Duty</h1>
-
-            <p>
-                No locker duty assignments were found for
-                {next_day}, Week {next_week}.
-            </p>
-
-            <a href="/dashboard">
-                Return to Dashboard
-            </a>
-        """
-
-    sent = []
+        print(
+            f"No locker duty assignments found for "
+            f"{next_day}, Week {next_week}."
+        )
+        return
 
     for assignment in assignments:
 
@@ -405,20 +387,29 @@ PrefectConnect
 """
         )
 
-        sent.append(assignment["name"])
+        print(
+            f"Locker duty reminder sent to "
+            f"{assignment['name']} ({assignment['email']})"
+        )
 
-    return f"""
-        <h1>Reminder Emails Sent!</h1>
+@app.route("/send-tomorrow-reminders")
+def send_tomorrow_reminders():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    send_locker_duty_reminders()
+
+    return """
+        <h1>Locker Duty Reminders Sent!</h1>
 
         <p>
-            Reminder emails were sent for
-            {next_day}, Week {next_week}.
+            The reminder system has been run successfully.
         </p>
 
-        <ul>
-            {''.join(f"<li>{name}</li>" for name in sent)}
-        </ul>
-
         <a href="/dashboard">
             Return to Dashboard
         </a>

Commit: 734c22e
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:56:22 2026 +1200
Message: got schedule pip
---
 main.py | 2 ++
 1 file changed, 2 insertions(+)

diff --git a/main.py b/main.py
index 35d9b91..b1825c9 100644
--- a/main.py
+++ b/main.py
@@ -11,6 +11,8 @@ from gmail import send_email
 
 from datetime import datetime, timedelta
 
+from apscheduler.schedulers.background import BackgroundScheduler
+
 # SCHOOL WEEK CONFIGURATION
 
 # The Monday that starts a known Week A.

Commit: 0a91e87
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:48:08 2026 +1200
Message: changed email to be more gramma
---
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/main.py b/main.py
index 78e27d9..35d9b91 100644
--- a/main.py
+++ b/main.py
@@ -391,7 +391,7 @@ def send_tomorrow_reminders():
             "PrefectConnect - Locker Duty Reminder",
             f"""Hi {assignment["name"]},
 
-This is a reminder that you have locker duty tomorrow.
+This is a reminder that you have locker duty coming up.
 
 Day: {assignment["day"]}
 Week: {assignment["week"]}

Commit: a207d0e
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:47:34 2026 +1200
Message: replaced temp route with new route
---
 main.py | 52 ++++++++++++++++++++++++++++++++++++++--------------
 1 file changed, 38 insertions(+), 14 deletions(-)

diff --git a/main.py b/main.py
index c3b6f39..78e27d9 100644
--- a/main.py
+++ b/main.py
@@ -325,19 +325,28 @@ def send_tomorrow_reminders():
     if "user" not in session:
         return redirect(url_for("index"))
 
-    # Only admins can send reminder emails
     if session["user"]["role"] != "admin":
         return render_template("403.html"), 403
 
-    from datetime import datetime, timedelta
+    today = datetime.now()
 
-    # Get tomorrow's day
-    tomorrow = datetime.now() + timedelta(days=1)
-    tomorrow_day = tomorrow.strftime("%A")
+    # Find the next school day
+    if today.weekday() == 4:  # Friday
+        next_duty_date = today + timedelta(days=3)
 
-    # Work out which week we're currently in
-    # TODO: Replace this with your actual Week A/B calendar system later.
-    current_week = session.get("current_week", "A")
+    elif today.weekday() == 5:  # Saturday
+        next_duty_date = today + timedelta(days=2)
+
+    elif today.weekday() == 6:  # Sunday
+        next_duty_date = today + timedelta(days=1)
+
+    else:
+        # Monday → Thursday
+        next_duty_date = today + timedelta(days=1)
+
+    next_day = next_duty_date.strftime("%A")
+
+    next_week = get_school_week(next_duty_date)
 
     db = get_db()
     cursor = db.cursor()
@@ -353,7 +362,7 @@ def send_tomorrow_reminders():
             ON locker_duty.user_id = users.user_id
         WHERE locker_duty.week = ?
         AND locker_duty.day = ?
-    """, (current_week, tomorrow_day))
+    """, (next_week, next_day))
 
     assignments = cursor.fetchall()
 
@@ -361,9 +370,16 @@ def send_tomorrow_reminders():
 
     if not assignments:
         return f"""
-            <h1>No Locker Duty Tomorrow</h1>
-            <p>There are no assignments for {tomorrow_day}, Week {current_week}.</p>
-            <a href="/dashboard">Return to Dashboard</a>
+            <h1>No Locker Duty</h1>
+
+            <p>
+                No locker duty assignments were found for
+                {next_day}, Week {next_week}.
+            </p>
+
+            <a href="/dashboard">
+                Return to Dashboard
+            </a>
         """
 
     sent = []
@@ -391,11 +407,19 @@ PrefectConnect
 
     return f"""
         <h1>Reminder Emails Sent!</h1>
-        <p>Emails were sent to:</p>
+
+        <p>
+            Reminder emails were sent for
+            {next_day}, Week {next_week}.
+        </p>
+
         <ul>
             {''.join(f"<li>{name}</li>" for name in sent)}
         </ul>
-        <a href="/dashboard">Return to Dashboard</a>
+
+        <a href="/dashboard">
+            Return to Dashboard
+        </a>
     """
 
 @app.route("/login", methods=["POST"])

Commit: 87bb22f
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:45:46 2026 +1200
Message: added func for school week config
---
 main.py | 25 +++++++++++++++++++++++++
 1 file changed, 25 insertions(+)

diff --git a/main.py b/main.py
index b561dfa..c3b6f39 100644
--- a/main.py
+++ b/main.py
@@ -28,6 +28,31 @@ def get_db():
     conn.row_factory = sqlite3.Row
     return conn
 
+from datetime import datetime, timedelta
+
+
+# SCHOOL WEEK CONFIGURATION
+
+WEEK_A_START = datetime(2026, 8, 10)
+
+
+def get_school_week(date):
+
+    # Find the Monday of the week containing this date
+    monday = date - timedelta(days=date.weekday())
+
+    # Calculate how many weeks have passed since Week A started
+    weeks_since_start = (
+        monday.date() - WEEK_A_START.date()
+    ).days // 7
+
+    # Even = Week A
+    # Odd = Week B
+    if weeks_since_start % 2 == 0:
+        return "A"
+
+    return "B"
+
 app = Flask(__name__)
 app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
 GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

Commit: 105039a
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:43:03 2026 +1200
Message: added school week config
---
 main.py | 8 ++++++++
 1 file changed, 8 insertions(+)

diff --git a/main.py b/main.py
index ddd50dc..b561dfa 100644
--- a/main.py
+++ b/main.py
@@ -9,6 +9,14 @@ from gmail import create_flow
 
 from gmail import send_email
 
+from datetime import datetime, timedelta
+
+# SCHOOL WEEK CONFIGURATION
+
+# The Monday that starts a known Week A.
+# Change this date if your school's Week A starts on a different Monday.
+WEEK_A_START = datetime(2026, 8, 10)
+
 print("Hello, World!")
 
 load_dotenv(override=True)

Commit: 40d0fdd
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:38:46 2026 +1200
Message: deleted test
---
 main.py | 20 --------------------
 1 file changed, 20 deletions(-)

diff --git a/main.py b/main.py
index 42d31f1..ddd50dc 100644
--- a/main.py
+++ b/main.py
@@ -726,27 +726,7 @@ def edit_role(user_id):
 
     return redirect(url_for("users")) 
 
-@app.route("/test-email")
-def test_email():
 
-    if "user" not in session:
-        return redirect(url_for("index"))
-
-    if session["user"]["role"] != "admin":
-        return render_template("403.html"), 403
-
-    send_email(
-        "lukegvsicloud@gmail.com",
-        "PrefectConnect Test Email",
-        "This is a test email sent from PrefectConnect."
-    )
-
-    return """
-        <h1>Email Sent!</h1>
-        <p>The test email was successfully sent.</p>
-        <a href="/dashboard">Return to Dashboard</a>
-    """
-    
 @app.route("/403")
 def forbidden():
 

Commit: c53229a
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:37:40 2026 +1200
Message: send email route
---
 main.py | 79 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 79 insertions(+)

diff --git a/main.py b/main.py
index 99b80d4..42d31f1 100644
--- a/main.py
+++ b/main.py
@@ -286,6 +286,85 @@ def delete_locker_duty(duty_id):
 
     return redirect(url_for("locker_duty"))
 
+@app.route("/send-tomorrow-reminders")
+def send_tomorrow_reminders():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    # Only admins can send reminder emails
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    from datetime import datetime, timedelta
+
+    # Get tomorrow's day
+    tomorrow = datetime.now() + timedelta(days=1)
+    tomorrow_day = tomorrow.strftime("%A")
+
+    # Work out which week we're currently in
+    # TODO: Replace this with your actual Week A/B calendar system later.
+    current_week = session.get("current_week", "A")
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute("""
+        SELECT
+            users.name,
+            users.email,
+            locker_duty.week,
+            locker_duty.day
+        FROM locker_duty
+        JOIN users
+            ON locker_duty.user_id = users.user_id
+        WHERE locker_duty.week = ?
+        AND locker_duty.day = ?
+    """, (current_week, tomorrow_day))
+
+    assignments = cursor.fetchall()
+
+    db.close()
+
+    if not assignments:
+        return f"""
+            <h1>No Locker Duty Tomorrow</h1>
+            <p>There are no assignments for {tomorrow_day}, Week {current_week}.</p>
+            <a href="/dashboard">Return to Dashboard</a>
+        """
+
+    sent = []
+
+    for assignment in assignments:
+
+        send_email(
+            assignment["email"],
+            "PrefectConnect - Locker Duty Reminder",
+            f"""Hi {assignment["name"]},
+
+This is a reminder that you have locker duty tomorrow.
+
+Day: {assignment["day"]}
+Week: {assignment["week"]}
+
+Please remember to attend your locker duty.
+
+Thanks,
+PrefectConnect
+"""
+        )
+
+        sent.append(assignment["name"])
+
+    return f"""
+        <h1>Reminder Emails Sent!</h1>
+        <p>Emails were sent to:</p>
+        <ul>
+            {''.join(f"<li>{name}</li>" for name in sent)}
+        </ul>
+        <a href="/dashboard">Return to Dashboard</a>
+    """
+
 @app.route("/login", methods=["POST"])
 def login():
 

Commit: a4f8877
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:36:48 2026 +1200
Message: reject email if adress invalid
---
 gmail.py | 10 ++++++++--
 1 file changed, 8 insertions(+), 2 deletions(-)

diff --git a/gmail.py b/gmail.py
index 474c244..76ac7aa 100644
--- a/gmail.py
+++ b/gmail.py
@@ -42,8 +42,15 @@ def create_flow():
     return flow
 
 
+from email.utils import parseaddr
+
 def send_email(to_email, subject, body):
 
+    name, address = parseaddr(to_email)
+
+    if not address or "@" not in address:
+        raise ValueError(f"Invalid recipient email address: {to_email}")
+
     token_file = "gmail_token.json"
 
     if not os.path.exists(token_file):
@@ -57,7 +64,6 @@ def send_email(to_email, subject, body):
     )
 
     if credentials.expired and credentials.refresh_token:
-
         credentials.refresh(Request())
 
         with open(token_file, "w") as token:
@@ -71,7 +77,7 @@ def send_email(to_email, subject, body):
 
     message = EmailMessage()
 
-    message["To"] = to_email
+    message["To"] = address
     message["Subject"] = subject
 
     message.set_content(body)

Commit: 44cfc7b
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:28:22 2026 +1200
Message: test email
---
 main.py | 23 +++++++++++++++++++++++
 1 file changed, 23 insertions(+)

diff --git a/main.py b/main.py
index 6f3faf7..99b80d4 100644
--- a/main.py
+++ b/main.py
@@ -7,6 +7,8 @@ import os
 
 from gmail import create_flow
 
+from gmail import send_email
+
 print("Hello, World!")
 
 load_dotenv(override=True)
@@ -644,6 +646,27 @@ def edit_role(user_id):
     db.close()
 
     return redirect(url_for("users")) 
+
+@app.route("/test-email")
+def test_email():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    send_email(
+        "lukegvsicloud@gmail.com",
+        "PrefectConnect Test Email",
+        "This is a test email sent from PrefectConnect."
+    )
+
+    return """
+        <h1>Email Sent!</h1>
+        <p>The test email was successfully sent.</p>
+        <a href="/dashboard">Return to Dashboard</a>
+    """
     
 @app.route("/403")
 def forbidden():

Commit: a061e47
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:23:30 2026 +1200
Message: ignored more stuff
---
 .gitignore | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

diff --git a/.gitignore b/.gitignore
index b419381..85fc2eb 100644
--- a/.gitignore
+++ b/.gitignore
@@ -4,4 +4,5 @@
 .env
 *.db
 *.exe
-__pycache__/
\ No newline at end of file
+__pycache__/
+gmail_token.json
\ No newline at end of file

Commit: 14753b6
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:21:22 2026 +1200
Message: fixed gmail
---
 gmail.py | 5 +++++
 1 file changed, 5 insertions(+)

diff --git a/gmail.py b/gmail.py
index 8df1116..474c244 100644
--- a/gmail.py
+++ b/gmail.py
@@ -27,6 +27,9 @@ CLIENT_CONFIG = {
 
 def create_flow():
 
+    print("GMAIL CLIENT ID LOADED:", bool(os.getenv("GOOGLE_CLIENT_ID")))
+    print("GMAIL CLIENT SECRET LOADED:", bool(os.getenv("GOOGLE_CLIENT_SECRET")))
+
     flow = Flow.from_client_config(
         CLIENT_CONFIG,
         scopes=SCOPES
@@ -34,6 +37,8 @@ def create_flow():
 
     flow.redirect_uri = "http://localhost:5000/gmail/callback"
 
+    print("GMAIL REDIRECT URI:", flow.redirect_uri)
+
     return flow
 
 

Commit: d0e1168
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 03:21:01 2026 +1200
Message: fixed route
---
 main.py | 11 ++++++++++-
 1 file changed, 10 insertions(+), 1 deletion(-)

diff --git a/main.py b/main.py
index d3dd9cd..6f3faf7 100644
--- a/main.py
+++ b/main.py
@@ -357,11 +357,13 @@ def gmail_authorize():
 
     authorization_url, state = flow.authorization_url(
         access_type="offline",
-        include_granted_scopes="true",
         prompt="consent"
     )
 
+    # Save OAuth information so the callback can recreate
+    # the exact same OAuth flow
     session["gmail_state"] = state
+    session["gmail_code_verifier"] = flow.code_verifier
 
     return redirect(authorization_url)
 
@@ -377,6 +379,9 @@ def gmail_callback():
 
     flow = create_flow()
 
+    # Restore the code verifier generated during /gmail/authorize
+    flow.code_verifier = session.get("gmail_code_verifier")
+
     flow.fetch_token(
         authorization_response=request.url
     )
@@ -386,6 +391,10 @@ def gmail_callback():
     with open("gmail_token.json", "w") as token:
         token.write(credentials.to_json())
 
+    # Remove temporary OAuth data
+    session.pop("gmail_state", None)
+    session.pop("gmail_code_verifier", None)
+
     return """
         <h1>Gmail Connected!</h1>
         <p>PrefectConnect can now send emails.</p>

Commit: 3afee95
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:43:54 2026 +1200
Message: dont mind this
---
 __pycache__/gmail.cpython-314.pyc | Bin 2940 -> 0 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)

diff --git a/__pycache__/gmail.cpython-314.pyc b/__pycache__/gmail.cpython-314.pyc
deleted file mode 100644
index a84831f..0000000
Binary files a/__pycache__/gmail.cpython-314.pyc and /dev/null differ

Commit: efe5057
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:41:23 2026 +1200
Message: ignore
---
 .gitignore | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

diff --git a/.gitignore b/.gitignore
index 3ef1e0e..b419381 100644
--- a/.gitignore
+++ b/.gitignore
@@ -3,4 +3,5 @@
 /bin
 .env
 *.db
-*.exe
\ No newline at end of file
+*.exe
+__pycache__/
\ No newline at end of file

Commit: 6c1aedd
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:15:04 2026 +1200
Message: fixed gmail
---
 gmail.py | 1 +
 1 file changed, 1 insertion(+)

diff --git a/gmail.py b/gmail.py
index 74b03cb..8df1116 100644
--- a/gmail.py
+++ b/gmail.py
@@ -1,4 +1,5 @@
 import os
+os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
 import base64
 from email.message import EmailMessage
 

Commit: a7ade35
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:14:51 2026 +1200
Message: this thing got created
---
 __pycache__/gmail.cpython-314.pyc | Bin 0 -> 2940 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)

diff --git a/__pycache__/gmail.cpython-314.pyc b/__pycache__/gmail.cpython-314.pyc
new file mode 100644
index 0000000..a84831f
Binary files /dev/null and b/__pycache__/gmail.cpython-314.pyc differ

Commit: 2d8ffbe
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:14:43 2026 +1200
Message: added the gmail route
---
 main.py | 51 +++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 51 insertions(+)

diff --git a/main.py b/main.py
index 66f2d34..d3dd9cd 100644
--- a/main.py
+++ b/main.py
@@ -4,6 +4,7 @@ from google.auth.transport import requests as grequests
 from dotenv import load_dotenv
 import sqlite3
 import os
+
 from gmail import create_flow
 
 print("Hello, World!")
@@ -340,6 +341,56 @@ def login():
             "status": "error",
             "message": str(e)
         }), 401
+    
+# GMAIL AUTHORISATION
+
+@app.route("/gmail/authorize")
+def gmail_authorize():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    flow = create_flow()
+
+    authorization_url, state = flow.authorization_url(
+        access_type="offline",
+        include_granted_scopes="true",
+        prompt="consent"
+    )
+
+    session["gmail_state"] = state
+
+    return redirect(authorization_url)
+
+
+@app.route("/gmail/callback")
+def gmail_callback():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    flow = create_flow()
+
+    flow.fetch_token(
+        authorization_response=request.url
+    )
+
+    credentials = flow.credentials
+
+    with open("gmail_token.json", "w") as token:
+        token.write(credentials.to_json())
+
+    return """
+        <h1>Gmail Connected!</h1>
+        <p>PrefectConnect can now send emails.</p>
+        <a href="/dashboard">Return to Dashboard</a>
+    """
 
 @app.route("/assemblies")
 def assemblies():

Commit: 3afe17b
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:02:28 2026 +1200
Message: linked gmail.py to main
---
 main.py | 1 +
 1 file changed, 1 insertion(+)

diff --git a/main.py b/main.py
index 0d3c4eb..66f2d34 100644
--- a/main.py
+++ b/main.py
@@ -4,6 +4,7 @@ from google.auth.transport import requests as grequests
 from dotenv import load_dotenv
 import sqlite3
 import os
+from gmail import create_flow
 
 print("Hello, World!")
 

Commit: fd6477a
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 01:01:13 2026 +1200
Message: created gmail.py
---
 gmail.py | 84 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 84 insertions(+)

diff --git a/gmail.py b/gmail.py
new file mode 100644
index 0000000..74b03cb
--- /dev/null
+++ b/gmail.py
@@ -0,0 +1,84 @@
+import os
+import base64
+from email.message import EmailMessage
+
+from google_auth_oauthlib.flow import Flow
+from googleapiclient.discovery import build
+from google.auth.transport.requests import Request
+
+
+SCOPES = [
+    "https://www.googleapis.com/auth/gmail.send"
+]
+
+CLIENT_CONFIG = {
+    "web": {
+        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
+        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
+        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
+        "token_uri": "https://oauth2.googleapis.com/token",
+        "redirect_uris": [
+            "http://localhost:5000/gmail/callback"
+        ]
+    }
+}
+
+
+def create_flow():
+
+    flow = Flow.from_client_config(
+        CLIENT_CONFIG,
+        scopes=SCOPES
+    )
+
+    flow.redirect_uri = "http://localhost:5000/gmail/callback"
+
+    return flow
+
+
+def send_email(to_email, subject, body):
+
+    token_file = "gmail_token.json"
+
+    if not os.path.exists(token_file):
+        raise Exception("Gmail has not been connected yet.")
+
+    from google.oauth2.credentials import Credentials
+
+    credentials = Credentials.from_authorized_user_file(
+        token_file,
+        SCOPES
+    )
+
+    if credentials.expired and credentials.refresh_token:
+
+        credentials.refresh(Request())
+
+        with open(token_file, "w") as token:
+            token.write(credentials.to_json())
+
+    service = build(
+        "gmail",
+        "v1",
+        credentials=credentials
+    )
+
+    message = EmailMessage()
+
+    message["To"] = to_email
+    message["Subject"] = subject
+
+    message.set_content(body)
+
+    encoded_message = base64.urlsafe_b64encode(
+        message.as_bytes()
+    ).decode()
+
+    message_body = {
+        "raw": encoded_message
+    }
+
+    service.users().messages().send(
+        userId="me",
+        body=message_body
+    ).execute()
\ No newline at end of file

Commit: 13dc705
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 00:23:01 2026 +1200
Message: fixed locker duty front end
---
 static/css/locker_duty.css | 6 ++++++
 templates/locker_duty.html | 2 +-
 2 files changed, 7 insertions(+), 1 deletion(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index cc7e0c7..40225e8 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -389,4 +389,10 @@
         padding: 25px;
     }
 
+}
+
+/* SHOW ADD DUTY MODAL WHEN THERE IS AN ERROR */
+
+.modal.show-modal {
+    display: flex;
 }
\ No newline at end of file
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index e149d47..e84277b 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -307,7 +307,7 @@ Locker Duty
 
 {% if user.role == "admin" %}
 
-<div id="addDutyModal" class="modal">
+<div id="addDutyModal" class="modal {% if error %}show-modal{% endif %}">
 
     <div class="modal-content">
 

Commit: 17ae351
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 00:19:22 2026 +1200
Message: added front end for error
---
 static/css/locker_duty.css | 23 ++++++++++++++++++++++-
 templates/locker_duty.html | 25 +++++++++++++++++++++++--
 2 files changed, 45 insertions(+), 3 deletions(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 23f6482..cc7e0c7 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -1,4 +1,3 @@
-
 /* LOCKER DUTY PAGE */
 
 .topbar {
@@ -139,6 +138,7 @@
     color: white;
 
     border: none;
+
     border-radius: 6px;
 
     padding: 6px 10px;
@@ -249,6 +249,27 @@
 }
 
 
+/* FORM ERROR */
+
+.form-error {
+    background-color: #fde8e8;
+
+    color: #b42318;
+
+    border: 1px solid #f5c2c0;
+
+    padding: 10px 12px;
+
+    border-radius: 8px;
+
+    margin-bottom: 15px;
+
+    font-size: 14px;
+
+    font-weight: 600;
+}
+
+
 /* MODAL BUTTONS */
 
 .modal-actions {
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index b1db5e9..e149d47 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -28,6 +28,7 @@ Locker Duty
 <div class="actions">
 
     <button
+        type="button"
         class="button"
         onclick="openAddDutyModal()">
 
@@ -70,7 +71,6 @@ Locker Duty
                         {{ day }}
                     </td>
 
-
                     {% set day_duties = duties
                         | selectattr("week", "equalto", "A")
                         | selectattr("day", "equalto", day)
@@ -202,7 +202,6 @@ Locker Duty
                         {{ day }}
                     </td>
 
-
                     {% set day_duties = duties
                         | selectattr("week", "equalto", "B")
                         | selectattr("day", "equalto", day)
@@ -314,10 +313,26 @@ Locker Duty
 
         <h2>Add Locker Duty</h2>
 
+
+        <!-- ERROR MESSAGE -->
+
+        {% if error %}
+
+        <div class="form-error">
+            {{ error }}
+        </div>
+
+        {% endif %}
+
+
+        <!-- ADD DUTY FORM -->
+
         <form
             action="/add-locker-duty"
             method="POST">
 
+            <!-- PERSON -->
+
             <label>
                 Person
             </label>
@@ -341,6 +356,8 @@ Locker Duty
             </select>
 
 
+            <!-- WEEK -->
+
             <label>
                 Week
             </label>
@@ -360,6 +377,8 @@ Locker Duty
             </select>
 
 
+            <!-- DAY -->
+
             <label>
                 Day
             </label>
@@ -391,6 +410,8 @@ Locker Duty
             </select>
 
 
+            <!-- BUTTONS -->
+
             <div class="modal-actions">
 
                 <button

Commit: 11e565b
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 00:18:13 2026 +1200
Message: change js
---
 static/script.js | 136 +++++++++++++++++++++++++++++++------------------------
 1 file changed, 76 insertions(+), 60 deletions(-)

diff --git a/static/script.js b/static/script.js
index 5f2b572..e6526b7 100644
--- a/static/script.js
+++ b/static/script.js
@@ -1,4 +1,4 @@
-// GOOGLE LOGIN 
+// GOOGLE LOGIN
 
 function handleCredentialResponse(response) {
 
@@ -43,7 +43,7 @@ function handleCredentialResponse(response) {
 }
 
 
-// DELETE USER 
+// DELETE USER
 
 function openDeleteModal(id, name) {
 
@@ -51,8 +51,8 @@ function openDeleteModal(id, name) {
 
     document.getElementById("deleteName").textContent = name;
 
-    document.getElementById("deleteForm").action = "/delete-user/" + id;
-
+    document.getElementById("deleteForm").action =
+        "/delete-user/" + id;
 }
 
 
@@ -63,7 +63,7 @@ function closeDeleteModal() {
 }
 
 
-// ADD USER 
+// ADD USER
 
 function openAddUserModal() {
 
@@ -89,7 +89,8 @@ function openRoleModal(id, name, role) {
 
     document.getElementById("roleSelect").value = role;
 
-    document.getElementById("roleForm").action = "/edit-role/" + id;
+    document.getElementById("roleForm").action =
+        "/edit-role/" + id;
 
 }
 
@@ -101,44 +102,6 @@ function closeRoleModal() {
 }
 
 
-// CLOSE MODALS
-
-window.addEventListener("click", function(event) {
-
-    const deleteModal = document.getElementById("deleteModal");
-    const addUserModal = document.getElementById("addUserModal");
-    const roleModal = document.getElementById("roleModal");
-
-    const addDutyModal = document.getElementById("addDutyModal");
-    const deleteDutyModal = document.getElementById("deleteDutyModal");
-
-
-    if (deleteModal && event.target === deleteModal) {
-        closeDeleteModal();
-    }
-
-
-    if (addUserModal && event.target === addUserModal) {
-        closeAddUserModal();
-    }
-
-
-    if (roleModal && event.target === roleModal) {
-        closeRoleModal();
-    }
-
-
-    if (addDutyModal && event.target === addDutyModal) {
-        closeAddDutyModal();
-    }
-
-
-    if (deleteDutyModal && event.target === deleteDutyModal) {
-        closeDeleteDutyModal();
-    }
-
-});
-
 // ADD NOTICE
 
 function openAddNoticeModal() {
@@ -147,12 +110,14 @@ function openAddNoticeModal() {
 
 }
 
+
 function closeAddNoticeModal() {
 
     document.getElementById("addNoticeModal").style.display = "none";
 
 }
 
+
 // DELETE NOTICE
 
 function openDeleteNoticeModal(id, title) {
@@ -173,7 +138,8 @@ function closeDeleteNoticeModal() {
 
 }
 
-//  NOTICE LINE LIMIT 
+
+// NOTICE LINE LIMIT
 
 const noticeTextarea = document.querySelector(
     '#addNoticeModal textarea[name="content"]'
@@ -198,17 +164,23 @@ if (noticeTextarea) {
 }
 
 
-// ADD LOCKER DUTY MODAL
+// ADD LOCKER DUTY
 
 function openAddDutyModal() {
+
     document.getElementById("addDutyModal").style.display = "flex";
+
 }
 
+
 function closeAddDutyModal() {
+
     document.getElementById("addDutyModal").style.display = "none";
+
 }
 
-// DELETE LOCKER DUTY MODAL
+
+// DELETE LOCKER DUTY
 
 function openDeleteDutyModal(dutyId, name) {
 
@@ -218,31 +190,75 @@ function openDeleteDutyModal(dutyId, name) {
         "/delete-locker-duty/" + dutyId;
 
     document.getElementById("deleteDutyModal").style.display = "flex";
+
 }
 
 
 function closeDeleteDutyModal() {
 
     document.getElementById("deleteDutyModal").style.display = "none";
+
 }
 
-console.log("LOCKER DUTY DELETE JS LOADED");
 
-function openDeleteDutyModal(dutyId, name) {
+// CLOSE MODALS WHEN CLICKING OUTSIDE
 
-    console.log("DELETE BUTTON CLICKED");
-    console.log("Duty ID:", dutyId);
-    console.log("Name:", name);
+window.addEventListener("click", function(event) {
 
-    document.getElementById("deleteDutyName").textContent = name;
+    const deleteModal =
+        document.getElementById("deleteModal");
 
-    document.getElementById("deleteDutyForm").action =
-        "/delete-locker-duty/" + dutyId;
+    const addUserModal =
+        document.getElementById("addUserModal");
 
-    document.getElementById("deleteDutyModal").style.display = "flex";
-}
+    const roleModal =
+        document.getElementById("roleModal");
 
-function closeDeleteDutyModal() {
+    const addDutyModal =
+        document.getElementById("addDutyModal");
 
-    document.getElementById("deleteDutyModal").style.display = "none";
-}
\ No newline at end of file
+    const deleteDutyModal =
+        document.getElementById("deleteDutyModal");
+
+    const addNoticeModal =
+        document.getElementById("addNoticeModal");
+
+    const deleteNoticeModal =
+        document.getElementById("deleteNoticeModal");
+
+
+    if (deleteModal && event.target === deleteModal) {
+        closeDeleteModal();
+    }
+
+
+    if (addUserModal && event.target === addUserModal) {
+        closeAddUserModal();
+    }
+
+
+    if (roleModal && event.target === roleModal) {
+        closeRoleModal();
+    }
+
+
+    if (addDutyModal && event.target === addDutyModal) {
+        closeAddDutyModal();
+    }
+
+
+    if (deleteDutyModal && event.target === deleteDutyModal) {
+        closeDeleteDutyModal();
+    }
+
+
+    if (addNoticeModal && event.target === addNoticeModal) {
+        closeAddNoticeModal();
+    }
+
+
+    if (deleteNoticeModal && event.target === deleteNoticeModal) {
+        closeDeleteNoticeModal();
+    }
+
+});
\ No newline at end of file

Commit: d648511
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 21 00:17:19 2026 +1200
Message: change route for same person in day twice
---
 main.py | 107 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++------
 1 file changed, 98 insertions(+), 9 deletions(-)

diff --git a/main.py b/main.py
index 64cd323..0d3c4eb 100644
--- a/main.py
+++ b/main.py
@@ -130,22 +130,68 @@ def add_locker_duty():
     db = get_db()
     cursor = db.cursor()
 
-    # Check if this person is already assigned to this exact day
+    # Check if this person is already assigned to this day
     cursor.execute("""
-        SELECT *
+        SELECT users.name
         FROM locker_duty
-        WHERE user_id = ?
-        AND week = ?
-        AND day = ?
+        JOIN users
+            ON locker_duty.user_id = users.user_id
+        WHERE locker_duty.user_id = ?
+        AND locker_duty.week = ?
+        AND locker_duty.day = ?
     """, (user_id, week, day))
 
     existing_duty = cursor.fetchone()
 
     if existing_duty:
+
+        error = f"{existing_duty['name']} is already assigned to {day}, Week {week}."
+
+        # Get duties again
+        cursor.execute("""
+            SELECT
+                locker_duty.duty_id,
+                locker_duty.user_id,
+                locker_duty.week,
+                locker_duty.day,
+                users.name
+            FROM locker_duty
+            JOIN users
+                ON locker_duty.user_id = users.user_id
+            ORDER BY
+                locker_duty.week,
+                CASE locker_duty.day
+                    WHEN 'Monday' THEN 1
+                    WHEN 'Tuesday' THEN 2
+                    WHEN 'Wednesday' THEN 3
+                    WHEN 'Thursday' THEN 4
+                    WHEN 'Friday' THEN 5
+                END
+        """)
+
+        duties = cursor.fetchall()
+
+        # Get users again
+        cursor.execute("""
+            SELECT user_id, name
+            FROM users
+            WHERE is_active = 1
+            ORDER BY name
+        """)
+
+        users = cursor.fetchall()
+
         db.close()
-        return redirect(url_for("locker_duty"))
 
-    # Check how many people are already assigned
+        return render_template(
+            "locker_duty.html",
+            user=session["user"],
+            duties=duties,
+            users=users,
+            error=error
+        )
+
+    # Check if the day already has two people
     cursor.execute("""
         SELECT COUNT(*)
         FROM locker_duty
@@ -154,10 +200,53 @@ def add_locker_duty():
 
     count = cursor.fetchone()[0]
 
-    # Maximum of 2 people per day
     if count >= 2:
+
+        error = f"{day}, Week {week} already has two people assigned."
+
+        # Get duties again
+        cursor.execute("""
+            SELECT
+                locker_duty.duty_id,
+                locker_duty.user_id,
+                locker_duty.week,
+                locker_duty.day,
+                users.name
+            FROM locker_duty
+            JOIN users
+                ON locker_duty.user_id = users.user_id
+            ORDER BY
+                locker_duty.week,
+                CASE locker_duty.day
+                    WHEN 'Monday' THEN 1
+                    WHEN 'Tuesday' THEN 2
+                    WHEN 'Wednesday' THEN 3
+                    WHEN 'Thursday' THEN 4
+                    WHEN 'Friday' THEN 5
+                END
+        """)
+
+        duties = cursor.fetchall()
+
+        # Get users again
+        cursor.execute("""
+            SELECT user_id, name
+            FROM users
+            WHERE is_active = 1
+            ORDER BY name
+        """)
+
+        users = cursor.fetchall()
+
         db.close()
-        return redirect(url_for("locker_duty"))
+
+        return render_template(
+            "locker_duty.html",
+            user=session["user"],
+            duties=duties,
+            users=users,
+            error=error
+        )
 
     # Add the new duty
     cursor.execute("""

Commit: 98d577d
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Aug 20 17:37:30 2026 +1200
Message: made it so you can only be in one day locker duty at a time
---
 main.py | 17 ++++++++++++++++-
 1 file changed, 16 insertions(+), 1 deletion(-)

diff --git a/main.py b/main.py
index 7f47508..64cd323 100644
--- a/main.py
+++ b/main.py
@@ -130,6 +130,21 @@ def add_locker_duty():
     db = get_db()
     cursor = db.cursor()
 
+    # Check if this person is already assigned to this exact day
+    cursor.execute("""
+        SELECT *
+        FROM locker_duty
+        WHERE user_id = ?
+        AND week = ?
+        AND day = ?
+    """, (user_id, week, day))
+
+    existing_duty = cursor.fetchone()
+
+    if existing_duty:
+        db.close()
+        return redirect(url_for("locker_duty"))
+
     # Check how many people are already assigned
     cursor.execute("""
         SELECT COUNT(*)
@@ -142,7 +157,7 @@ def add_locker_duty():
     # Maximum of 2 people per day
     if count >= 2:
         db.close()
-        return "This day already has two people assigned.", 400
+        return redirect(url_for("locker_duty"))
 
     # Add the new duty
     cursor.execute("""

Commit: d18de3b
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:41:53 2026 +1200
Message: added js path
---
 static/script.js | 60 ++++++++++++++++++++++++++++++++++++++++++++++++--------
 1 file changed, 52 insertions(+), 8 deletions(-)

diff --git a/static/script.js b/static/script.js
index 1d8da9f..5f2b572 100644
--- a/static/script.js
+++ b/static/script.js
@@ -101,35 +101,40 @@ function closeRoleModal() {
 }
 
 
-// CLOSE MODALS  
+// CLOSE MODALS
 
 window.addEventListener("click", function(event) {
 
     const deleteModal = document.getElementById("deleteModal");
-
     const addUserModal = document.getElementById("addUserModal");
-
     const roleModal = document.getElementById("roleModal");
 
+    const addDutyModal = document.getElementById("addDutyModal");
+    const deleteDutyModal = document.getElementById("deleteDutyModal");
 
-    if (deleteModal && event.target === deleteModal) {
 
+    if (deleteModal && event.target === deleteModal) {
         closeDeleteModal();
-
     }
 
 
     if (addUserModal && event.target === addUserModal) {
-
         closeAddUserModal();
-
     }
 
 
     if (roleModal && event.target === roleModal) {
-
         closeRoleModal();
+    }
 
+
+    if (addDutyModal && event.target === addDutyModal) {
+        closeAddDutyModal();
+    }
+
+
+    if (deleteDutyModal && event.target === deleteDutyModal) {
+        closeDeleteDutyModal();
     }
 
 });
@@ -201,4 +206,43 @@ function openAddDutyModal() {
 
 function closeAddDutyModal() {
     document.getElementById("addDutyModal").style.display = "none";
+}
+
+// DELETE LOCKER DUTY MODAL
+
+function openDeleteDutyModal(dutyId, name) {
+
+    document.getElementById("deleteDutyName").textContent = name;
+
+    document.getElementById("deleteDutyForm").action =
+        "/delete-locker-duty/" + dutyId;
+
+    document.getElementById("deleteDutyModal").style.display = "flex";
+}
+
+
+function closeDeleteDutyModal() {
+
+    document.getElementById("deleteDutyModal").style.display = "none";
+}
+
+console.log("LOCKER DUTY DELETE JS LOADED");
+
+function openDeleteDutyModal(dutyId, name) {
+
+    console.log("DELETE BUTTON CLICKED");
+    console.log("Duty ID:", dutyId);
+    console.log("Name:", name);
+
+    document.getElementById("deleteDutyName").textContent = name;
+
+    document.getElementById("deleteDutyForm").action =
+        "/delete-locker-duty/" + dutyId;
+
+    document.getElementById("deleteDutyModal").style.display = "flex";
+}
+
+function closeDeleteDutyModal() {
+
+    document.getElementById("deleteDutyModal").style.display = "none";
 }
\ No newline at end of file

Commit: 002cf76
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:41:30 2026 +1200
Message: added delete route(forgot to commit this earlier)
---
 main.py | 23 +++++++++++++++++++++++
 1 file changed, 23 insertions(+)

diff --git a/main.py b/main.py
index e5507b5..7f47508 100644
--- a/main.py
+++ b/main.py
@@ -155,6 +155,29 @@ def add_locker_duty():
 
     return redirect(url_for("locker_duty"))
 
+@app.route("/delete-locker-duty/<int:duty_id>", methods=["POST"])
+def delete_locker_duty(duty_id):
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    # Only admins can remove people
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute("""
+        DELETE FROM locker_duty
+        WHERE duty_id = ?
+    """, (duty_id,))
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("locker_duty"))
+
 @app.route("/login", methods=["POST"])
 def login():
 

Commit: 94a040a
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:41:05 2026 +1200
Message: fixed delete
---
 templates/locker_duty.html | 54 ++++++++++++++--------------------------------
 1 file changed, 16 insertions(+), 38 deletions(-)

diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index 52b7203..b1db5e9 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -21,10 +21,8 @@ Locker Duty
 </div>
 
 
-
 <!-- ADD PERSON BUTTON -->
 
-
 {% if user.role == "admin" %}
 
 <div class="actions">
@@ -42,10 +40,8 @@ Locker Duty
 {% endif %}
 
 
-
 <!-- WEEK A -->
 
-
 <div class="roster-section">
 
     <h2>Week A</h2>
@@ -94,15 +90,15 @@ Locker Duty
                                 {{ day_duties[0].name }}
                             </span>
 
-
                             {% if user.role == "admin" %}
 
                             <button
+                                type="button"
                                 class="delete-duty-btn"
-                                onclick="openDeleteDutyModal(
-                                    '{{ day_duties[0].duty_id }}',
+                                onclick='openDeleteDutyModal(
+                                    "{{ day_duties[0].duty_id }}",
                                     {{ day_duties[0].name | tojson }}
-                                )">
+                                )'>
 
                                 Delete
 
@@ -135,15 +131,15 @@ Locker Duty
                                 {{ day_duties[1].name }}
                             </span>
 
-
                             {% if user.role == "admin" %}
 
                             <button
+                                type="button"
                                 class="delete-duty-btn"
-                                onclick="openDeleteDutyModal(
-                                    '{{ day_duties[1].duty_id }}',
+                                onclick='openDeleteDutyModal(
+                                    "{{ day_duties[1].duty_id }}",
                                     {{ day_duties[1].name | tojson }}
-                                )">
+                                )'>
 
                                 Delete
 
@@ -176,10 +172,8 @@ Locker Duty
 </div>
 
 
-
 <!-- WEEK B -->
 
-
 <div class="roster-section">
 
     <h2>Week B</h2>
@@ -228,15 +222,15 @@ Locker Duty
                                 {{ day_duties[0].name }}
                             </span>
 
-
                             {% if user.role == "admin" %}
 
                             <button
+                                type="button"
                                 class="delete-duty-btn"
-                                onclick="openDeleteDutyModal(
-                                    '{{ day_duties[0].duty_id }}',
+                                onclick='openDeleteDutyModal(
+                                    "{{ day_duties[0].duty_id }}",
                                     {{ day_duties[0].name | tojson }}
-                                )">
+                                )'>
 
                                 Delete
 
@@ -269,15 +263,15 @@ Locker Duty
                                 {{ day_duties[1].name }}
                             </span>
 
-
                             {% if user.role == "admin" %}
 
                             <button
+                                type="button"
                                 class="delete-duty-btn"
-                                onclick="openDeleteDutyModal(
-                                    '{{ day_duties[1].duty_id }}',
+                                onclick='openDeleteDutyModal(
+                                    "{{ day_duties[1].duty_id }}",
                                     {{ day_duties[1].name | tojson }}
-                                )">
+                                )'>
 
                                 Delete
 
@@ -310,10 +304,8 @@ Locker Duty
 </div>
 
 
-
 <!-- ADD LOCKER DUTY MODAL -->
 
-
 {% if user.role == "admin" %}
 
 <div id="addDutyModal" class="modal">
@@ -322,14 +314,10 @@ Locker Duty
 
         <h2>Add Locker Duty</h2>
 
-
         <form
             action="/add-locker-duty"
             method="POST">
 
-
-            <!-- PERSON -->
-
             <label>
                 Person
             </label>
@@ -353,8 +341,6 @@ Locker Duty
             </select>
 
 
-            <!-- WEEK -->
-
             <label>
                 Week
             </label>
@@ -374,8 +360,6 @@ Locker Duty
             </select>
 
 
-            <!-- DAY -->
-
             <label>
                 Day
             </label>
@@ -407,8 +391,6 @@ Locker Duty
             </select>
 
 
-            <!-- BUTTONS -->
-
             <div class="modal-actions">
 
                 <button
@@ -420,7 +402,6 @@ Locker Duty
 
                 </button>
 
-
                 <button
                     type="submit"
                     class="confirm-btn">
@@ -440,10 +421,8 @@ Locker Duty
 {% endif %}
 
 
-
 <!-- DELETE LOCKER DUTY MODAL -->
 
-
 {% if user.role == "admin" %}
 
 <div id="deleteDutyModal" class="modal">
@@ -493,5 +472,4 @@ Locker Duty
 
 {% endif %}
 
-
 {% endblock %}
\ No newline at end of file

Commit: a4d0869
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:21:51 2026 +1200
Message: added delete
---
 static/css/locker_duty.css | 135 ++++++++++++++++++++++-----
 templates/locker_duty.html | 223 +++++++++++++++++++++++++++++++++++++++++----
 2 files changed, 319 insertions(+), 39 deletions(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 2bd3f5f..23f6482 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -1,7 +1,6 @@
 
 /* LOCKER DUTY PAGE */
 
-
 .topbar {
     margin-bottom: 25px;
 }
@@ -16,17 +15,14 @@
 }
 
 
-
 /* ACTIONS */
 
-
 .actions {
     margin-bottom: 25px;
 }
 
 .button {
     background-color: #003d52;
-
     color: white;
 
     border: none;
@@ -47,25 +43,20 @@
 }
 
 
-
 /* ROSTER SECTION */
 
-
 .roster-section {
     margin-bottom: 35px;
 }
 
 .roster-section h2 {
     margin-bottom: 15px;
-
     color: #003d52;
 }
 
 
-
 /* ROSTER CARD */
 
-
 .roster-card {
     background: white;
 
@@ -79,13 +70,10 @@
 }
 
 
-
 /* ROSTER TABLE */
 
-
 .roster-card table {
     width: 100%;
-
     border-collapse: collapse;
 }
 
@@ -110,10 +98,8 @@
 }
 
 
-
 /* DAY COLUMN */
 
-
 .roster-card .day {
     width: 25%;
 
@@ -123,9 +109,20 @@
 }
 
 
+/* PERSON CELL */
 
-/* UNASSIGNED */
+.person-cell {
+    display: flex;
+
+    align-items: center;
 
+    justify-content: space-between;
+
+    gap: 15px;
+}
+
+
+/* UNASSIGNED */
 
 .unassigned {
     color: #999;
@@ -134,9 +131,32 @@
 }
 
 
+/* DELETE DUTY BUTTON */
 
-/* MODAL */
+.delete-duty-btn {
+    background-color: #dc3545;
 
+    color: white;
+
+    border: none;
+    border-radius: 6px;
+
+    padding: 6px 10px;
+
+    cursor: pointer;
+
+    font-size: 13px;
+    font-weight: 600;
+
+    transition: background-color 0.2s;
+}
+
+.delete-duty-btn:hover {
+    background-color: #b02a37;
+}
+
+
+/* MODALS */
 
 .modal {
     display: none;
@@ -158,10 +178,8 @@
 }
 
 
-
 /* MODAL CONTENT */
 
-
 .modal-content {
     background: white;
 
@@ -173,6 +191,8 @@
     border-radius: 12px;
 
     box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
+
+    box-sizing: border-box;
 }
 
 .modal-content h2 {
@@ -182,10 +202,17 @@
 }
 
 
+/* MODAL TEXT */
 
-/* FORM */
+.modal-content p {
+    color: #555;
+
+    line-height: 1.5;
+}
 
 
+/* FORM */
+
 .modal-content label {
     display: block;
 
@@ -222,10 +249,8 @@
 }
 
 
-
 /* MODAL BUTTONS */
 
-
 .modal-actions {
     display: flex;
 
@@ -236,6 +261,9 @@
     margin-top: 25px;
 }
 
+
+/* CANCEL BUTTON */
+
 .cancel-btn {
     background-color: #e5e7eb;
 
@@ -250,6 +278,8 @@
     cursor: pointer;
 
     font-weight: 600;
+
+    transition: background-color 0.2s;
 }
 
 .cancel-btn:hover {
@@ -257,6 +287,8 @@
 }
 
 
+/* CONFIRM BUTTON */
+
 .confirm-btn {
     background-color: #003d52;
 
@@ -271,8 +303,69 @@
     cursor: pointer;
 
     font-weight: 600;
+
+    transition: background-color 0.2s;
 }
 
 .confirm-btn:hover {
     background-color: #00566f;
+}
+
+
+/* DELETE CONFIRM BUTTON */
+
+.confirm-delete-btn {
+    background-color: #dc3545;
+
+    color: white;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+
+    transition: background-color 0.2s;
+}
+
+.confirm-delete-btn:hover {
+    background-color: #b02a37;
+}
+
+
+/* MOBILE */
+
+@media (max-width: 700px) {
+
+    .roster-card {
+        padding: 15px;
+    }
+
+    .roster-card th,
+    .roster-card td {
+        padding: 12px 10px;
+    }
+
+    .person-cell {
+        flex-direction: column;
+
+        align-items: flex-start;
+
+        gap: 8px;
+    }
+
+    .delete-duty-btn {
+        font-size: 12px;
+
+        padding: 5px 9px;
+    }
+
+    .modal-content {
+        padding: 25px;
+    }
+
 }
\ No newline at end of file
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index c97d821..52b7203 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -20,6 +20,8 @@ Locker Duty
 
 </div>
 
+
+
 <!-- ADD PERSON BUTTON -->
 
 
@@ -40,8 +42,10 @@ Locker Duty
 {% endif %}
 
 
+
 <!-- WEEK A -->
 
+
 <div class="roster-section">
 
     <h2>Week A</h2>
@@ -70,30 +74,93 @@ Locker Duty
                         {{ day }}
                     </td>
 
+
                     {% set day_duties = duties
                         | selectattr("week", "equalto", "A")
                         | selectattr("day", "equalto", day)
                         | list
                     %}
 
+
+                    <!-- PERSON 1 -->
+
                     <td>
+
                         {% if day_duties|length > 0 %}
-                            {{ day_duties[0].name }}
-                        {% else %}
-                            <span class="unassigned">
-                                Unassigned
+
+                        <div class="person-cell">
+
+                            <span>
+                                {{ day_duties[0].name }}
                             </span>
+
+
+                            {% if user.role == "admin" %}
+
+                            <button
+                                class="delete-duty-btn"
+                                onclick="openDeleteDutyModal(
+                                    '{{ day_duties[0].duty_id }}',
+                                    {{ day_duties[0].name | tojson }}
+                                )">
+
+                                Delete
+
+                            </button>
+
+                            {% endif %}
+
+                        </div>
+
+                        {% else %}
+
+                        <span class="unassigned">
+                            Unassigned
+                        </span>
+
                         {% endif %}
+
                     </td>
 
+
+                    <!-- PERSON 2 -->
+
                     <td>
+
                         {% if day_duties|length > 1 %}
-                            {{ day_duties[1].name }}
-                        {% else %}
-                            <span class="unassigned">
-                                Unassigned
+
+                        <div class="person-cell">
+
+                            <span>
+                                {{ day_duties[1].name }}
                             </span>
+
+
+                            {% if user.role == "admin" %}
+
+                            <button
+                                class="delete-duty-btn"
+                                onclick="openDeleteDutyModal(
+                                    '{{ day_duties[1].duty_id }}',
+                                    {{ day_duties[1].name | tojson }}
+                                )">
+
+                                Delete
+
+                            </button>
+
+                            {% endif %}
+
+                        </div>
+
+                        {% else %}
+
+                        <span class="unassigned">
+                            Unassigned
+                        </span>
+
                         {% endif %}
+
                     </td>
 
                 </tr>
@@ -141,30 +208,93 @@ Locker Duty
                         {{ day }}
                     </td>
 
+
                     {% set day_duties = duties
                         | selectattr("week", "equalto", "B")
                         | selectattr("day", "equalto", day)
                         | list
                     %}
 
+
+                    <!-- PERSON 1 -->
+
                     <td>
+
                         {% if day_duties|length > 0 %}
-                            {{ day_duties[0].name }}
-                        {% else %}
-                            <span class="unassigned">
-                                Unassigned
+
+                        <div class="person-cell">
+
+                            <span>
+                                {{ day_duties[0].name }}
                             </span>
+
+
+                            {% if user.role == "admin" %}
+
+                            <button
+                                class="delete-duty-btn"
+                                onclick="openDeleteDutyModal(
+                                    '{{ day_duties[0].duty_id }}',
+                                    {{ day_duties[0].name | tojson }}
+                                )">
+
+                                Delete
+
+                            </button>
+
+                            {% endif %}
+
+                        </div>
+
+                        {% else %}
+
+                        <span class="unassigned">
+                            Unassigned
+                        </span>
+
                         {% endif %}
+
                     </td>
 
+
+                    <!-- PERSON 2 -->
+
                     <td>
+
                         {% if day_duties|length > 1 %}
-                            {{ day_duties[1].name }}
-                        {% else %}
-                            <span class="unassigned">
-                                Unassigned
+
+                        <div class="person-cell">
+
+                            <span>
+                                {{ day_duties[1].name }}
                             </span>
+
+
+                            {% if user.role == "admin" %}
+
+                            <button
+                                class="delete-duty-btn"
+                                onclick="openDeleteDutyModal(
+                                    '{{ day_duties[1].duty_id }}',
+                                    {{ day_duties[1].name | tojson }}
+                                )">
+
+                                Delete
+
+                            </button>
+
+                            {% endif %}
+
+                        </div>
+
+                        {% else %}
+
+                        <span class="unassigned">
+                            Unassigned
+                        </span>
+
                         {% endif %}
+
                     </td>
 
                 </tr>
@@ -180,6 +310,7 @@ Locker Duty
 </div>
 
 
+
 <!-- ADD LOCKER DUTY MODAL -->
 
 
@@ -192,7 +323,9 @@ Locker Duty
         <h2>Add Locker Duty</h2>
 
 
-        <form action="/add-locker-duty" method="POST">
+        <form
+            action="/add-locker-duty"
+            method="POST">
 
 
             <!-- PERSON -->
@@ -287,6 +420,7 @@ Locker Duty
 
                 </button>
 
+
                 <button
                     type="submit"
                     class="confirm-btn">
@@ -297,7 +431,6 @@ Locker Duty
 
             </div>
 
-
         </form>
 
     </div>
@@ -307,4 +440,58 @@ Locker Duty
 {% endif %}
 
 
+
+<!-- DELETE LOCKER DUTY MODAL -->
+
+
+{% if user.role == "admin" %}
+
+<div id="deleteDutyModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Remove Locker Duty</h2>
+
+        <p>
+            Are you sure you want to remove
+            <strong id="deleteDutyName"></strong>
+            from this duty?
+        </p>
+
+
+        <div class="modal-actions">
+
+            <button
+                type="button"
+                class="cancel-btn"
+                onclick="closeDeleteDutyModal()">
+
+                Cancel
+
+            </button>
+
+
+            <form
+                id="deleteDutyForm"
+                method="POST">
+
+                <button
+                    type="submit"
+                    class="confirm-delete-btn">
+
+                    Delete
+
+                </button>
+
+            </form>
+
+        </div>
+
+    </div>
+
+</div>
+
+{% endif %}
+
+
 {% endblock %}
\ No newline at end of file

Commit: 6ea102d
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:13:07 2026 +1200
Message: added confrim button route
---
 main.py                    | 57 ++++++++++++++++++++++++++++++++++++++++++++--
 static/css/locker_duty.css | 44 +++++++++++++++++------------------
 templates/locker_duty.html | 13 ++++-------
 3 files changed, 81 insertions(+), 33 deletions(-)

diff --git a/main.py b/main.py
index 1e86ac1..e5507b5 100644
--- a/main.py
+++ b/main.py
@@ -70,7 +70,7 @@ def locker_duty():
     db = get_db()
     cursor = db.cursor()
 
-    # Get all locker duty assignments
+    # Get locker duty assignments
     cursor.execute("""
         SELECT
             locker_duty.duty_id,
@@ -94,14 +94,67 @@ def locker_duty():
 
     duties = cursor.fetchall()
 
+    # Get active users for the Add Person dropdown
+    cursor.execute("""
+        SELECT user_id, name
+        FROM users
+        WHERE is_active = 1
+        ORDER BY name
+    """)
+
+    users = cursor.fetchall()
+
     db.close()
 
     return render_template(
         "locker_duty.html",
         user=session["user"],
-        duties=duties
+        duties=duties,
+        users=users
     )
 
+@app.route("/add-locker-duty", methods=["POST"])
+def add_locker_duty():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    # Only admins can modify the roster
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    user_id = request.form["user_id"]
+    week = request.form["week"]
+    day = request.form["day"]
+
+    db = get_db()
+    cursor = db.cursor()
+
+    # Check how many people are already assigned
+    cursor.execute("""
+        SELECT COUNT(*)
+        FROM locker_duty
+        WHERE week = ? AND day = ?
+    """, (week, day))
+
+    count = cursor.fetchone()[0]
+
+    # Maximum of 2 people per day
+    if count >= 2:
+        db.close()
+        return "This day already has two people assigned.", 400
+
+    # Add the new duty
+    cursor.execute("""
+        INSERT INTO locker_duty (user_id, week, day)
+        VALUES (?, ?, ?)
+    """, (user_id, week, day))
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("locker_duty"))
+
 @app.route("/login", methods=["POST"])
 def login():
 
diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 4bf51e8..2bd3f5f 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -1,6 +1,6 @@
-/* ============================= */
+
 /* LOCKER DUTY PAGE */
-/* ============================= */
+
 
 .topbar {
     margin-bottom: 25px;
@@ -16,9 +16,9 @@
 }
 
 
-/* ============================= */
+
 /* ACTIONS */
-/* ============================= */
+
 
 .actions {
     margin-bottom: 25px;
@@ -47,9 +47,9 @@
 }
 
 
-/* ============================= */
+
 /* ROSTER SECTION */
-/* ============================= */
+
 
 .roster-section {
     margin-bottom: 35px;
@@ -62,9 +62,9 @@
 }
 
 
-/* ============================= */
+
 /* ROSTER CARD */
-/* ============================= */
+
 
 .roster-card {
     background: white;
@@ -79,9 +79,9 @@
 }
 
 
-/* ============================= */
+
 /* ROSTER TABLE */
-/* ============================= */
+
 
 .roster-card table {
     width: 100%;
@@ -110,9 +110,9 @@
 }
 
 
-/* ============================= */
+
 /* DAY COLUMN */
-/* ============================= */
+
 
 .roster-card .day {
     width: 25%;
@@ -123,9 +123,9 @@
 }
 
 
-/* ============================= */
+
 /* UNASSIGNED */
-/* ============================= */
+
 
 .unassigned {
     color: #999;
@@ -134,9 +134,9 @@
 }
 
 
-/* ============================= */
+
 /* MODAL */
-/* ============================= */
+
 
 .modal {
     display: none;
@@ -158,9 +158,9 @@
 }
 
 
-/* ============================= */
+
 /* MODAL CONTENT */
-/* ============================= */
+
 
 .modal-content {
     background: white;
@@ -182,9 +182,9 @@
 }
 
 
-/* ============================= */
+
 /* FORM */
-/* ============================= */
+
 
 .modal-content label {
     display: block;
@@ -222,9 +222,9 @@
 }
 
 
-/* ============================= */
+
 /* MODAL BUTTONS */
-/* ============================= */
+
 
 .modal-actions {
     display: flex;
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index 072641f..c97d821 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -20,10 +20,8 @@ Locker Duty
 
 </div>
 
-
-<!-- ============================= -->
 <!-- ADD PERSON BUTTON -->
-<!-- ============================= -->
+
 
 {% if user.role == "admin" %}
 
@@ -42,9 +40,7 @@ Locker Duty
 {% endif %}
 
 
-<!-- ============================= -->
 <!-- WEEK A -->
-<!-- ============================= -->
 
 <div class="roster-section">
 
@@ -113,9 +109,9 @@ Locker Duty
 </div>
 
 
-<!-- ============================= -->
+
 <!-- WEEK B -->
-<!-- ============================= -->
+
 
 <div class="roster-section">
 
@@ -184,9 +180,8 @@ Locker Duty
 </div>
 
 
-<!-- ============================= -->
 <!-- ADD LOCKER DUTY MODAL -->
-<!-- ============================= -->
+
 
 {% if user.role == "admin" %}
 

Commit: 2d62502
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:03:50 2026 +1200
Message: added the js for the button
---
 static/script.js | 11 +++++++++++
 1 file changed, 11 insertions(+)

diff --git a/static/script.js b/static/script.js
index 6ce1568..1d8da9f 100644
--- a/static/script.js
+++ b/static/script.js
@@ -190,4 +190,15 @@ if (noticeTextarea) {
 
     });
 
+}
+
+
+// ADD LOCKER DUTY MODAL
+
+function openAddDutyModal() {
+    document.getElementById("addDutyModal").style.display = "flex";
+}
+
+function closeAddDutyModal() {
+    document.getElementById("addDutyModal").style.display = "none";
 }
\ No newline at end of file

Commit: e16f387
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:02:38 2026 +1200
Message: added add person button
---
 static/css/locker_duty.css | 188 +++++++++++++++++++++++++++++++++++++++++++--
 templates/locker_duty.html | 165 ++++++++++++++++++++++++++++++++++++++-
 2 files changed, 341 insertions(+), 12 deletions(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 252de39..4bf51e8 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -3,7 +3,7 @@
 /* ============================= */
 
 .topbar {
-    margin-bottom: 30px;
+    margin-bottom: 25px;
 }
 
 .topbar h1 {
@@ -16,6 +16,37 @@
 }
 
 
+/* ============================= */
+/* ACTIONS */
+/* ============================= */
+
+.actions {
+    margin-bottom: 25px;
+}
+
+.button {
+    background-color: #003d52;
+
+    color: white;
+
+    border: none;
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    font-size: 15px;
+    font-weight: 600;
+
+    cursor: pointer;
+
+    transition: background-color 0.2s;
+}
+
+.button:hover {
+    background-color: #00566f;
+}
+
+
 /* ============================= */
 /* ROSTER SECTION */
 /* ============================= */
@@ -26,6 +57,7 @@
 
 .roster-section h2 {
     margin-bottom: 15px;
+
     color: #003d52;
 }
 
@@ -77,21 +109,17 @@
     color: #333;
 }
 
-.roster-card tr:first-child td {
-    border-top: none;
-}
-
 
 /* ============================= */
-/* DAY */
+/* DAY COLUMN */
 /* ============================= */
 
 .roster-card .day {
+    width: 25%;
+
     font-weight: 600;
 
     color: #003d52;
-
-    width: 25%;
 }
 
 
@@ -103,4 +131,148 @@
     color: #999;
 
     font-style: italic;
+}
+
+
+/* ============================= */
+/* MODAL */
+/* ============================= */
+
+.modal {
+    display: none;
+
+    position: fixed;
+
+    top: 0;
+    left: 0;
+
+    width: 100%;
+    height: 100%;
+
+    background-color: rgba(0, 0, 0, 0.5);
+
+    justify-content: center;
+    align-items: center;
+
+    z-index: 1000;
+}
+
+
+/* ============================= */
+/* MODAL CONTENT */
+/* ============================= */
+
+.modal-content {
+    background: white;
+
+    width: 90%;
+    max-width: 500px;
+
+    padding: 30px;
+
+    border-radius: 12px;
+
+    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
+}
+
+.modal-content h2 {
+    margin-top: 0;
+
+    color: #003d52;
+}
+
+
+/* ============================= */
+/* FORM */
+/* ============================= */
+
+.modal-content label {
+    display: block;
+
+    font-weight: 600;
+
+    margin-top: 15px;
+    margin-bottom: 6px;
+}
+
+.modal-content select {
+    width: 100%;
+
+    padding: 10px 12px;
+
+    border: 1px solid #d1d5db;
+
+    border-radius: 8px;
+
+    font-size: 15px;
+
+    box-sizing: border-box;
+
+    font-family: inherit;
+
+    background-color: white;
+
+    cursor: pointer;
+}
+
+.modal-content select:focus {
+    outline: none;
+
+    border-color: #003d52;
+}
+
+
+/* ============================= */
+/* MODAL BUTTONS */
+/* ============================= */
+
+.modal-actions {
+    display: flex;
+
+    justify-content: flex-end;
+
+    gap: 10px;
+
+    margin-top: 25px;
+}
+
+.cancel-btn {
+    background-color: #e5e7eb;
+
+    color: #333;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+}
+
+.cancel-btn:hover {
+    background-color: #d1d5db;
+}
+
+
+.confirm-btn {
+    background-color: #003d52;
+
+    color: white;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+}
+
+.confirm-btn:hover {
+    background-color: #00566f;
 }
\ No newline at end of file
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index 66cc491..072641f 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -21,6 +21,27 @@ Locker Duty
 </div>
 
 
+<!-- ============================= -->
+<!-- ADD PERSON BUTTON -->
+<!-- ============================= -->
+
+{% if user.role == "admin" %}
+
+<div class="actions">
+
+    <button
+        class="button"
+        onclick="openAddDutyModal()">
+
+        + Add Person
+
+    </button>
+
+</div>
+
+{% endif %}
+
+
 <!-- ============================= -->
 <!-- WEEK A -->
 <!-- ============================= -->
@@ -63,7 +84,9 @@ Locker Duty
                         {% if day_duties|length > 0 %}
                             {{ day_duties[0].name }}
                         {% else %}
-                            <span class="unassigned">Unassigned</span>
+                            <span class="unassigned">
+                                Unassigned
+                            </span>
                         {% endif %}
                     </td>
 
@@ -71,7 +94,9 @@ Locker Duty
                         {% if day_duties|length > 1 %}
                             {{ day_duties[1].name }}
                         {% else %}
-                            <span class="unassigned">Unassigned</span>
+                            <span class="unassigned">
+                                Unassigned
+                            </span>
                         {% endif %}
                     </td>
 
@@ -130,7 +155,9 @@ Locker Duty
                         {% if day_duties|length > 0 %}
                             {{ day_duties[0].name }}
                         {% else %}
-                            <span class="unassigned">Unassigned</span>
+                            <span class="unassigned">
+                                Unassigned
+                            </span>
                         {% endif %}
                     </td>
 
@@ -138,7 +165,9 @@ Locker Duty
                         {% if day_duties|length > 1 %}
                             {{ day_duties[1].name }}
                         {% else %}
-                            <span class="unassigned">Unassigned</span>
+                            <span class="unassigned">
+                                Unassigned
+                            </span>
                         {% endif %}
                     </td>
 
@@ -155,4 +184,132 @@ Locker Duty
 </div>
 
 
+<!-- ============================= -->
+<!-- ADD LOCKER DUTY MODAL -->
+<!-- ============================= -->
+
+{% if user.role == "admin" %}
+
+<div id="addDutyModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Add Locker Duty</h2>
+
+
+        <form action="/add-locker-duty" method="POST">
+
+
+            <!-- PERSON -->
+
+            <label>
+                Person
+            </label>
+
+            <select
+                name="user_id"
+                required>
+
+                <option value="">
+                    Select a person
+                </option>
+
+                {% for member in users %}
+
+                <option value="{{ member.user_id }}">
+                    {{ member.name }}
+                </option>
+
+                {% endfor %}
+
+            </select>
+
+
+            <!-- WEEK -->
+
+            <label>
+                Week
+            </label>
+
+            <select
+                name="week"
+                required>
+
+                <option value="A">
+                    Week A
+                </option>
+
+                <option value="B">
+                    Week B
+                </option>
+
+            </select>
+
+
+            <!-- DAY -->
+
+            <label>
+                Day
+            </label>
+
+            <select
+                name="day"
+                required>
+
+                <option value="Monday">
+                    Monday
+                </option>
+
+                <option value="Tuesday">
+                    Tuesday
+                </option>
+
+                <option value="Wednesday">
+                    Wednesday
+                </option>
+
+                <option value="Thursday">
+                    Thursday
+                </option>
+
+                <option value="Friday">
+                    Friday
+                </option>
+
+            </select>
+
+
+            <!-- BUTTONS -->
+
+            <div class="modal-actions">
+
+                <button
+                    type="button"
+                    class="cancel-btn"
+                    onclick="closeAddDutyModal()">
+
+                    Cancel
+
+                </button>
+
+                <button
+                    type="submit"
+                    class="confirm-btn">
+
+                    Add Person
+
+                </button>
+
+            </div>
+
+
+        </form>
+
+    </div>
+
+</div>
+
+{% endif %}
+
+
 {% endblock %}
\ No newline at end of file

Commit: 5d02610
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 21:00:40 2026 +1200
Message: updated locker duty page
---
 static/css/locker_duty.css | 114 ++++++++++++++++++++----------
 templates/locker_duty.html | 172 +++++++++++++++++++++++++++++----------------
 2 files changed, 190 insertions(+), 96 deletions(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 9cb295e..252de39 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -1,64 +1,106 @@
-h1 {
-    color: #003d52;
-    margin-bottom: 10px;
-    font-size: 2.2rem;
-}
+/* ============================= */
+/* LOCKER DUTY PAGE */
+/* ============================= */
 
-p {
-    color: #555;
+.topbar {
     margin-bottom: 30px;
-    line-height: 1.5;
 }
 
-.container {
-    display: flex;
-    gap: 30px;
+.topbar h1 {
+    margin-bottom: 5px;
 }
 
-.week {
-    flex: 1;
-    background: white;
-    border-radius: 12px;
-    padding: 20px;
+.topbar p {
+    margin-top: 0;
+    color: #666;
+}
+
+
+/* ============================= */
+/* ROSTER SECTION */
+/* ============================= */
+
+.roster-section {
+    margin-bottom: 35px;
+}
 
-    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
+.roster-section h2 {
+    margin-bottom: 15px;
+    color: #003d52;
 }
 
-.week h2 {
-    background-color: #003d52;
-    color: white;
 
-    text-align: center;
+/* ============================= */
+/* ROSTER CARD */
+/* ============================= */
+
+.roster-card {
+    background: white;
+
+    border-radius: 12px;
 
-    padding: 12px;
+    padding: 25px;
 
-    border-radius: 8px;
+    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
 
-    margin-bottom: 20px;
+    overflow-x: auto;
 }
 
-table {
+
+/* ============================= */
+/* ROSTER TABLE */
+/* ============================= */
+
+.roster-card table {
     width: 100%;
+
     border-collapse: collapse;
 }
 
-th {
-    background-color: #f5f5f5;
-    color: #003d52;
-
+.roster-card th {
     text-align: left;
 
-    padding: 12px;
+    padding: 14px 16px;
+
+    background-color: #f5f7f8;
 
-    border-bottom: 2px solid #ddd;
+    color: #003d52;
+
+    font-weight: 600;
 }
 
-td {
-    padding: 12px;
-    border-bottom: 1px solid #eee;
+.roster-card td {
+    padding: 16px;
+
+    border-top: 1px solid #eee;
+
     color: #333;
 }
 
-tr:hover td {
-    background-color: #f7f7f7;
+.roster-card tr:first-child td {
+    border-top: none;
+}
+
+
+/* ============================= */
+/* DAY */
+/* ============================= */
+
+.roster-card .day {
+    font-weight: 600;
+
+    color: #003d52;
+
+    width: 25%;
+}
+
+
+/* ============================= */
+/* UNASSIGNED */
+/* ============================= */
+
+.unassigned {
+    color: #999;
+
+    font-style: italic;
 }
\ No newline at end of file
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index ac53123..66cc491 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -10,92 +10,143 @@ Locker Duty
 
 {% block content %}
 
-<h1>Locker Duty Roster</h1>
+<div class="topbar">
 
-<p>
-    Lock the side doors on arrival - there will be staff on duty to assist.<br>
-    Monitor student behaviour.
-</p>
+    <h1>Locker Duty</h1>
 
-<div class="container">
+    <p>
+        Manage the prefect locker duty roster.
+    </p>
 
-    <!-- WEEK A -->
-    <div class="week">
+</div>
+
+
+<!-- ============================= -->
+<!-- WEEK A -->
+<!-- ============================= -->
+
+<div class="roster-section">
 
-        <h2>WEEK A</h2>
+    <h2>Week A</h2>
+
+    <div class="roster-card">
 
         <table>
 
-            <tr>
-                <th>Day</th>
-                <th>Students</th>
-            </tr>
+            <thead>
+
+                <tr>
+                    <th>Day</th>
+                    <th>Person 1</th>
+                    <th>Person 2</th>
+                </tr>
+
+            </thead>
 
-            <tr>
-                <td>Monday</td>
-                <td>Elizabeth, Rosie</td>
-            </tr>
+            <tbody>
 
-            <tr>
-                <td>Tuesday</td>
-                <td>Barnaby, Samuel</td>
-            </tr>
+                {% for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] %}
 
-            <tr>
-                <td>Wednesday</td>
-                <td>Ava, Dasha</td>
-            </tr>
+                <tr>
 
-            <tr>
-                <td>Thursday</td>
-                <td>Sione, Michaela</td>
-            </tr>
+                    <td class="day">
+                        {{ day }}
+                    </td>
 
-            <tr>
-                <td>Friday</td>
-                <td>James, Luke</td>
-            </tr>
+                    {% set day_duties = duties
+                        | selectattr("week", "equalto", "A")
+                        | selectattr("day", "equalto", day)
+                        | list
+                    %}
+
+                    <td>
+                        {% if day_duties|length > 0 %}
+                            {{ day_duties[0].name }}
+                        {% else %}
+                            <span class="unassigned">Unassigned</span>
+                        {% endif %}
+                    </td>
+
+                    <td>
+                        {% if day_duties|length > 1 %}
+                            {{ day_duties[1].name }}
+                        {% else %}
+                            <span class="unassigned">Unassigned</span>
+                        {% endif %}
+                    </td>
+
+                </tr>
+
+                {% endfor %}
+
+            </tbody>
 
         </table>
 
     </div>
 
-    <!-- WEEK B -->
-    <div class="week">
+</div>
 
-        <h2>WEEK B</h2>
+
+<!-- ============================= -->
+<!-- WEEK B -->
+<!-- ============================= -->
+
+<div class="roster-section">
+
+    <h2>Week B</h2>
+
+    <div class="roster-card">
 
         <table>
 
-            <tr>
-                <th>Day</th>
-                <th>Students</th>
-            </tr>
+            <thead>
+
+                <tr>
+                    <th>Day</th>
+                    <th>Person 1</th>
+                    <th>Person 2</th>
+                </tr>
+
+            </thead>
 
-            <tr>
-                <td>Monday</td>
-                <td>Zoe, Chloe</td>
-            </tr>
+            <tbody>
 
-            <tr>
-                <td>Tuesday</td>
-                <td>Kanon, Ida</td>
-            </tr>
+                {% for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] %}
 
-            <tr>
-                <td>Wednesday</td>
-                <td>Lukas, Messi</td>
-            </tr>
+                <tr>
 
-            <tr>
-                <td>Thursday</td>
-                <td>Sho, Aaron</td>
-            </tr>
+                    <td class="day">
+                        {{ day }}
+                    </td>
 
-            <tr>
-                <td>Friday</td>
-                <td>Eason, Nilana</td>
-            </tr>
+                    {% set day_duties = duties
+                        | selectattr("week", "equalto", "B")
+                        | selectattr("day", "equalto", day)
+                        | list
+                    %}
+
+                    <td>
+                        {% if day_duties|length > 0 %}
+                            {{ day_duties[0].name }}
+                        {% else %}
+                            <span class="unassigned">Unassigned</span>
+                        {% endif %}
+                    </td>
+
+                    <td>
+                        {% if day_duties|length > 1 %}
+                            {{ day_duties[1].name }}
+                        {% else %}
+                            <span class="unassigned">Unassigned</span>
+                        {% endif %}
+                    </td>
+
+                </tr>
+
+                {% endfor %}
+
+            </tbody>
 
         </table>
 
@@ -103,4 +154,5 @@ Locker Duty
 
 </div>
 
+
 {% endblock %}
\ No newline at end of file

Commit: a3fcd48
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 20:58:43 2026 +1200
Message: updated locker duty route
---
 main.py | 35 ++++++++++++++++++++++++++++++++++-
 1 file changed, 34 insertions(+), 1 deletion(-)

diff --git a/main.py b/main.py
index c89d5c6..1e86ac1 100644
--- a/main.py
+++ b/main.py
@@ -67,7 +67,40 @@ def locker_duty():
     if "user" not in session:
         return redirect(url_for("index"))
 
-    return render_template("locker_duty.html", user=session["user"])
+    db = get_db()
+    cursor = db.cursor()
+
+    # Get all locker duty assignments
+    cursor.execute("""
+        SELECT
+            locker_duty.duty_id,
+            locker_duty.user_id,
+            locker_duty.week,
+            locker_duty.day,
+            users.name
+        FROM locker_duty
+        JOIN users
+            ON locker_duty.user_id = users.user_id
+        ORDER BY
+            locker_duty.week,
+            CASE locker_duty.day
+                WHEN 'Monday' THEN 1
+                WHEN 'Tuesday' THEN 2
+                WHEN 'Wednesday' THEN 3
+                WHEN 'Thursday' THEN 4
+                WHEN 'Friday' THEN 5
+            END
+    """)
+
+    duties = cursor.fetchall()
+
+    db.close()
+
+    return render_template(
+        "locker_duty.html",
+        user=session["user"],
+        duties=duties
+    )
 
 @app.route("/login", methods=["POST"])
 def login():

Commit: d0756c3
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 20:55:16 2026 +1200
Message: genuinly js removed 1 space
---
 static/css/index.css | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/static/css/index.css b/static/css/index.css
index e1c69cb..540d750 100644
--- a/static/css/index.css
+++ b/static/css/index.css
@@ -95,4 +95,4 @@ body {
 
     text-decoration: none;
     font-weight: bold;
-}. 
\ No newline at end of file
+}.
\ No newline at end of file

Commit: 238aeb4
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 20:54:58 2026 +1200
Message: added new table
---
 db.py | 28 +++++++++++++++++-----------
 1 file changed, 17 insertions(+), 11 deletions(-)

diff --git a/db.py b/db.py
index ba2073d..7541f6e 100644
--- a/db.py
+++ b/db.py
@@ -3,7 +3,11 @@ import sqlite3
 connection = sqlite3.connect("prefectconnect.db")
 cursor = connection.cursor()
 
+
+# ==============================
 # USERS TABLE
+# ==============================
+
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS users (
     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
@@ -14,28 +18,26 @@ CREATE TABLE IF NOT EXISTS users (
 )
 """)
 
+
+# ==============================
 # LOCKER DUTY TABLE
+# ==============================
+
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS locker_duty (
     duty_id INTEGER PRIMARY KEY AUTOINCREMENT,
     user_id INTEGER NOT NULL,
-    duty_date DATE NOT NULL,
+    week TEXT NOT NULL,
+    day TEXT NOT NULL,
     FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
 )
 """)
 
-# MESSAGE POST TABLE
-cursor.execute("""
-CREATE TABLE IF NOT EXISTS message_post (
-    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
-    user_id INTEGER NOT NULL,
-    content TEXT NOT NULL,
-    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
-    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
-)
-""")
 
+# ==============================
 # NOTICE TABLE
+# ==============================
+
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS notice (
     notice_id INTEGER PRIMARY KEY AUTOINCREMENT,
@@ -48,7 +50,11 @@ CREATE TABLE IF NOT EXISTS notice (
 )
 """)
 
+
+# ==============================
 # NOTICE READ TABLE
+# ==============================
+
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS notice_read (
     read_id INTEGER PRIMARY KEY AUTOINCREMENT,

Commit: 50bc287
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 19 20:28:55 2026 +1200
Message: removed useless tables
---
 db.py                   | 33 ---------------------------------
 templates/assembly.html |  4 ++--
 2 files changed, 2 insertions(+), 35 deletions(-)

diff --git a/db.py b/db.py
index 6ca5c52..ba2073d 100644
--- a/db.py
+++ b/db.py
@@ -61,39 +61,6 @@ CREATE TABLE IF NOT EXISTS notice_read (
 )
 """)
 
-# ASSEMBLY TABLE
-cursor.execute("""
-CREATE TABLE IF NOT EXISTS assembly (
-    assembly_id INTEGER PRIMARY KEY AUTOINCREMENT,
-    title TEXT NOT NULL,
-    date DATE NOT NULL
-)
-""")
-
-
-# ASSEMBLY IDEA TABLE
-cursor.execute("""
-CREATE TABLE IF NOT EXISTS assembly_idea (
-    idea_id INTEGER PRIMARY KEY AUTOINCREMENT,
-    assembly_id INTEGER NOT NULL,
-    content TEXT NOT NULL,
-    updated_by INTEGER NOT NULL,
-    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE,
-    FOREIGN KEY (updated_by) REFERENCES users(user_id) ON DELETE CASCADE
-)
-""")
-
-# RUN SHEET TABLE
-cursor.execute("""
-               
-CREATE TABLE IF NOT EXISTS run_sheet (
-    runsheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
-    assembly_id INTEGER NOT NULL,
-    content TEXT NOT NULL,
-    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
-    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE
-)
-""")
 
 connection.commit()
 connection.close()
diff --git a/templates/assembly.html b/templates/assembly.html
index 9919d77..8f72db5 100644
--- a/templates/assembly.html
+++ b/templates/assembly.html
@@ -13,11 +13,11 @@ Assemblies
 <div class="topbar">
 
     <h1>Assemblies</h1>
-
+    
     <p>
         View assembly information and responsibilities.
     </p>
-
+    
 </div>
 
 

Commit: 9854ed2
Author: BHS23113 <23113@burnside.school.nz>
Date: Tue Aug 18 09:23:43 2026 +1200
Message: fixed add user button mouse pointer
---
 static/css/users.css | 1 +
 1 file changed, 1 insertion(+)

diff --git a/static/css/users.css b/static/css/users.css
index 03829a5..1420828 100644
--- a/static/css/users.css
+++ b/static/css/users.css
@@ -27,6 +27,7 @@
     border-radius: 8px;
     font-weight: bold;
     transition: 0.2s;
+    cursor: pointer;
 }
 
 .button:hover {

Commit: dd855a3
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 10:01:36 2026 +1200
Message: added new notice check
---
 db.py   | 15 +++++++++++++++
 main.py | 27 +++++++++++++++++++++++++--
 2 files changed, 40 insertions(+), 2 deletions(-)

diff --git a/db.py b/db.py
index f5cadbc..6ca5c52 100644
--- a/db.py
+++ b/db.py
@@ -48,6 +48,19 @@ CREATE TABLE IF NOT EXISTS notice (
 )
 """)
 
+# NOTICE READ TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS notice_read (
+    read_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    notice_id INTEGER NOT NULL,
+    user_id INTEGER NOT NULL,
+    read_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
+    UNIQUE(notice_id, user_id),
+    FOREIGN KEY (notice_id) REFERENCES notice(notice_id) ON DELETE CASCADE,
+    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
+)
+""")
+
 # ASSEMBLY TABLE
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS assembly (
@@ -57,6 +70,7 @@ CREATE TABLE IF NOT EXISTS assembly (
 )
 """)
 
+
 # ASSEMBLY IDEA TABLE
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS assembly_idea (
@@ -71,6 +85,7 @@ CREATE TABLE IF NOT EXISTS assembly_idea (
 
 # RUN SHEET TABLE
 cursor.execute("""
+               
 CREATE TABLE IF NOT EXISTS run_sheet (
     runsheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
     assembly_id INTEGER NOT NULL,
diff --git a/main.py b/main.py
index cdeed46..c89d5c6 100644
--- a/main.py
+++ b/main.py
@@ -37,11 +37,19 @@ def dashboard():
     db = get_db()
     cursor = db.cursor()
 
+    user_id = session["user"]["user_id"]
+
+    # Count active notices this user has NOT read
     cursor.execute("""
         SELECT COUNT(*)
         FROM notice
-        WHERE is_active = 1
-    """)
+        WHERE notice.is_active = 1
+        AND notice.notice_id NOT IN (
+            SELECT notice_id
+            FROM notice_read
+            WHERE user_id = ?
+        )
+    """, (user_id,))
 
     notice_count = cursor.fetchone()[0]
 
@@ -139,6 +147,7 @@ def notices():
     db = get_db()
     cursor = db.cursor()
 
+    # Get all active notices
     cursor.execute("""
         SELECT
             notice.notice_id,
@@ -155,6 +164,19 @@ def notices():
 
     notices = cursor.fetchall()
 
+    # Get the current user's ID
+    user_id = session["user"]["user_id"]
+
+    # Mark all active notices as read for this user
+    for notice in notices:
+
+        cursor.execute("""
+            INSERT OR IGNORE INTO notice_read
+            (notice_id, user_id)
+            VALUES (?, ?)
+        """, (notice["notice_id"], user_id))
+
+    db.commit()
     db.close()
 
     return render_template(
@@ -162,6 +184,7 @@ def notices():
         user=session["user"],
         notices=notices
     )
+
 @app.route("/add-notice", methods=["POST"])
 def add_notice():
 

Commit: dde8cb4
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 01:02:21 2026 +1200
Message: removed chat on dashboard
---
 templates/dashboard.html | 5 +----
 1 file changed, 1 insertion(+), 4 deletions(-)

diff --git a/templates/dashboard.html b/templates/dashboard.html
index 99c402f..85d6f9a 100644
--- a/templates/dashboard.html
+++ b/templates/dashboard.html
@@ -27,10 +27,7 @@ Dashboard
         <p>{{ notice_count }} new announcements</p>
     </div>
 
-    <div class="card">
-        <h3>Chat</h3>
-        <p>Open discussions</p>
-    </div>
+
 
 </div>
 

Commit: 4fa8ebd
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:54:20 2026 +1200
Message: removed hardcode from dashboard
---
 main.py                  | 16 +++++++++++++++-
 templates/dashboard.html |  2 +-
 2 files changed, 16 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 984a790..cdeed46 100644
--- a/main.py
+++ b/main.py
@@ -34,9 +34,23 @@ def dashboard():
     if "user" not in session:
         return redirect(url_for("index"))
 
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute("""
+        SELECT COUNT(*)
+        FROM notice
+        WHERE is_active = 1
+    """)
+
+    notice_count = cursor.fetchone()[0]
+
+    db.close()
+
     return render_template(
         "dashboard.html",
-        user=session["user"]
+        user=session["user"],
+        notice_count=notice_count
     )
 
 @app.route("/locker-duty")
diff --git a/templates/dashboard.html b/templates/dashboard.html
index 7d9956d..99c402f 100644
--- a/templates/dashboard.html
+++ b/templates/dashboard.html
@@ -24,7 +24,7 @@ Dashboard
 
     <div class="card">
         <h3>Notices</h3>
-        <p>3 new announcements</p>
+        <p>{{ notice_count }} new announcements</p>
     </div>
 
     <div class="card">

Commit: ecf3f83
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:41:52 2026 +1200
Message: added special character error protection
---
 templates/notices.html | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)

diff --git a/templates/notices.html b/templates/notices.html
index a8e89f1..c693b1d 100644
--- a/templates/notices.html
+++ b/templates/notices.html
@@ -56,10 +56,10 @@ Notices
 
                 <button
                     class="delete-notice-btn"
-                    onclick="openDeleteNoticeModal(
-                        '{{ notice.notice_id }}',
-                        '{{ notice.title }}'
-                    )">
+                    onclick='openDeleteNoticeModal(
+                        "{{ notice.notice_id }}",
+                        {{ notice.title | tojson }}
+                    )'>
 
                     Delete
 
@@ -176,7 +176,7 @@ Notices
 {% endif %}
 
 
-<!-- DELETE NOTICE MODAL  -->
+<!-- DELETE NOTICE MODAL -->
 
 {% if user.role == "admin" %}
 

Commit: cc3200d
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:31:43 2026 +1200
Message: added max lines
---
 main.py          |  3 +++
 static/script.js | 24 ++++++++++++++++++++++++
 2 files changed, 27 insertions(+)

diff --git a/main.py b/main.py
index 7adcd2d..984a790 100644
--- a/main.py
+++ b/main.py
@@ -162,6 +162,9 @@ def add_notice():
 
     if len(title) > 50 or len(content) > 500:
         return redirect(url_for("notices"))
+    
+    if content.count("\n") >= 8:
+        return redirect(url_for("notices"))
 
     user_id = session["user"]["user_id"]
 
diff --git a/static/script.js b/static/script.js
index f73730e..6ce1568 100644
--- a/static/script.js
+++ b/static/script.js
@@ -166,4 +166,28 @@ function closeDeleteNoticeModal() {
 
     document.getElementById("deleteNoticeModal").style.display = "none";
 
+}
+
+//  NOTICE LINE LIMIT 
+
+const noticeTextarea = document.querySelector(
+    '#addNoticeModal textarea[name="content"]'
+);
+
+if (noticeTextarea) {
+
+    noticeTextarea.addEventListener("input", function () {
+
+        const maxLines = 8;
+
+        const lines = this.value.split("\n");
+
+        if (lines.length > maxLines) {
+
+            this.value = lines.slice(0, maxLines).join("\n");
+
+        }
+
+    });
+
 }
\ No newline at end of file

Commit: c3b1e7c
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:24:16 2026 +1200
Message: lowered max characters
---
 main.py                | 2 +-
 templates/notices.html | 4 ++--
 2 files changed, 3 insertions(+), 3 deletions(-)

diff --git a/main.py b/main.py
index 331dadd..7adcd2d 100644
--- a/main.py
+++ b/main.py
@@ -160,7 +160,7 @@ def add_notice():
     title = request.form["title"].strip()
     content = request.form["content"].strip()
 
-    if len(title) > 100 or len(content) > 750:
+    if len(title) > 50 or len(content) > 500:
         return redirect(url_for("notices"))
 
     user_id = session["user"]["user_id"]
diff --git a/templates/notices.html b/templates/notices.html
index 4be1e09..a8e89f1 100644
--- a/templates/notices.html
+++ b/templates/notices.html
@@ -130,7 +130,7 @@ Notices
                 type="text"
                 name="title"
                 placeholder="Notice title"
-                maxlength="100"
+                maxlength="50"
                 required>
 
 
@@ -142,7 +142,7 @@ Notices
                 name="content"
                 placeholder="Write your notice..."
                 rows="6"
-                maxlength="750"
+                maxlength="500"
                 required></textarea>
 
 

Commit: 4e2640d
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:19:52 2026 +1200
Message: fixed wrap
---
 static/css/notices.css | 12 ++++++++++++
 templates/notices.html |  4 +---
 2 files changed, 13 insertions(+), 3 deletions(-)

diff --git a/static/css/notices.css b/static/css/notices.css
index 15e0705..a44de04 100644
--- a/static/css/notices.css
+++ b/static/css/notices.css
@@ -69,6 +69,9 @@
     padding: 25px;
 
     box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
+
+    /* Prevent long content from breaking the page */
+    overflow: hidden;
 }
 
 
@@ -89,6 +92,8 @@
     margin: 0;
 
     color: #003d52;
+
+    overflow-wrap: anywhere;
 }
 
 
@@ -102,12 +107,19 @@
 
 .notice-content p {
     margin: 0;
+    padding: 0;
 
     line-height: 1.6;
 
     color: #333;
 
+    /* Preserve intentional line breaks */
     white-space: pre-wrap;
+
+    /* Break extremely long strings */
+    overflow-wrap: anywhere;
+
+    word-break: normal;
 }
 
 
diff --git a/templates/notices.html b/templates/notices.html
index d9b0592..4be1e09 100644
--- a/templates/notices.html
+++ b/templates/notices.html
@@ -72,9 +72,7 @@ Notices
 
             <div class="notice-content">
 
-                <p>
-                    {{ notice.content }}
-                </p>
+                <p>{{ notice.content }}</p>
 
             </div>
 

Commit: e524567
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Aug 17 00:05:03 2026 +1200
Message: shortened word limit
---
 main.py                | 2 +-
 templates/notices.html | 4 ++--
 2 files changed, 3 insertions(+), 3 deletions(-)

diff --git a/main.py b/main.py
index fd67cb4..331dadd 100644
--- a/main.py
+++ b/main.py
@@ -160,7 +160,7 @@ def add_notice():
     title = request.form["title"].strip()
     content = request.form["content"].strip()
 
-    if len(title) > 100 or len(content) > 2000:
+    if len(title) > 100 or len(content) > 750:
         return redirect(url_for("notices"))
 
     user_id = session["user"]["user_id"]
diff --git a/templates/notices.html b/templates/notices.html
index b6f2c84..d9b0592 100644
--- a/templates/notices.html
+++ b/templates/notices.html
@@ -144,7 +144,7 @@ Notices
                 name="content"
                 placeholder="Write your notice..."
                 rows="6"
-                maxlength="2000"
+                maxlength="750"
                 required></textarea>
 
 
@@ -178,7 +178,7 @@ Notices
 {% endif %}
 
 
-<!-- ================= DELETE NOTICE MODAL ================= -->
+<!-- DELETE NOTICE MODAL  -->
 
 {% if user.role == "admin" %}
 

Commit: 8a02a09
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Aug 16 23:56:55 2026 +1200
Message: added word limit
---
 main.py                | 7 +++++--
 templates/notices.html | 4 +++-
 2 files changed, 8 insertions(+), 3 deletions(-)

diff --git a/main.py b/main.py
index 0729c68..fd67cb4 100644
--- a/main.py
+++ b/main.py
@@ -157,8 +157,11 @@ def add_notice():
     if session["user"]["role"] != "admin":
         return render_template("403.html"), 403
 
-    title = request.form["title"]
-    content = request.form["content"]
+    title = request.form["title"].strip()
+    content = request.form["content"].strip()
+
+    if len(title) > 100 or len(content) > 2000:
+        return redirect(url_for("notices"))
 
     user_id = session["user"]["user_id"]
 
diff --git a/templates/notices.html b/templates/notices.html
index 17c7761..b6f2c84 100644
--- a/templates/notices.html
+++ b/templates/notices.html
@@ -112,7 +112,7 @@ Notices
 </div>
 
 
-<!-- ================= ADD NOTICE MODAL ================= -->
+<!-- ADD NOTICE MODAL  -->
 
 {% if user.role == "admin" %}
 
@@ -132,6 +132,7 @@ Notices
                 type="text"
                 name="title"
                 placeholder="Notice title"
+                maxlength="100"
                 required>
 
 
@@ -143,6 +144,7 @@ Notices
                 name="content"
                 placeholder="Write your notice..."
                 rows="6"
+                maxlength="2000"
                 required></textarea>
 
 

Commit: e661220
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 17:45:41 2026 +1200
Message: added delete post
---
 main.py          | 26 ++++++++++++++++++++++++++
 static/script.js | 20 ++++++++++++++++++++
 2 files changed, 46 insertions(+)

diff --git a/main.py b/main.py
index 7be7d05..0729c68 100644
--- a/main.py
+++ b/main.py
@@ -177,6 +177,32 @@ def add_notice():
     db.close()
 
     return redirect(url_for("notices"))
+
+@app.route("/delete-notice/<int:notice_id>", methods=["POST"])
+def delete_notice(notice_id):
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute(
+        """
+        UPDATE notice
+        SET is_active = 0
+        WHERE notice_id = ?
+        """,
+        (notice_id,)
+    )
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("notices"))
     
 @app.route("/users")
 def users():
diff --git a/static/script.js b/static/script.js
index d4b9e52..f73730e 100644
--- a/static/script.js
+++ b/static/script.js
@@ -146,4 +146,24 @@ function closeAddNoticeModal() {
 
     document.getElementById("addNoticeModal").style.display = "none";
 
+}
+
+// DELETE NOTICE
+
+function openDeleteNoticeModal(id, title) {
+
+    document.getElementById("deleteNoticeModal").style.display = "flex";
+
+    document.getElementById("deleteNoticeTitle").textContent = title;
+
+    document.getElementById("deleteNoticeForm").action =
+        "/delete-notice/" + id;
+
+}
+
+
+function closeDeleteNoticeModal() {
+
+    document.getElementById("deleteNoticeModal").style.display = "none";
+
 }
\ No newline at end of file

Commit: 1601319
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 17:31:05 2026 +1200
Message: added notices + add notice button
---
 main.py                |  62 +++++++++
 static/css/notices.css | 348 +++++++++++++++++++++++++++++++++++++++++++++++++
 static/script.js       |  16 ++-
 templates/layout.html  |   2 +-
 templates/notices.html | 229 ++++++++++++++++++++++++++++++++
 5 files changed, 655 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 2ff2ec5..7be7d05 100644
--- a/main.py
+++ b/main.py
@@ -115,6 +115,68 @@ def assemblies():
         "assembly.html",
         user=session["user"]
     )
+
+@app.route("/notices")
+def notices():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute("""
+        SELECT
+            notice.notice_id,
+            notice.title,
+            notice.content,
+            notice.created_at,
+            users.name AS author
+        FROM notice
+        JOIN users
+            ON notice.created_by = users.user_id
+        WHERE notice.is_active = 1
+        ORDER BY notice.created_at DESC
+    """)
+
+    notices = cursor.fetchall()
+
+    db.close()
+
+    return render_template(
+        "notices.html",
+        user=session["user"],
+        notices=notices
+    )
+@app.route("/add-notice", methods=["POST"])
+def add_notice():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    title = request.form["title"]
+    content = request.form["content"]
+
+    user_id = session["user"]["user_id"]
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute(
+        """
+        INSERT INTO notice (title, content, created_by)
+        VALUES (?, ?, ?)
+        """,
+        (title, content, user_id)
+    )
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("notices"))
     
 @app.route("/users")
 def users():
diff --git a/static/css/notices.css b/static/css/notices.css
new file mode 100644
index 0000000..15e0705
--- /dev/null
+++ b/static/css/notices.css
@@ -0,0 +1,348 @@
+/* ============================= */
+/* NOTICES PAGE */
+/* ============================= */
+
+.topbar {
+    margin-bottom: 25px;
+}
+
+.topbar h1 {
+    margin-bottom: 5px;
+}
+
+.topbar p {
+    margin-top: 0;
+    color: #666;
+}
+
+
+/* ============================= */
+/* ACTIONS */
+/* ============================= */
+
+.actions {
+    margin-bottom: 25px;
+}
+
+.button {
+    background-color: #003d52;
+    color: white;
+
+    border: none;
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    font-size: 15px;
+    font-weight: 600;
+
+    cursor: pointer;
+
+    transition: background-color 0.2s;
+}
+
+.button:hover {
+    background-color: #00566f;
+}
+
+
+/* ============================= */
+/* NOTICE CONTAINER */
+/* ============================= */
+
+.notices-container {
+    display: flex;
+    flex-direction: column;
+    gap: 20px;
+}
+
+
+/* ============================= */
+/* NOTICE CARD */
+/* ============================= */
+
+.notice-card {
+    background: white;
+
+    border-radius: 12px;
+
+    padding: 25px;
+
+    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
+}
+
+
+/* ============================= */
+/* NOTICE HEADER */
+/* ============================= */
+
+.notice-header {
+    display: flex;
+
+    justify-content: space-between;
+    align-items: center;
+
+    margin-bottom: 15px;
+}
+
+.notice-header h2 {
+    margin: 0;
+
+    color: #003d52;
+}
+
+
+/* ============================= */
+/* NOTICE CONTENT */
+/* ============================= */
+
+.notice-content {
+    margin-bottom: 20px;
+}
+
+.notice-content p {
+    margin: 0;
+
+    line-height: 1.6;
+
+    color: #333;
+
+    white-space: pre-wrap;
+}
+
+
+/* ============================= */
+/* NOTICE FOOTER */
+/* ============================= */
+
+.notice-footer {
+    display: flex;
+
+    justify-content: space-between;
+
+    padding-top: 15px;
+
+    border-top: 1px solid #eee;
+
+    color: #777;
+
+    font-size: 13px;
+}
+
+
+/* ============================= */
+/* DELETE NOTICE BUTTON */
+/* ============================= */
+
+.delete-notice-btn {
+    background-color: #dc3545;
+
+    color: white;
+
+    border: none;
+    border-radius: 6px;
+
+    padding: 8px 14px;
+
+    cursor: pointer;
+
+    font-size: 14px;
+}
+
+.delete-notice-btn:hover {
+    background-color: #b02a37;
+}
+
+
+/* ============================= */
+/* NO NOTICES */
+/* ============================= */
+
+.no-notices {
+    background: white;
+
+    border-radius: 12px;
+
+    padding: 40px;
+
+    text-align: center;
+
+    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
+}
+
+.no-notices h2 {
+    margin-bottom: 8px;
+
+    color: #003d52;
+}
+
+.no-notices p {
+    margin: 0;
+
+    color: #777;
+}
+
+
+/* ============================= */
+/* MODALS */
+/* ============================= */
+
+.modal {
+    display: none;
+
+    position: fixed;
+
+    top: 0;
+    left: 0;
+
+    width: 100%;
+    height: 100%;
+
+    background-color: rgba(0, 0, 0, 0.5);
+
+    justify-content: center;
+    align-items: center;
+
+    z-index: 1000;
+}
+
+
+.modal-content {
+    background: white;
+
+    width: 90%;
+    max-width: 500px;
+
+    padding: 30px;
+
+    border-radius: 12px;
+
+    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
+}
+
+.modal-content h2 {
+    margin-top: 0;
+
+    color: #003d52;
+}
+
+
+/* ============================= */
+/* FORM */
+/* ============================= */
+
+.modal-content label {
+    display: block;
+
+    font-weight: 600;
+
+    margin-top: 15px;
+    margin-bottom: 6px;
+}
+
+.modal-content input,
+.modal-content textarea {
+    width: 100%;
+
+    padding: 10px 12px;
+
+    border: 1px solid #d1d5db;
+
+    border-radius: 8px;
+
+    font-size: 15px;
+
+    box-sizing: border-box;
+
+    font-family: inherit;
+}
+
+.modal-content textarea {
+    resize: vertical;
+
+    min-height: 120px;
+}
+
+.modal-content input:focus,
+.modal-content textarea:focus {
+    outline: none;
+
+    border-color: #003d52;
+}
+
+
+/* ============================= */
+/* MODAL BUTTONS */
+/* ============================= */
+
+.modal-actions {
+    display: flex;
+
+    justify-content: flex-end;
+
+    gap: 10px;
+
+    margin-top: 25px;
+}
+
+.cancel-btn {
+    background-color: #e5e7eb;
+
+    color: #333;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+}
+
+.cancel-btn:hover {
+    background-color: #d1d5db;
+}
+
+
+.confirm-btn {
+    background-color: #003d52;
+
+    color: white;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+}
+
+.confirm-btn:hover {
+    background-color: #00566f;
+}
+
+
+.confirm-delete-btn {
+    background-color: #dc3545;
+
+    color: white;
+
+    border: none;
+
+    border-radius: 8px;
+
+    padding: 10px 18px;
+
+    cursor: pointer;
+
+    font-weight: 600;
+}
+
+.confirm-delete-btn:hover {
+    background-color: #b02a37;
+}
\ No newline at end of file
diff --git a/static/script.js b/static/script.js
index 2d2d991..d4b9e52 100644
--- a/static/script.js
+++ b/static/script.js
@@ -132,4 +132,18 @@ window.addEventListener("click", function(event) {
 
     }
 
-});
\ No newline at end of file
+});
+
+// ADD NOTICE
+
+function openAddNoticeModal() {
+
+    document.getElementById("addNoticeModal").style.display = "flex";
+
+}
+
+function closeAddNoticeModal() {
+
+    document.getElementById("addNoticeModal").style.display = "none";
+
+}
\ No newline at end of file
diff --git a/templates/layout.html b/templates/layout.html
index 51823a3..2d46379 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -30,7 +30,7 @@
 
             <a href="/dashboard">Dashboard</a>
             <a href="/locker-duty">Locker Duty</a>
-            <a href="#">Notices</a>
+            <a href="/notices">Notices</a>
             <a href="/assemblies">Assemblies</a>
 
             <!-- Only visible to admins -->
diff --git a/templates/notices.html b/templates/notices.html
new file mode 100644
index 0000000..17c7761
--- /dev/null
+++ b/templates/notices.html
@@ -0,0 +1,229 @@
+{% extends "layout.html" %}
+
+{% block title %}
+Notices
+{% endblock %}
+
+{% block css %}
+<link rel="stylesheet" href="{{ url_for('static', filename='css/notices.css') }}">
+{% endblock %}
+
+{% block content %}
+
+<div class="topbar">
+
+    <h1>Notices</h1>
+
+    <p>
+        Important announcements and information for prefects.
+    </p>
+
+</div>
+
+
+{% if user.role == "admin" %}
+
+<div class="actions">
+
+    <button
+        class="button"
+        onclick="openAddNoticeModal()">
+
+        + Add Notice
+
+    </button>
+
+</div>
+
+{% endif %}
+
+
+<div class="notices-container">
+
+    {% if notices %}
+
+        {% for notice in notices %}
+
+        <div class="notice-card">
+
+            <div class="notice-header">
+
+                <h2>
+                    {{ notice.title }}
+                </h2>
+
+                {% if user.role == "admin" %}
+
+                <button
+                    class="delete-notice-btn"
+                    onclick="openDeleteNoticeModal(
+                        '{{ notice.notice_id }}',
+                        '{{ notice.title }}'
+                    )">
+
+                    Delete
+
+                </button>
+
+                {% endif %}
+
+            </div>
+
+
+            <div class="notice-content">
+
+                <p>
+                    {{ notice.content }}
+                </p>
+
+            </div>
+
+
+            <div class="notice-footer">
+
+                <span>
+                    Posted by {{ notice.author }}
+                </span>
+
+                <span>
+                    {{ notice.created_at }}
+                </span>
+
+            </div>
+
+        </div>
+
+        {% endfor %}
+
+    {% else %}
+
+        <div class="no-notices">
+
+            <h2>No Notices</h2>
+
+            <p>
+                There are currently no notices to display.
+            </p>
+
+        </div>
+
+    {% endif %}
+
+</div>
+
+
+<!-- ================= ADD NOTICE MODAL ================= -->
+
+{% if user.role == "admin" %}
+
+<div id="addNoticeModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Add Notice</h2>
+
+        <form action="/add-notice" method="POST">
+
+            <label>
+                Title
+            </label>
+
+            <input
+                type="text"
+                name="title"
+                placeholder="Notice title"
+                required>
+
+
+            <label>
+                Notice
+            </label>
+
+            <textarea
+                name="content"
+                placeholder="Write your notice..."
+                rows="6"
+                required></textarea>
+
+
+            <div class="modal-actions">
+
+                <button
+                    type="button"
+                    class="cancel-btn"
+                    onclick="closeAddNoticeModal()">
+
+                    Cancel
+
+                </button>
+
+                <button
+                    type="submit"
+                    class="confirm-btn">
+
+                    Post Notice
+
+                </button>
+
+            </div>
+
+        </form>
+
+    </div>
+
+</div>
+
+{% endif %}
+
+
+<!-- ================= DELETE NOTICE MODAL ================= -->
+
+{% if user.role == "admin" %}
+
+<div id="deleteNoticeModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Delete Notice</h2>
+
+        <p>
+            Are you sure you want to delete
+            <strong id="deleteNoticeTitle"></strong>?
+        </p>
+
+
+        <div class="modal-actions">
+
+            <button
+                type="button"
+                class="cancel-btn"
+                onclick="closeDeleteNoticeModal()">
+
+                Cancel
+
+            </button>
+
+
+            <form
+                id="deleteNoticeForm"
+                method="POST">
+
+                <button
+                    type="submit"
+                    class="confirm-delete-btn">
+
+                    Delete
+
+                </button>
+
+            </form>
+
+        </div>
+
+    </div>
+
+</div>
+
+{% endif %}
+
+{% endblock %}
\ No newline at end of file

Commit: 190ebf2
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 15:39:07 2026 +1200
Message: added open doc button css
---
 static/css/assembly.css | 32 +++++++++++++++++++++-----------
 templates/assembly.html |  2 +-
 2 files changed, 22 insertions(+), 12 deletions(-)

diff --git a/static/css/assembly.css b/static/css/assembly.css
index 2da94f2..9901aa1 100644
--- a/static/css/assembly.css
+++ b/static/css/assembly.css
@@ -1,25 +1,35 @@
-.document-card {
+.document-actions {
 
-    background: white;
+    display: flex;
 
-    border-radius: 12px;
+    justify-content: center;
 
-    padding: 20px;
+    margin-top: 20px;
 
-    margin-top: 25px;
+}
 
-    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
+.edit-document-button {
 
-}
+    display: inline-block;
 
-.document-card iframe {
+    padding: 10px 20px;
 
-    width: 100%;
+    background-color: #003d52;
 
-    height: 800px;
+    color: white;
 
-    border: none;
+    text-decoration: none;
 
     border-radius: 8px;
 
+    font-weight: 600;
+
+    transition: background-color 0.2s;
+
+}
+
+.edit-document-button:hover {
+
+    background-color: #00566f;
+
 }
\ No newline at end of file
diff --git a/templates/assembly.html b/templates/assembly.html
index 8778045..9919d77 100644
--- a/templates/assembly.html
+++ b/templates/assembly.html
@@ -38,7 +38,7 @@ Assemblies
             target="_blank"
             class="edit-document-button">
 
-            Open Assembly Document ↗
+            Open Assembly Document
 
         </a>
 

Commit: d10e71c
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 15:36:13 2026 +1200
Message: added open doc button
---
 templates/assembly.html | 14 ++++++++++++++
 1 file changed, 14 insertions(+)

diff --git a/templates/assembly.html b/templates/assembly.html
index 7013925..8778045 100644
--- a/templates/assembly.html
+++ b/templates/assembly.html
@@ -30,6 +30,20 @@ Assemblies
         frameborder="0">
     </iframe>
 
+
+    <div class="document-actions">
+
+        <a
+            href="https://docs.google.com/document/d/1O0Ev7imSTQ5KuuVID2BW_pdBUZOhbf-j9fIOrlPmRlg/edit"
+            target="_blank"
+            class="edit-document-button">
+
+            Open Assembly Document ↗
+
+        </a>
+
+    </div>
+
 </div>
 
 {% endblock %}
\ No newline at end of file

Commit: f93686a
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 15:32:37 2026 +1200
Message: fixed assebmlies route
---
 templates/layout.html | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/templates/layout.html b/templates/layout.html
index d558c65..51823a3 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -31,7 +31,7 @@
             <a href="/dashboard">Dashboard</a>
             <a href="/locker-duty">Locker Duty</a>
             <a href="#">Notices</a>
-            <a href="/assembly">Assemblies</a>
+            <a href="/assemblies">Assemblies</a>
 
             <!-- Only visible to admins -->
             {% if user.role == "admin" %}

Commit: dd6ecb7
Author: BHS23113 <23113@burnside.school.nz>
Date: Sat Aug 15 15:31:20 2026 +1200
Message: added aseembly
---
 main.py                 | 13 +++++++++++++
 static/css/assembly.css | 25 +++++++++++++++++++++++++
 templates/assembly.html | 35 +++++++++++++++++++++++++++++++++++
 templates/layout.html   |  2 +-
 4 files changed, 74 insertions(+), 1 deletion(-)

diff --git a/main.py b/main.py
index 16c2477..2ff2ec5 100644
--- a/main.py
+++ b/main.py
@@ -5,6 +5,8 @@ from dotenv import load_dotenv
 import sqlite3
 import os
 
+print("Hello, World!")
+
 load_dotenv(override=True)
 
 DATABASE = "prefectconnect.db"
@@ -102,6 +104,17 @@ def login():
             "status": "error",
             "message": str(e)
         }), 401
+
+@app.route("/assemblies")
+def assemblies():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    return render_template(
+        "assembly.html",
+        user=session["user"]
+    )
     
 @app.route("/users")
 def users():
diff --git a/static/css/assembly.css b/static/css/assembly.css
new file mode 100644
index 0000000..2da94f2
--- /dev/null
+++ b/static/css/assembly.css
@@ -0,0 +1,25 @@
+.document-card {
+
+    background: white;
+
+    border-radius: 12px;
+
+    padding: 20px;
+
+    margin-top: 25px;
+
+    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
+
+}
+
+.document-card iframe {
+
+    width: 100%;
+
+    height: 800px;
+
+    border: none;
+
+    border-radius: 8px;
+
+}
\ No newline at end of file
diff --git a/templates/assembly.html b/templates/assembly.html
new file mode 100644
index 0000000..7013925
--- /dev/null
+++ b/templates/assembly.html
@@ -0,0 +1,35 @@
+{% extends "layout.html" %}
+
+{% block title %}
+Assemblies
+{% endblock %}
+
+{% block css %}
+<link rel="stylesheet" href="{{ url_for('static', filename='css/assembly.css') }}">
+{% endblock %}
+
+{% block content %}
+
+<div class="topbar">
+
+    <h1>Assemblies</h1>
+
+    <p>
+        View assembly information and responsibilities.
+    </p>
+
+</div>
+
+
+<div class="document-card">
+
+    <iframe
+        src="https://docs.google.com/document/d/1O0Ev7imSTQ5KuuVID2BW_pdBUZOhbf-j9fIOrlPmRlg/preview"
+        width="100%"
+        height="800"
+        frameborder="0">
+    </iframe>
+
+</div>
+
+{% endblock %}
\ No newline at end of file
diff --git a/templates/layout.html b/templates/layout.html
index 750763b..d558c65 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -31,7 +31,7 @@
             <a href="/dashboard">Dashboard</a>
             <a href="/locker-duty">Locker Duty</a>
             <a href="#">Notices</a>
-            <a href="#">Assemblies</a>
+            <a href="/assembly">Assemblies</a>
 
             <!-- Only visible to admins -->
             {% if user.role == "admin" %}

Commit: 4fe8dd4
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 14 14:15:26 2026 +1200
Message: removed chat in layout
---
 templates/layout.html | 1 -
 1 file changed, 1 deletion(-)

diff --git a/templates/layout.html b/templates/layout.html
index 3949460..750763b 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -31,7 +31,6 @@
             <a href="/dashboard">Dashboard</a>
             <a href="/locker-duty">Locker Duty</a>
             <a href="#">Notices</a>
-            <a href="#">Chat</a>
             <a href="#">Assemblies</a>
 
             <!-- Only visible to admins -->

Commit: 7fa73c1
Author: BHS23113 <23113@burnside.school.nz>
Date: Fri Aug 14 14:12:57 2026 +1200
Message: added change role btn
---
 main.py              | 28 ++++++++++++++++++
 static/script.js     | 54 +++++++++++++++++++++++++++++-----
 templates/users.html | 82 ++++++++++++++++++++++++++++++++++++++++++++++++++--
 3 files changed, 153 insertions(+), 11 deletions(-)

diff --git a/main.py b/main.py
index 1870725..16c2477 100644
--- a/main.py
+++ b/main.py
@@ -198,6 +198,34 @@ def add_user():
     db.close()
 
     return redirect(url_for("users"))
+
+@app.route("/edit-role/<int:user_id>", methods=["POST"])
+def edit_role(user_id):
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    role = request.form["role"]
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute(
+        """
+        UPDATE users
+        SET role = ?
+        WHERE user_id = ?
+        """,
+        (role, user_id)
+    )
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("users")) 
     
 @app.route("/403")
 def forbidden():
diff --git a/static/script.js b/static/script.js
index 8b7fa05..2d2d991 100644
--- a/static/script.js
+++ b/static/script.js
@@ -1,4 +1,4 @@
-// ================= GOOGLE LOGIN =================
+// GOOGLE LOGIN 
 
 function handleCredentialResponse(response) {
 
@@ -24,17 +24,13 @@ function handleCredentialResponse(response) {
 
             window.location.href = data.redirect;
 
-        }
-
-        else {
+        } else {
 
             if (data.redirect) {
 
                 window.location.href = data.redirect;
 
-            }
-
-            else {
+            } else {
 
                 alert("Login failed");
 
@@ -47,7 +43,7 @@ function handleCredentialResponse(response) {
 }
 
 
-// ================= USERS PAGE =================
+// DELETE USER 
 
 function openDeleteModal(id, name) {
 
@@ -67,6 +63,8 @@ function closeDeleteModal() {
 }
 
 
+// ADD USER 
+
 function openAddUserModal() {
 
     document.getElementById("addUserModal").style.display = "flex";
@@ -81,17 +79,57 @@ function closeAddUserModal() {
 }
 
 
+// EDIT ROLE
+
+function openRoleModal(id, name, role) {
+
+    document.getElementById("roleModal").style.display = "flex";
+
+    document.getElementById("roleName").textContent = name;
+
+    document.getElementById("roleSelect").value = role;
+
+    document.getElementById("roleForm").action = "/edit-role/" + id;
+
+}
+
+
+function closeRoleModal() {
+
+    document.getElementById("roleModal").style.display = "none";
+
+}
+
+
+// CLOSE MODALS  
+
 window.addEventListener("click", function(event) {
 
     const deleteModal = document.getElementById("deleteModal");
+
     const addUserModal = document.getElementById("addUserModal");
 
+    const roleModal = document.getElementById("roleModal");
+
+
     if (deleteModal && event.target === deleteModal) {
+
         closeDeleteModal();
+
     }
 
+
     if (addUserModal && event.target === addUserModal) {
+
         closeAddUserModal();
+
+    }
+
+
+    if (roleModal && event.target === roleModal) {
+
+        closeRoleModal();
+
     }
 
 });
\ No newline at end of file
diff --git a/templates/users.html b/templates/users.html
index b25fed5..05be878 100644
--- a/templates/users.html
+++ b/templates/users.html
@@ -46,10 +46,19 @@ Users
 
                 <td>
 
-                    <button class="role-btn">
+                    <!-- Edit Role Button -->
+
+                    <button
+                        class="role-btn"
+                        onclick="openRoleModal('{{ member.user_id }}', '{{ member.name }}', '{{ member.role }}')">
+
                         Edit Role
+
                     </button>
 
+
+                    <!-- Delete Button -->
+
                     <button
                         class="delete-btn"
                         onclick="openDeleteModal('{{ member.user_id }}', '{{ member.name }}')">
@@ -70,7 +79,8 @@ Users
 
 </div>
 
-<!-- Delete Modal -->
+
+<!--DELETE MODAL-->
 
 <div id="deleteModal" class="modal">
 
@@ -113,7 +123,8 @@ Users
 
 </div>
 
-<!-- Add User Modal -->
+
+<!--ADD USER MODAL-->
 
 <div id="addUserModal" class="modal">
 
@@ -131,6 +142,7 @@ Users
                 placeholder="Full name"
                 required>
 
+
             <label>Email</label>
 
             <input
@@ -139,6 +151,7 @@ Users
                 placeholder="school@email.com"
                 required>
 
+
             <label>Role</label>
 
             <select name="role" required>
@@ -153,6 +166,7 @@ Users
 
             </select>
 
+
             <div class="modal-actions">
 
                 <button
@@ -180,4 +194,66 @@ Users
 
 </div>
 
+
+<!--EDIT ROLE MODAL-->
+
+<div id="roleModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Edit Role</h2>
+
+        <p>
+            Change the role for
+            <strong id="roleName"></strong>
+        </p>
+
+
+        <form id="roleForm" method="POST">
+
+            <label>Role</label>
+
+            <select
+                name="role"
+                id="roleSelect"
+                required>
+
+                <option value="prefect">
+                    Prefect
+                </option>
+
+                <option value="admin">
+                    Admin
+                </option>
+
+            </select>
+
+
+            <div class="modal-actions">
+
+                <button
+                    type="button"
+                    class="cancel-btn"
+                    onclick="closeRoleModal()">
+
+                    Cancel
+
+                </button>
+
+                <button
+                    type="submit"
+                    class="confirm-btn">
+
+                    Save Changes
+
+                </button>
+
+            </div>
+
+        </form>
+
+    </div>
+
+</div>
+
 {% endblock %}
\ No newline at end of file

Commit: 7fdd090
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 12 12:19:33 2026 +1200
Message: made add user button work
---
 main.py              | 46 ++++++++++++++++++++++++++++++-
 static/css/users.css | 57 +++++++++++++++++++++++++++++++++++++++
 static/script.js     | 50 ++++++++++++++++++++++++++++++----
 templates/users.html | 76 +++++++++++++++++++++++++++++++++++++---------------
 4 files changed, 202 insertions(+), 27 deletions(-)

diff --git a/main.py b/main.py
index 0858d08..1870725 100644
--- a/main.py
+++ b/main.py
@@ -156,6 +156,48 @@ def delete_user(user_id):
     db.close()
 
     return redirect(url_for("users"))
+
+@app.route("/add-user", methods=["POST"])
+def add_user():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    name = request.form["name"]
+    email = request.form["email"]
+    role = request.form["role"]
+
+    db = get_db()
+    cursor = db.cursor()
+
+    # Check if the email already exists
+    cursor.execute(
+        "SELECT * FROM users WHERE email=?",
+        (email,)
+    )
+
+    existing_user = cursor.fetchone()
+
+    if existing_user:
+        db.close()
+        return redirect(url_for("users"))
+
+    # Add the new user
+    cursor.execute(
+        """
+        INSERT INTO users (name, email, role)
+        VALUES (?, ?, ?)
+        """,
+        (name, email, role)
+    )
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("users"))
     
 @app.route("/403")
 def forbidden():
@@ -170,4 +212,6 @@ def logout():
 
 
 if __name__ == "__main__":
-    app.run(debug=True)
\ No newline at end of file
+    app.run(debug=True)
+
+    
\ No newline at end of file
diff --git a/static/css/users.css b/static/css/users.css
index 1fead04..03829a5 100644
--- a/static/css/users.css
+++ b/static/css/users.css
@@ -148,4 +148,61 @@ td button:hover {
 
 .confirm-delete-btn:hover {
     background: #b91c1c;
+}
+
+/* ================= ADD USER MODAL ================= */
+
+.modal-content label {
+
+    display: block;
+    font-weight: 600;
+    margin-top: 15px;
+    margin-bottom: 6px;
+
+}
+
+.modal-content input,
+.modal-content select {
+
+    width: 100%;
+    padding: 10px 12px;
+
+    margin-bottom: 20px;
+
+    border: 1px solid #d1d5db;
+    border-radius: 8px;
+
+    font-size: 15px;
+    box-sizing: border-box;
+
+}
+
+.modal-content input:focus,
+.modal-content select:focus {
+
+    outline: none;
+    border-color: #2563eb;
+
+}
+
+.confirm-btn {
+
+    background: #2563eb;
+    color: white;
+
+    border: none;
+    border-radius: 8px;
+
+    padding: 10px 20px;
+
+    cursor: pointer;
+
+    transition: background 0.2s;
+
+}
+
+.confirm-btn:hover {
+
+    background: #1d4ed8;
+
 }
\ No newline at end of file
diff --git a/static/script.js b/static/script.js
index da0b6b0..8b7fa05 100644
--- a/static/script.js
+++ b/static/script.js
@@ -1,4 +1,7 @@
+// ================= GOOGLE LOGIN =================
+
 function handleCredentialResponse(response) {
+
     console.log("TOKEN:", response.credential);
 
     fetch("/login", {
@@ -10,25 +13,41 @@ function handleCredentialResponse(response) {
             credential: response.credential
         })
     })
+
     .then(res => res.json())
+
     .then(data => {
+
         console.log("SERVER RESPONSE:", data);
 
         if (data.status === "success") {
+
             window.location.href = data.redirect;
-        } 
+
+        }
+
         else {
+
             if (data.redirect) {
+
                 window.location.href = data.redirect;
-            } else {
+
+            }
+
+            else {
+
                 alert("Login failed");
+
             }
+
         }
+
     });
+
 }
 
 
-// ---------- Delete User Modal ----------
+// ================= USERS PAGE =================
 
 function openDeleteModal(id, name) {
 
@@ -40,18 +59,39 @@ function openDeleteModal(id, name) {
 
 }
 
+
 function closeDeleteModal() {
 
     document.getElementById("deleteModal").style.display = "none";
 
 }
 
+
+function openAddUserModal() {
+
+    document.getElementById("addUserModal").style.display = "flex";
+
+}
+
+
+function closeAddUserModal() {
+
+    document.getElementById("addUserModal").style.display = "none";
+
+}
+
+
 window.addEventListener("click", function(event) {
 
-    const modal = document.getElementById("deleteModal");
+    const deleteModal = document.getElementById("deleteModal");
+    const addUserModal = document.getElementById("addUserModal");
 
-    if (event.target === modal) {
+    if (deleteModal && event.target === deleteModal) {
         closeDeleteModal();
     }
 
+    if (addUserModal && event.target === addUserModal) {
+        closeAddUserModal();
+    }
+
 });
\ No newline at end of file
diff --git a/templates/users.html b/templates/users.html
index 17abfcb..b25fed5 100644
--- a/templates/users.html
+++ b/templates/users.html
@@ -16,7 +16,9 @@ Users
 </div>
 
 <div class="actions">
-    <a href="#" class="button">+ Add User</a>
+    <button class="button" onclick="openAddUserModal()">
+        + Add User
+    </button>
 </div>
 
 <div class="table-card">
@@ -68,8 +70,7 @@ Users
 
 </div>
 
-
-<!-- Delete Confirmation Modal -->
+<!-- Delete Modal -->
 
 <div id="deleteModal" class="modal">
 
@@ -86,6 +87,7 @@ Users
         <div class="modal-actions">
 
             <button
+                type="button"
                 class="cancel-btn"
                 onclick="closeDeleteModal()">
 
@@ -111,39 +113,71 @@ Users
 
 </div>
 
-{% endblock %}
+<!-- Add User Modal -->
+
+<div id="addUserModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Add User</h2>
+
+        <form action="/add-user" method="POST">
+
+            <label>Name</label>
+
+            <input
+                type="text"
+                name="name"
+                placeholder="Full name"
+                required>
 
+            <label>Email</label>
 
-{% block scripts %}
+            <input
+                type="email"
+                name="email"
+                placeholder="school@email.com"
+                required>
 
-<script>
+            <label>Role</label>
 
-function openDeleteModal(id, name) {
+            <select name="role" required>
 
-    document.getElementById("deleteModal").style.display = "flex";
+                <option value="prefect">
+                    Prefect
+                </option>
 
-    document.getElementById("deleteName").textContent = name;
+                <option value="admin">
+                    Admin
+                </option>
 
-    document.getElementById("deleteForm").action = "/delete-user/" + id;
+            </select>
 
-}
+            <div class="modal-actions">
 
-function closeDeleteModal() {
+                <button
+                    type="button"
+                    class="cancel-btn"
+                    onclick="closeAddUserModal()">
 
-    document.getElementById("deleteModal").style.display = "none";
+                    Cancel
 
-}
+                </button>
 
-window.onclick = function(event) {
+                <button
+                    type="submit"
+                    class="confirm-btn">
 
-    const modal = document.getElementById("deleteModal");
+                    Add User
 
-    if (event.target == modal) {
-        closeDeleteModal();
-    }
+                </button>
 
-}
+            </div>
 
-</script>
+        </form>
+
+    </div>
+
+</div>
 
 {% endblock %}
\ No newline at end of file

Commit: 0cec02f
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Aug 6 11:38:57 2026 +1200
Message: changed .onclick to .addevent for better javascript interaction
---
 static/script.js | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/static/script.js b/static/script.js
index 1c1f87f..da0b6b0 100644
--- a/static/script.js
+++ b/static/script.js
@@ -46,7 +46,7 @@ function closeDeleteModal() {
 
 }
 
-window.onclick = function(event) {
+window.addEventListener("click", function(event) {
 
     const modal = document.getElementById("deleteModal");
 
@@ -54,4 +54,4 @@ window.onclick = function(event) {
         closeDeleteModal();
     }
 
-}
\ No newline at end of file
+});
\ No newline at end of file

Commit: 902e6e2
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Aug 6 11:33:41 2026 +1200
Message: fixed java html pull
---
 templates/layout.html | 4 ++++
 1 file changed, 4 insertions(+)

diff --git a/templates/layout.html b/templates/layout.html
index 28c1c43..3949460 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -16,6 +16,7 @@
     <!-- Page-specific CSS -->
     {% block css %}
     {% endblock %}
+
 </head>
 
 <body>
@@ -52,6 +53,9 @@
 
     </div>
 
+    <!-- Shared JavaScript -->
+    <script src="{{ url_for('static', filename='script.js') }}"></script>
+
     <!-- Page-specific JavaScript -->
     {% block scripts %}
     {% endblock %}

Commit: 24ad1d9
Author: BHS23113 <23113@burnside.school.nz>
Date: Wed Aug 5 11:43:18 2026 +1200
Message: made confirm delete button better for hci
---
 static/css/users.css | 66 +++++++++++++++++++++++++++++++++++
 static/script.js     | 29 ++++++++++++++++
 templates/users.html | 97 ++++++++++++++++++++++++++++++++++++++++++++--------
 3 files changed, 178 insertions(+), 14 deletions(-)

diff --git a/static/css/users.css b/static/css/users.css
index 68fe91b..1fead04 100644
--- a/static/css/users.css
+++ b/static/css/users.css
@@ -82,4 +82,70 @@ td button {
 
 td button:hover {
     background-color: #005c7a;
+}
+
+/* ---------- Delete Modal ---------- */
+
+.modal {
+    display: none;
+    position: fixed;
+    inset: 0;
+    background: rgba(0, 0, 0, 0.45);
+    justify-content: center;
+    align-items: center;
+    z-index: 1000;
+}
+
+.modal-content {
+    background: white;
+    width: 420px;
+    max-width: 90%;
+    border-radius: 12px;
+    padding: 30px;
+    text-align: center;
+    box-shadow: 0 15px 40px rgba(0,0,0,.2);
+}
+
+.modal-content h2 {
+    margin-top: 0;
+    margin-bottom: 12px;
+}
+
+.modal-content p {
+    color: #555;
+    margin-bottom: 25px;
+}
+
+.modal-actions {
+    display: flex;
+    justify-content: center;
+    gap: 15px;
+}
+
+.cancel-btn,
+.confirm-delete-btn {
+    padding: 10px 22px;
+    border: none;
+    border-radius: 8px;
+    cursor: pointer;
+    font-size: 15px;
+    transition: 0.2s;
+}
+
+.cancel-btn {
+    background: #e5e7eb;
+    color: #333;
+}
+
+.cancel-btn:hover {
+    background: #d1d5db;
+}
+
+.confirm-delete-btn {
+    background: #dc2626;
+    color: white;
+}
+
+.confirm-delete-btn:hover {
+    background: #b91c1c;
 }
\ No newline at end of file
diff --git a/static/script.js b/static/script.js
index bdbc691..1c1f87f 100644
--- a/static/script.js
+++ b/static/script.js
@@ -25,4 +25,33 @@ function handleCredentialResponse(response) {
             }
         }
     });
+}
+
+
+// ---------- Delete User Modal ----------
+
+function openDeleteModal(id, name) {
+
+    document.getElementById("deleteModal").style.display = "flex";
+
+    document.getElementById("deleteName").textContent = name;
+
+    document.getElementById("deleteForm").action = "/delete-user/" + id;
+
+}
+
+function closeDeleteModal() {
+
+    document.getElementById("deleteModal").style.display = "none";
+
+}
+
+window.onclick = function(event) {
+
+    const modal = document.getElementById("deleteModal");
+
+    if (event.target === modal) {
+        closeDeleteModal();
+    }
+
 }
\ No newline at end of file
diff --git a/templates/users.html b/templates/users.html
index f4b374a..17abfcb 100644
--- a/templates/users.html
+++ b/templates/users.html
@@ -39,9 +39,7 @@ Users
             <tr>
 
                 <td>{{ member.name }}</td>
-
                 <td>{{ member.email }}</td>
-
                 <td>{{ member.role }}</td>
 
                 <td>
@@ -50,20 +48,13 @@ Users
                         Edit Role
                     </button>
 
-                    <form action="/delete-user/{{ member.user_id }}"
-                          method="POST"
-                          style="display: inline;">
-
-                        <button
-                            type="submit"
-                            class="delete-btn"
-                            onclick="return confirm('Are you sure you want to delete {{ member.name }}?')">
+                    <button
+                        class="delete-btn"
+                        onclick="openDeleteModal('{{ member.user_id }}', '{{ member.name }}')">
 
-                            Delete
+                        Delete
 
-                        </button>
-
-                    </form>
+                    </button>
 
                 </td>
 
@@ -77,4 +68,82 @@ Users
 
 </div>
 
+
+<!-- Delete Confirmation Modal -->
+
+<div id="deleteModal" class="modal">
+
+    <div class="modal-content">
+
+        <h2>Delete User</h2>
+
+        <p>
+            Are you sure you want to remove
+            <strong id="deleteName"></strong>
+            from PrefectConnect?
+        </p>
+
+        <div class="modal-actions">
+
+            <button
+                class="cancel-btn"
+                onclick="closeDeleteModal()">
+
+                Cancel
+
+            </button>
+
+            <form id="deleteForm" method="POST">
+
+                <button
+                    type="submit"
+                    class="confirm-delete-btn">
+
+                    Delete
+
+                </button>
+
+            </form>
+
+        </div>
+
+    </div>
+
+</div>
+
+{% endblock %}
+
+
+{% block scripts %}
+
+<script>
+
+function openDeleteModal(id, name) {
+
+    document.getElementById("deleteModal").style.display = "flex";
+
+    document.getElementById("deleteName").textContent = name;
+
+    document.getElementById("deleteForm").action = "/delete-user/" + id;
+
+}
+
+function closeDeleteModal() {
+
+    document.getElementById("deleteModal").style.display = "none";
+
+}
+
+window.onclick = function(event) {
+
+    const modal = document.getElementById("deleteModal");
+
+    if (event.target == modal) {
+        closeDeleteModal();
+    }
+
+}
+
+</script>
+
 {% endblock %}
\ No newline at end of file

Commit: 52b7365
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 30 12:41:11 2026 +1200
Message: made the delete user work
---
 main.py              | 26 ++++++++++++++++++++++++++
 templates/users.html | 32 ++++++++++++++++++--------------
 2 files changed, 44 insertions(+), 14 deletions(-)

diff --git a/main.py b/main.py
index d79035b..0858d08 100644
--- a/main.py
+++ b/main.py
@@ -130,6 +130,32 @@ def users():
         user=session["user"],
         users=users
     )
+
+@app.route("/delete-user/<int:user_id>", methods=["POST"])
+def delete_user(user_id):
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    # Prevent an admin from deleting themselves
+    if user_id == session["user"]["user_id"]:
+        return redirect(url_for("users"))
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute(
+        "DELETE FROM users WHERE user_id = ?",
+        (user_id,)
+    )
+
+    db.commit()
+    db.close()
+
+    return redirect(url_for("users"))
     
 @app.route("/403")
 def forbidden():
diff --git a/templates/users.html b/templates/users.html
index b3e4834..f4b374a 100644
--- a/templates/users.html
+++ b/templates/users.html
@@ -28,7 +28,6 @@ Users
                 <th>Name</th>
                 <th>Email</th>
                 <th>Role</th>
-                <th>Status</th>
                 <th>Actions</th>
             </tr>
         </thead>
@@ -46,21 +45,26 @@ Users
                 <td>{{ member.role }}</td>
 
                 <td>
-                    {% if member.is_active %}
-                        Active
-                    {% else %}
-                        Inactive
-                    {% endif %}
-                </td>
 
-                <td>
-                    <button>Edit Role</button>
+                    <button class="role-btn">
+                        Edit Role
+                    </button>
+
+                    <form action="/delete-user/{{ member.user_id }}"
+                          method="POST"
+                          style="display: inline;">
+
+                        <button
+                            type="submit"
+                            class="delete-btn"
+                            onclick="return confirm('Are you sure you want to delete {{ member.name }}?')">
+
+                            Delete
+
+                        </button>
+
+                    </form>
 
-                    {% if member.is_active %}
-                        <button>Deactivate</button>
-                    {% else %}
-                        <button>Activate</button>
-                    {% endif %}
                 </td>
 
             </tr>

Commit: 05be67d
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 30 10:03:42 2026 +1200
Message: updated the side bar
---
 templates/layout.html | 22 ++++++++++++++++------
 1 file changed, 16 insertions(+), 6 deletions(-)

diff --git a/templates/layout.html b/templates/layout.html
index 2a172ae..28c1c43 100644
--- a/templates/layout.html
+++ b/templates/layout.html
@@ -3,24 +3,26 @@
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
+
     <title>
         {% block title %}
         PrefectConnect
         {% endblock %}
     </title>
 
-    <!-- CSS -->
+    <!-- Shared CSS -->
     <link rel="stylesheet" href="{{ url_for('static', filename='css/layout.css') }}">
 
     <!-- Page-specific CSS -->
     {% block css %}
     {% endblock %}
-
 </head>
+
 <body>
-    <div class ="layout">
 
-        <!--Side Bar-->
+    <div class="layout">
+
+        <!-- SIDEBAR -->
         <div class="sidebar">
 
             <h2>PREFECTS</h2>
@@ -31,18 +33,26 @@
             <a href="#">Chat</a>
             <a href="#">Assemblies</a>
 
+            <!-- Only visible to admins -->
+            {% if user.role == "admin" %}
+                <a href="/users">Users</a>
+            {% endif %}
+
             <a href="/logout" class="logout">Logout</a>
 
         </div>
 
-        <main class="main-content">
+        <!-- PAGE CONTENT -->
+        <div class="main-content">
 
             {% block content %}
             {% endblock %}
 
-        </main>
+        </div>
+
     </div>
 
+    <!-- Page-specific JavaScript -->
     {% block scripts %}
     {% endblock %}
 

Commit: 96322c7
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 30 10:03:29 2026 +1200
Message: added route for users
---
 main.py | 33 +++++++++++++++++++++++++++++++--
 1 file changed, 31 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index 987ae3c..d79035b 100644
--- a/main.py
+++ b/main.py
@@ -72,7 +72,7 @@ def login():
 
         user = cursor.fetchone()
 
-        # If the email isn't in the database deny access
+        # If the email isn't in the database, deny access
         if user is None:
             db.close()
 
@@ -85,7 +85,8 @@ def login():
         session["user"] = {
             "user_id": user["user_id"],
             "email": user["email"],
-            "name": user["name"]
+            "name": user["name"],
+            "role": user["role"]
         }
 
         db.close()
@@ -102,6 +103,34 @@ def login():
             "message": str(e)
         }), 401
     
+@app.route("/users")
+def users():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    if session["user"]["role"] != "admin":
+        return render_template("403.html"), 403
+
+    db = get_db()
+    cursor = db.cursor()
+
+    cursor.execute("""
+        SELECT *
+        FROM users
+        ORDER BY name
+    """)
+
+    users = cursor.fetchall()
+
+    db.close()
+
+    return render_template(
+        "users.html",
+        user=session["user"],
+        users=users
+    )
+    
 @app.route("/403")
 def forbidden():
 

Commit: e1d0bba
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 30 10:03:19 2026 +1200
Message: added users page
---
 static/css/users.css | 85 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 templates/users.html | 76 ++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 161 insertions(+)

diff --git a/static/css/users.css b/static/css/users.css
new file mode 100644
index 0000000..68fe91b
--- /dev/null
+++ b/static/css/users.css
@@ -0,0 +1,85 @@
+/* TOP BAR */
+.topbar {
+    margin-bottom: 30px;
+}
+
+.topbar h1 {
+    font-size: 2.5rem;
+    color: #003d52;
+    margin-bottom: 8px;
+}
+
+.topbar p {
+    color: #555;
+}
+
+/* ACTION BUTTON */
+.actions {
+    margin-bottom: 25px;
+}
+
+.button {
+    display: inline-block;
+    background-color: #003d52;
+    color: white;
+    text-decoration: none;
+    padding: 12px 20px;
+    border-radius: 8px;
+    font-weight: bold;
+    transition: 0.2s;
+}
+
+.button:hover {
+    background-color: #005c7a;
+}
+
+/* TABLE CARD */
+.table-card {
+    background: white;
+    border-radius: 12px;
+    padding: 25px;
+    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
+}
+
+/* TABLE */
+table {
+    width: 100%;
+    border-collapse: collapse;
+}
+
+/* HEADERS */
+th {
+    background-color: #f5f5f5;
+    color: #003d52;
+    text-align: left;
+    padding: 14px;
+    border-bottom: 2px solid #ddd;
+}
+
+/* CELLS */
+td {
+    padding: 14px;
+    border-bottom: 1px solid #eee;
+    color: #333;
+}
+
+/* ROW HOVER */
+tbody tr:hover {
+    background-color: #fafafa;
+}
+
+/* ACTION BUTTONS */
+td button {
+    background-color: #003d52;
+    color: white;
+    border: none;
+    padding: 8px 14px;
+    margin-right: 8px;
+    border-radius: 6px;
+    cursor: pointer;
+    transition: 0.2s;
+}
+
+td button:hover {
+    background-color: #005c7a;
+}
\ No newline at end of file
diff --git a/templates/users.html b/templates/users.html
new file mode 100644
index 0000000..b3e4834
--- /dev/null
+++ b/templates/users.html
@@ -0,0 +1,76 @@
+{% extends "layout.html" %}
+
+{% block title %}
+Users
+{% endblock %}
+
+{% block css %}
+<link rel="stylesheet" href="{{ url_for('static', filename='css/users.css') }}">
+{% endblock %}
+
+{% block content %}
+
+<div class="topbar">
+    <h1>Users</h1>
+    <p>Manage prefect accounts and permissions.</p>
+</div>
+
+<div class="actions">
+    <a href="#" class="button">+ Add User</a>
+</div>
+
+<div class="table-card">
+
+    <table>
+
+        <thead>
+            <tr>
+                <th>Name</th>
+                <th>Email</th>
+                <th>Role</th>
+                <th>Status</th>
+                <th>Actions</th>
+            </tr>
+        </thead>
+
+        <tbody>
+
+            {% for member in users %}
+
+            <tr>
+
+                <td>{{ member.name }}</td>
+
+                <td>{{ member.email }}</td>
+
+                <td>{{ member.role }}</td>
+
+                <td>
+                    {% if member.is_active %}
+                        Active
+                    {% else %}
+                        Inactive
+                    {% endif %}
+                </td>
+
+                <td>
+                    <button>Edit Role</button>
+
+                    {% if member.is_active %}
+                        <button>Deactivate</button>
+                    {% else %}
+                        <button>Activate</button>
+                    {% endif %}
+                </td>
+
+            </tr>
+
+            {% endfor %}
+
+        </tbody>
+
+    </table>
+
+</div>
+
+{% endblock %}
\ No newline at end of file

Commit: 6a4c186
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 12:38:32 2026 +1200
Message: added 403 css and changed html
---
 main.py            |  2 +-
 static/css/403.css | 74 ++++++++++++++++++++++++++++++++++++++++++++++++++++++
 templates/403.html | 41 ++++++++++++++++++------------
 3 files changed, 100 insertions(+), 17 deletions(-)

diff --git a/main.py b/main.py
index e8a314e..987ae3c 100644
--- a/main.py
+++ b/main.py
@@ -72,7 +72,7 @@ def login():
 
         user = cursor.fetchone()
 
-        # If the email isn't in the database, deny access
+        # If the email isn't in the database deny access
         if user is None:
             db.close()
 
diff --git a/static/css/403.css b/static/css/403.css
new file mode 100644
index 0000000..99ee9f5
--- /dev/null
+++ b/static/css/403.css
@@ -0,0 +1,74 @@
+/* RESET */
+* {
+    margin: 0;
+    padding: 0;
+    box-sizing: border-box;
+    font-family: Arial, Helvetica, sans-serif;
+}
+
+/* BODY */
+body {
+    background-color: #ececec;
+
+    display: flex;
+    justify-content: center;
+    align-items: center;
+
+    min-height: 100vh;
+}
+
+/* ERROR CARD */
+.error-card {
+    width: 650px;
+    background-color: #003d52;
+    color: white;
+
+    padding: 60px;
+    border-radius: 12px;
+
+    text-align: center;
+
+    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
+}
+
+/* ERROR NUMBER */
+.error-card h1 {
+    font-size: 5rem;
+    margin-bottom: 10px;
+}
+
+/* HEADING */
+.error-card h2 {
+    font-size: 2rem;
+    margin-bottom: 25px;
+}
+
+/* TEXT */
+.error-card p {
+    font-size: 1.1rem;
+    line-height: 1.6;
+    margin-bottom: 20px;
+}
+
+/* BUTTON */
+.button {
+    display: inline-block;
+
+    margin-top: 20px;
+    padding: 12px 28px;
+
+    background-color: white;
+    color: #003d52;
+
+    text-decoration: none;
+    font-weight: bold;
+
+    border-radius: 8px;
+
+    transition: 0.2s;
+}
+
+/* BUTTON HOVER */
+.button:hover {
+    background-color: #e5e5e5;
+}
\ No newline at end of file
diff --git a/templates/403.html b/templates/403.html
index 7e4a8c5..7180f98 100644
--- a/templates/403.html
+++ b/templates/403.html
@@ -1,26 +1,35 @@
-{% extends "layout.html" %}
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>Access Denied</title>
 
-{% block title %}
-Access Denied
-{% endblock %}
+    <link rel="stylesheet"
+          href="{{ url_for('static', filename='css/403.css') }}">
+</head>
 
+<body>
 
-{% block content %}
+    <div class="error-card">
 
-<div class="error-page">
+        <h1>403</h1>
 
-    <h1>403<br><br></h1>
+        <h2>Access Denied</h2>
 
-    <h2>Access Denied<br><br></h2>
+        <p>
+            Your Google account isn't registered to use PrefectConnect.
+        </p>
 
-    <p>
-        Sorry, your account is not registered as a PrefectConnect user.<br>If you believe this is a mistake, please contact an administrator.<br><br>
-    </p>
+        <p>
+            If you believe this is a mistake, please contact an administrator.
+        </p>
 
-    <a href="/" class="error-button">
-        Return to Login
-    </a>
+        <a href="/" class="button">
+            Return to Login
+        </a>
 
-</div>
+    </div>
 
-{% endblock %}
\ No newline at end of file
+</body>
+</html>
\ No newline at end of file

Commit: 77826c5
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 04:23:45 2026 +1200
Message: added route and redirect
---
 main.py | 7 ++++++-
 1 file changed, 6 insertions(+), 1 deletion(-)

diff --git a/main.py b/main.py
index a86d509..e8a314e 100644
--- a/main.py
+++ b/main.py
@@ -78,7 +78,7 @@ def login():
 
             return jsonify({
                 "status": "error",
-                "message": "You are not authorised to access PrefectConnect."
+                "redirect": "/403"
             }), 403
 
         # Store DB user in session
@@ -101,6 +101,11 @@ def login():
             "status": "error",
             "message": str(e)
         }), 401
+    
+@app.route("/403")
+def forbidden():
+
+    return render_template("403.html"), 403
 
 
 @app.route("/logout")

Commit: 91b80d1
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 04:22:24 2026 +1200
Message: updated js
---
 static/script.js | 9 +++++++--
 1 file changed, 7 insertions(+), 2 deletions(-)

diff --git a/static/script.js b/static/script.js
index 195f8d6..bdbc691 100644
--- a/static/script.js
+++ b/static/script.js
@@ -16,8 +16,13 @@ function handleCredentialResponse(response) {
 
         if (data.status === "success") {
             window.location.href = data.redirect;
-        } else {
-            alert("Login failed");
+        } 
+        else {
+            if (data.redirect) {
+                window.location.href = data.redirect;
+            } else {
+                alert("Login failed");
+            }
         }
     });
 }
\ No newline at end of file

Commit: e035da8
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 04:20:43 2026 +1200
Message: added 403 page
---
 templates/403.html | 26 ++++++++++++++++++++++++++
 1 file changed, 26 insertions(+)

diff --git a/templates/403.html b/templates/403.html
new file mode 100644
index 0000000..7e4a8c5
--- /dev/null
+++ b/templates/403.html
@@ -0,0 +1,26 @@
+{% extends "layout.html" %}
+
+{% block title %}
+Access Denied
+{% endblock %}
+
+
+{% block content %}
+
+<div class="error-page">
+
+    <h1>403<br><br></h1>
+
+    <h2>Access Denied<br><br></h2>
+
+    <p>
+        Sorry, your account is not registered as a PrefectConnect user.<br>If you believe this is a mistake, please contact an administrator.<br><br>
+    </p>
+
+    <a href="/" class="error-button">
+        Return to Login
+    </a>
+
+</div>
+
+{% endblock %}
\ No newline at end of file

Commit: 083898f
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 04:05:33 2026 +1200
Message: added restricted login
---
 main.py | 20 +++++++-------------
 1 file changed, 7 insertions(+), 13 deletions(-)

diff --git a/main.py b/main.py
index 4d0709e..a86d509 100644
--- a/main.py
+++ b/main.py
@@ -72,20 +72,14 @@ def login():
 
         user = cursor.fetchone()
 
-        # Create user if first login
+        # If the email isn't in the database, deny access
         if user is None:
-            cursor.execute("""
-                INSERT INTO users (email, name, role)
-                VALUES (?, ?, ?)
-            """, (email, name, "prefect"))
-
-            db.commit()
-
-            cursor.execute(
-                "SELECT * FROM users WHERE email=?",
-                (email,)
-            )
-            user = cursor.fetchone()
+            db.close()
+
+            return jsonify({
+                "status": "error",
+                "message": "You are not authorised to access PrefectConnect."
+            }), 403
 
         # Store DB user in session
         session["user"] = {

Commit: 985e18f
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 00:09:15 2026 +1200
Message: fixed css path
---
 static/css/{style.css => index.css} | 0
 templates/index.html                | 2 +-
 2 files changed, 1 insertion(+), 1 deletion(-)

diff --git a/static/css/style.css b/static/css/index.css
similarity index 100%
rename from static/css/style.css
rename to static/css/index.css
diff --git a/templates/index.html b/templates/index.html
index e1e6d19..285b048 100644
--- a/templates/index.html
+++ b/templates/index.html
@@ -9,7 +9,7 @@
     <script src="https://accounts.google.com/gsi/client" async defer></script>
 
     <!-- CSS -->
-    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
+    <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
 </head>
 
 <body>

Commit: 86096b7
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 00:06:05 2026 +1200
Message: added layout in locker duty
---
 static/css/locker_duty.css |  89 +++-------------------
 templates/locker_duty.html | 182 ++++++++++++++++++++++++++-------------------
 2 files changed, 115 insertions(+), 156 deletions(-)

diff --git a/static/css/locker_duty.css b/static/css/locker_duty.css
index 22b1d7a..9cb295e 100644
--- a/static/css/locker_duty.css
+++ b/static/css/locker_duty.css
@@ -1,133 +1,64 @@
-/* RESET */
-* {
-    margin: 0;
-    padding: 0;
-    box-sizing: border-box;
-    font-family: Arial, Helvetica, sans-serif;
-}
-
-/* BODY */
-body {
-    background-color: #ececec;
-    color: #003d52;
-}
-
-/* PAGE LAYOUT */
-.layout {
-    display: flex;
-    min-height: 100vh;
-}
-
-/* SIDEBAR */
-.sidebar {
-    width: 250px;
-    background-color: #003d52;
-    color: white;
-    padding: 20px;
-
-    display: flex;
-    flex-direction: column;
-    gap: 20px;
-}
-
-.sidebar h2 {
-    margin-bottom: 20px;
-}
-
-/* SIDEBAR LINKS */
-.sidebar a {
-    color: white;
-    text-decoration: none;
-    padding: 10px;
-    border-radius: 6px;
-    transition: 0.2s;
-}
-
-.sidebar a:hover {
-    background-color: rgba(255,255,255,0.1);
-}
-
-/* LOGOUT BUTTON */
-.sidebar .logout {
-    margin-top: auto;
-    background-color: white;
-    color: #003d52;
-    text-align: center;
-    font-weight: bold;
-}
-
-.sidebar .logout:hover {
-    background-color: #e5e5e5;
-}
-
-/* MAIN CONTENT */
-.main-content {
-    flex: 1;
-    padding: 40px;
-}
-
-/* PAGE TITLE */
-.main-content h1 {
+h1 {
     color: #003d52;
     margin-bottom: 10px;
     font-size: 2.2rem;
 }
 
-/* DESCRIPTION */
-.main-content p {
+p {
     color: #555;
     margin-bottom: 30px;
     line-height: 1.5;
 }
 
-/* WEEK CARDS LAYOUT */
 .container {
     display: flex;
     gap: 30px;
 }
 
-/* WEEK CARD */
 .week {
     flex: 1;
     background: white;
     border-radius: 12px;
     padding: 20px;
+
     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
 }
 
-/* WEEK TITLE */
 .week h2 {
     background-color: #003d52;
     color: white;
+
     text-align: center;
+
     padding: 12px;
+
     border-radius: 8px;
+
     margin-bottom: 20px;
 }
 
-/* TABLE */
 table {
     width: 100%;
     border-collapse: collapse;
 }
 
-/* TABLE HEADERS */
 th {
     background-color: #f5f5f5;
     color: #003d52;
+
     text-align: left;
+
     padding: 12px;
+
     border-bottom: 2px solid #ddd;
 }
 
-/* TABLE CELLS */
 td {
     padding: 12px;
     border-bottom: 1px solid #eee;
     color: #333;
 }
 
-/* HOVER EFFECT */
 tr:hover td {
     background-color: #f7f7f7;
 }
\ No newline at end of file
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index e97e4c8..ac53123 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -1,78 +1,106 @@
-<!DOCTYPE html>
-<html lang="en">
-<head>
-    <meta charset="UTF-8">
-    <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <title>Locker Duty</title>
-
-    <link rel="stylesheet" href="{{ url_for('static', filename='css/locker_duty.css') }}?v=2">
-</head>
-
-<body>
-    <div class="layout">
-        <div class="sidebar">
-            <h2>PREFECTS</h2>
-
-            <a href="/dashboard">Dashboard</a>
-            <a href="/locker-duty">Locker Duty</a>
-            <a href="#">Notices</a>
-            <a href="#">Chat</a>
-            <a href="#">Assemblies</a>
-
-            <a href="/logout" class="logout">Logout</a>
-        </div>
-        <div class="main-content">
-            <!-- PAGE TITLE -->
-            <h1>Locker Duty Roster</h1>
-
-            <p>
-                Lock the side doors on arrival - there will be staff on duty to assist.<br>
-                Monitor student behaviour.
-            </p>
-
-            <!-- MAIN CONTAINER -->
-            <div class="container">
-
-                <!-- WEEK A -->
-                <div class="week">
-                    <h2>WEEK A</h2>
-
-                    <table>
-                        <tr>
-                            <th>Day</th>
-                            <th>Students</th>
-                        </tr>
-
-                        <tr><td>Monday</td><td>Elizabeth, Rosie</td></tr>
-                        <tr><td>Tuesday</td><td>Barnaby, Samuel</td></tr>
-                        <tr><td>Wednesday</td><td>Ava, Dasha</td></tr>
-                        <tr><td>Thursday</td><td>Sione, Michaela</td></tr>
-                        <tr><td>Friday</td><td>James, Luke</td></tr>
-
-                    </table>
-                </div>
-
-                <!-- WEEK B -->
-                <div class="week">
-                    <h2>WEEK B</h2>
-
-                    <table>
-                        <tr>
-                            <th>Day</th>
-                            <th>Students</th>
-                        </tr>
-
-                        <tr><td>Monday</td><td>Zoe, Chloe</td></tr>
-                        <tr><td>Tuesday</td><td>Kanon, Ida</td></tr>
-                        <tr><td>Wednesday</td><td>Lukas, Messi</td></tr>
-                        <tr><td>Thursday</td><td>Sho, Aaron</td></tr>
-                        <tr><td>Friday</td><td>Eason, Nilana</td></tr>
-
-                    </table>
-                </div>
-
-            </div>
-        </div>
+{% extends "layout.html" %}
+
+{% block title %}
+Locker Duty
+{% endblock %}
+
+{% block css %}
+<link rel="stylesheet" href="{{ url_for('static', filename='css/locker_duty.css') }}">
+{% endblock %}
+
+{% block content %}
+
+<h1>Locker Duty Roster</h1>
+
+<p>
+    Lock the side doors on arrival - there will be staff on duty to assist.<br>
+    Monitor student behaviour.
+</p>
+
+<div class="container">
+
+    <!-- WEEK A -->
+    <div class="week">
+
+        <h2>WEEK A</h2>
+
+        <table>
+
+            <tr>
+                <th>Day</th>
+                <th>Students</th>
+            </tr>
+
+            <tr>
+                <td>Monday</td>
+                <td>Elizabeth, Rosie</td>
+            </tr>
+
+            <tr>
+                <td>Tuesday</td>
+                <td>Barnaby, Samuel</td>
+            </tr>
+
+            <tr>
+                <td>Wednesday</td>
+                <td>Ava, Dasha</td>
+            </tr>
+
+            <tr>
+                <td>Thursday</td>
+                <td>Sione, Michaela</td>
+            </tr>
+
+            <tr>
+                <td>Friday</td>
+                <td>James, Luke</td>
+            </tr>
+
+        </table>
+
     </div>
-</body>
-</html>
\ No newline at end of file
+
+    <!-- WEEK B -->
+    <div class="week">
+
+        <h2>WEEK B</h2>
+
+        <table>
+
+            <tr>
+                <th>Day</th>
+                <th>Students</th>
+            </tr>
+
+            <tr>
+                <td>Monday</td>
+                <td>Zoe, Chloe</td>
+            </tr>
+
+            <tr>
+                <td>Tuesday</td>
+                <td>Kanon, Ida</td>
+            </tr>
+
+            <tr>
+                <td>Wednesday</td>
+                <td>Lukas, Messi</td>
+            </tr>
+
+            <tr>
+                <td>Thursday</td>
+                <td>Sho, Aaron</td>
+            </tr>
+
+            <tr>
+                <td>Friday</td>
+                <td>Eason, Nilana</td>
+            </tr>
+
+        </table>
+
+    </div>
+
+</div>
+
+{% endblock %}
\ No newline at end of file

Commit: 03d6a0a
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 00:05:48 2026 +1200
Message: added layout in dashbpard
---
 static/css/dashboard.css | 60 +------------------------------------
 templates/dashboard.html | 77 +++++++++++++++++-------------------------------
 2 files changed, 28 insertions(+), 109 deletions(-)

diff --git a/static/css/dashboard.css b/static/css/dashboard.css
index 87045ba..bd0cd07 100644
--- a/static/css/dashboard.css
+++ b/static/css/dashboard.css
@@ -1,60 +1,3 @@
-/* RESET */
-* {
-    margin: 0;
-    padding: 0;
-    box-sizing: border-box;
-    font-family: Arial, Helvetica, sans-serif;
-}
-
-/* LAYOUT */
-.layout {
-    display: flex;
-    min-height: 100vh;
-}
-
-/* SIDEBAR */
-.sidebar {
-    width: 250px;
-    background-color: #003d52;
-    color: white;
-    padding: 20px;
-
-    display: flex;
-    flex-direction: column;
-    gap: 20px;
-}
-
-.sidebar h2 {
-    margin-bottom: 20px;
-}
-
-.sidebar a {
-    color: white;
-    text-decoration: none;
-    padding: 10px;
-    border-radius: 6px;
-}
-
-.sidebar a:hover {
-    background-color: rgba(255,255,255,0.1);
-}
-
-.logout {
-    margin-top: auto;
-    background-color: white;
-    color: #003d52 !important;
-    text-align: center;
-    font-weight: bold;
-}
-
-/* MAIN */
-.main {
-    flex: 1;
-    background-color: #f2f2f2;
-    padding: 30px;
-}
-
-/* TOP BAR */
 .topbar {
     margin-bottom: 30px;
 }
@@ -68,7 +11,6 @@
     color: #555;
 }
 
-/* CARDS */
 .cards {
     display: grid;
     grid-template-columns: repeat(3, 1fr);
@@ -80,7 +22,7 @@
     padding: 20px;
     border-radius: 12px;
 
-    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
+    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
 }
 
 .card h3 {
diff --git a/templates/dashboard.html b/templates/dashboard.html
index 2f974dc..7d9956d 100644
--- a/templates/dashboard.html
+++ b/templates/dashboard.html
@@ -1,60 +1,37 @@
-<!DOCTYPE html>
-<html lang="en">
-<head>
-    <meta charset="UTF-8">
-    <meta name="viewport" content="width=device-width, initial-scale=1.0">
-    <title>Dashboard</title>
+{% extends "layout.html" %}
 
-    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
-</head>
+{% block title %}
+Dashboard
+{% endblock %}
 
-<body>
+{% block css %}
+<link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
+{% endblock %}
 
-    <div class="layout">
+{% block content %}
 
-        <!-- SIDEBAR -->
-        <div class="sidebar">
-            <h2>PREFECTS</h2>
+<div class="topbar">
+    <h1>Dashboard</h1>
+    <p>Welcome {{ user.name }}</p>
+</div>
 
-            <a href="/dashboard">Dashboard</a>
-            <a href="/locker-duty">Locker Duty</a>
-            <a href="#">Notices</a>
-            <a href="#">Chat</a>
-            <a href="#">Assemblies</a>
+<div class="cards">
 
-            <a href="/logout" class="logout">Logout</a>
-        </div>
-
-        <!-- MAIN CONTENT -->
-        <div class="main">
-
-            <div class="topbar">
-                <h1>Dashboard</h1>
-                <p>Welcome {{ user.name }}</p>
-            </div>
-
-            <div class="cards">
-
-                <div class="card">
-                    <h3>Locker Duty</h3>
-                    <p>Next duty: Tomorrow</p>
-                </div>
-
-                <div class="card">
-                    <h3>Notices</h3>
-                    <p>3 new announcements</p>
-                </div>
-
-                <div class="card">
-                    <h3>Chat</h3>
-                    <p>Open discussions</p>
-                </div>
-
-            </div>
+    <div class="card">
+        <h3>Locker Duty</h3>
+        <p>Next duty: Tomorrow</p>
+    </div>
 
-        </div>
+    <div class="card">
+        <h3>Notices</h3>
+        <p>3 new announcements</p>
+    </div>
 
+    <div class="card">
+        <h3>Chat</h3>
+        <p>Open discussions</p>
     </div>
 
-</body>
-</html>
\ No newline at end of file
+</div>
+
+{% endblock %}
\ No newline at end of file

Commit: 4746225
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 00:05:32 2026 +1200
Message: added layout tempate
---
 static/css/layout.css | 66 +++++++++++++++++++++++++++++++++++++++++++++++++++
 templates/layout.html | 50 ++++++++++++++++++++++++++++++++++++++
 2 files changed, 116 insertions(+)

diff --git a/static/css/layout.css b/static/css/layout.css
new file mode 100644
index 0000000..bf9d15e
--- /dev/null
+++ b/static/css/layout.css
@@ -0,0 +1,66 @@
+* {
+    margin: 0;
+    padding: 0;
+    box-sizing: border-box;
+    font-family: Arial, Helvetica, sans-serif;
+}
+
+body {
+    background-color: #ececec;
+    color: #003d52;
+}
+
+.layout {
+    display: flex;
+    min-height: 100vh;
+}
+
+.sidebar {
+    width: 250px;
+    background-color: #003d52;
+    color: white;
+
+    padding: 20px;
+
+    display: flex;
+    flex-direction: column;
+    gap: 20px;
+}
+
+.sidebar h2 {
+    margin-bottom: 20px;
+}
+
+.sidebar a {
+    color: white;
+    text-decoration: none;
+
+    padding: 10px;
+
+    border-radius: 6px;
+
+    transition: 0.2s;
+}
+
+.sidebar a:hover {
+    background-color: rgba(255,255,255,0.1);
+}
+
+.sidebar .logout {
+    margin-top: auto;
+
+    background: white;
+    color: #003d52;
+
+    text-align: center;
+    font-weight: bold;
+}
+
+.sidebar .logout:hover {
+    background: #e5e5e5;
+}
+
+.main-content {
+    flex: 1;
+    padding: 40px;
+}
\ No newline at end of file
diff --git a/templates/layout.html b/templates/layout.html
new file mode 100644
index 0000000..2a172ae
--- /dev/null
+++ b/templates/layout.html
@@ -0,0 +1,50 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>
+        {% block title %}
+        PrefectConnect
+        {% endblock %}
+    </title>
+
+    <!-- CSS -->
+    <link rel="stylesheet" href="{{ url_for('static', filename='css/layout.css') }}">
+
+    <!-- Page-specific CSS -->
+    {% block css %}
+    {% endblock %}
+
+</head>
+<body>
+    <div class ="layout">
+
+        <!--Side Bar-->
+        <div class="sidebar">
+
+            <h2>PREFECTS</h2>
+
+            <a href="/dashboard">Dashboard</a>
+            <a href="/locker-duty">Locker Duty</a>
+            <a href="#">Notices</a>
+            <a href="#">Chat</a>
+            <a href="#">Assemblies</a>
+
+            <a href="/logout" class="logout">Logout</a>
+
+        </div>
+
+        <main class="main-content">
+
+            {% block content %}
+            {% endblock %}
+
+        </main>
+    </div>
+
+    {% block scripts %}
+    {% endblock %}
+
+</body>
+</html>
\ No newline at end of file

Commit: dfede8f
Author: BHS23113 <23113@burnside.school.nz>
Date: Mon Jul 20 00:05:12 2026 +1200
Message: fixed redirect url
---
 main.py | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)

diff --git a/main.py b/main.py
index f7a249d..4d0709e 100644
--- a/main.py
+++ b/main.py
@@ -30,7 +30,7 @@ def index():
 def dashboard():
 
     if "user" not in session:
-        return redirect("/")
+        return redirect(url_for("index"))
 
     return render_template(
         "dashboard.html",
@@ -112,7 +112,7 @@ def login():
 @app.route("/logout")
 def logout():
     session.clear()
-    return redirect("/")
+    return redirect(url_for("index"))
 
 
 if __name__ == "__main__":

Commit: a78c80d
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Jul 19 23:15:12 2026 +1200
Message: fixed css path
---
 templates/dashboard.html   | 2 +-
 templates/locker_duty.html | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)

diff --git a/templates/dashboard.html b/templates/dashboard.html
index 63434c6..2f974dc 100644
--- a/templates/dashboard.html
+++ b/templates/dashboard.html
@@ -5,7 +5,7 @@
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Dashboard</title>
 
-    <link rel="stylesheet" href="{{ url_for('static', filename='dashboard.css') }}">
+    <link rel="stylesheet" href="{{ url_for('static', filename='css/dashboard.css') }}">
 </head>
 
 <body>
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
index b3cdb28..e97e4c8 100644
--- a/templates/locker_duty.html
+++ b/templates/locker_duty.html
@@ -5,7 +5,7 @@
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Locker Duty</title>
 
-    <link rel="stylesheet" href="{{ url_for('static', filename='locker_duty.css') }}?v=2">
+    <link rel="stylesheet" href="{{ url_for('static', filename='css/locker_duty.css') }}?v=2">
 </head>
 
 <body>

Commit: 9d5a719
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Jul 19 23:13:27 2026 +1200
Message: deleted my db from github
---
 prefectconnect.db | Bin 40960 -> 0 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)

diff --git a/prefectconnect.db b/prefectconnect.db
deleted file mode 100644
index 28d731c..0000000
Binary files a/prefectconnect.db and /dev/null differ

Commit: 2d99620
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Jul 19 23:11:40 2026 +1200
Message: re orginisation
---
 logic.py => secret_key.py        | 0
 static/{ => css}/dashboard.css   | 0
 static/{ => css}/locker_duty.css | 0
 static/{ => css}/style.css       | 0
 4 files changed, 0 insertions(+), 0 deletions(-)

diff --git a/logic.py b/secret_key.py
similarity index 100%
rename from logic.py
rename to secret_key.py
diff --git a/static/dashboard.css b/static/css/dashboard.css
similarity index 100%
rename from static/dashboard.css
rename to static/css/dashboard.css
diff --git a/static/locker_duty.css b/static/css/locker_duty.css
similarity index 100%
rename from static/locker_duty.css
rename to static/css/locker_duty.css
diff --git a/static/style.css b/static/css/style.css
similarity index 100%
rename from static/style.css
rename to static/css/style.css

Commit: a9bc3a4
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Jul 19 23:10:40 2026 +1200
Message: removed hard coded google id
---
 main.py              | 9 +++++----
 templates/index.html | 6 ++----
 2 files changed, 7 insertions(+), 8 deletions(-)

diff --git a/main.py b/main.py
index 768a884..f7a249d 100644
--- a/main.py
+++ b/main.py
@@ -1,9 +1,10 @@
 from flask import Flask, render_template, request, jsonify, session, redirect, url_for
 from google.oauth2 import id_token
 from google.auth.transport import requests as grequests
+from dotenv import load_dotenv
 import sqlite3
 import os
-from dotenv import load_dotenv
+
 load_dotenv(override=True)
 
 DATABASE = "prefectconnect.db"
@@ -21,7 +22,7 @@ GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
 @app.route("/")
 def index():
     user = session.get("user")
-    return render_template("index.html", user=user)
+    return render_template("index.html", user=user, client_id=GOOGLE_CLIENT_ID)
 
 
 # DASHBOARD ROUTE
@@ -29,7 +30,7 @@ def index():
 def dashboard():
 
     if "user" not in session:
-        return redirect(url_for("index"))
+        return redirect("/")
 
     return render_template(
         "dashboard.html",
@@ -111,7 +112,7 @@ def login():
 @app.route("/logout")
 def logout():
     session.clear()
-    return redirect(url_for("index"))
+    return redirect("/")
 
 
 if __name__ == "__main__":
diff --git a/templates/index.html b/templates/index.html
index 8373cc7..e1e6d19 100644
--- a/templates/index.html
+++ b/templates/index.html
@@ -9,7 +9,7 @@
     <script src="https://accounts.google.com/gsi/client" async defer></script>
 
     <!-- CSS -->
-    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
+    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
 </head>
 
 <body>
@@ -31,8 +31,6 @@
 
                 <div class="user-info">
 
-                    <img src="{{ user.picture }}" width="100">
-
                     <p>Welcome {{ user['name'] }}</p><br>
 
                     <a href="/logout" class="logout-btn">
@@ -45,7 +43,7 @@
 
                 <!-- Google Login Setup -->
                 <div id="g_id_onload"
-                    data-client_id="689612344288-p5f54jmflbfeh3f12p0o4bpmns3t9k8f.apps.googleusercontent.com"
+                    data-client_id="{{ client_id }}"
                     data-callback="handleCredentialResponse">
                 </div>
 

Commit: 3fec7cb
Author: BHS23113 <23113@burnside.school.nz>
Date: Sun Jul 19 21:51:05 2026 +1200
Message: added locker duty page
---
 main.py                    |   9 ++-
 static/locker_duty.css     | 133 +++++++++++++++++++++++++++++++++++++++++++++
 static/style.css           |   2 +-
 templates/dashboard.html   |   4 +-
 templates/locker_duty.html |  78 ++++++++++++++++++++++++++
 5 files changed, 222 insertions(+), 4 deletions(-)

diff --git a/main.py b/main.py
index cf43b26..768a884 100644
--- a/main.py
+++ b/main.py
@@ -36,6 +36,13 @@ def dashboard():
         user=session["user"]
     )
 
+@app.route("/locker-duty")
+def locker_duty():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    return render_template("locker_duty.html", user=session["user"])
 
 @app.route("/login", methods=["POST"])
 def login():
@@ -100,7 +107,7 @@ def login():
             "message": str(e)
         }), 401
 
-#testing#
+
 @app.route("/logout")
 def logout():
     session.clear()
diff --git a/static/locker_duty.css b/static/locker_duty.css
new file mode 100644
index 0000000..22b1d7a
--- /dev/null
+++ b/static/locker_duty.css
@@ -0,0 +1,133 @@
+/* RESET */
+* {
+    margin: 0;
+    padding: 0;
+    box-sizing: border-box;
+    font-family: Arial, Helvetica, sans-serif;
+}
+
+/* BODY */
+body {
+    background-color: #ececec;
+    color: #003d52;
+}
+
+/* PAGE LAYOUT */
+.layout {
+    display: flex;
+    min-height: 100vh;
+}
+
+/* SIDEBAR */
+.sidebar {
+    width: 250px;
+    background-color: #003d52;
+    color: white;
+    padding: 20px;
+
+    display: flex;
+    flex-direction: column;
+    gap: 20px;
+}
+
+.sidebar h2 {
+    margin-bottom: 20px;
+}
+
+/* SIDEBAR LINKS */
+.sidebar a {
+    color: white;
+    text-decoration: none;
+    padding: 10px;
+    border-radius: 6px;
+    transition: 0.2s;
+}
+
+.sidebar a:hover {
+    background-color: rgba(255,255,255,0.1);
+}
+
+/* LOGOUT BUTTON */
+.sidebar .logout {
+    margin-top: auto;
+    background-color: white;
+    color: #003d52;
+    text-align: center;
+    font-weight: bold;
+}
+
+.sidebar .logout:hover {
+    background-color: #e5e5e5;
+}
+
+/* MAIN CONTENT */
+.main-content {
+    flex: 1;
+    padding: 40px;
+}
+
+/* PAGE TITLE */
+.main-content h1 {
+    color: #003d52;
+    margin-bottom: 10px;
+    font-size: 2.2rem;
+}
+
+/* DESCRIPTION */
+.main-content p {
+    color: #555;
+    margin-bottom: 30px;
+    line-height: 1.5;
+}
+
+/* WEEK CARDS LAYOUT */
+.container {
+    display: flex;
+    gap: 30px;
+}
+
+/* WEEK CARD */
+.week {
+    flex: 1;
+    background: white;
+    border-radius: 12px;
+    padding: 20px;
+    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
+}
+
+/* WEEK TITLE */
+.week h2 {
+    background-color: #003d52;
+    color: white;
+    text-align: center;
+    padding: 12px;
+    border-radius: 8px;
+    margin-bottom: 20px;
+}
+
+/* TABLE */
+table {
+    width: 100%;
+    border-collapse: collapse;
+}
+
+/* TABLE HEADERS */
+th {
+    background-color: #f5f5f5;
+    color: #003d52;
+    text-align: left;
+    padding: 12px;
+    border-bottom: 2px solid #ddd;
+}
+
+/* TABLE CELLS */
+td {
+    padding: 12px;
+    border-bottom: 1px solid #eee;
+    color: #333;
+}
+
+/* HOVER EFFECT */
+tr:hover td {
+    background-color: #f7f7f7;
+}
\ No newline at end of file
diff --git a/static/style.css b/static/style.css
index 3ee8807..e1c69cb 100644
--- a/static/style.css
+++ b/static/style.css
@@ -95,4 +95,4 @@ body {
 
     text-decoration: none;
     font-weight: bold;
-}
\ No newline at end of file
+}. 
\ No newline at end of file
diff --git a/templates/dashboard.html b/templates/dashboard.html
index 98aa1d0..63434c6 100644
--- a/templates/dashboard.html
+++ b/templates/dashboard.html
@@ -16,8 +16,8 @@
         <div class="sidebar">
             <h2>PREFECTS</h2>
 
-            <a href="#">Dashboard</a>
-            <a href="#">Locker Duty</a>
+            <a href="/dashboard">Dashboard</a>
+            <a href="/locker-duty">Locker Duty</a>
             <a href="#">Notices</a>
             <a href="#">Chat</a>
             <a href="#">Assemblies</a>
diff --git a/templates/locker_duty.html b/templates/locker_duty.html
new file mode 100644
index 0000000..b3cdb28
--- /dev/null
+++ b/templates/locker_duty.html
@@ -0,0 +1,78 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>Locker Duty</title>
+
+    <link rel="stylesheet" href="{{ url_for('static', filename='locker_duty.css') }}?v=2">
+</head>
+
+<body>
+    <div class="layout">
+        <div class="sidebar">
+            <h2>PREFECTS</h2>
+
+            <a href="/dashboard">Dashboard</a>
+            <a href="/locker-duty">Locker Duty</a>
+            <a href="#">Notices</a>
+            <a href="#">Chat</a>
+            <a href="#">Assemblies</a>
+
+            <a href="/logout" class="logout">Logout</a>
+        </div>
+        <div class="main-content">
+            <!-- PAGE TITLE -->
+            <h1>Locker Duty Roster</h1>
+
+            <p>
+                Lock the side doors on arrival - there will be staff on duty to assist.<br>
+                Monitor student behaviour.
+            </p>
+
+            <!-- MAIN CONTAINER -->
+            <div class="container">
+
+                <!-- WEEK A -->
+                <div class="week">
+                    <h2>WEEK A</h2>
+
+                    <table>
+                        <tr>
+                            <th>Day</th>
+                            <th>Students</th>
+                        </tr>
+
+                        <tr><td>Monday</td><td>Elizabeth, Rosie</td></tr>
+                        <tr><td>Tuesday</td><td>Barnaby, Samuel</td></tr>
+                        <tr><td>Wednesday</td><td>Ava, Dasha</td></tr>
+                        <tr><td>Thursday</td><td>Sione, Michaela</td></tr>
+                        <tr><td>Friday</td><td>James, Luke</td></tr>
+
+                    </table>
+                </div>
+
+                <!-- WEEK B -->
+                <div class="week">
+                    <h2>WEEK B</h2>
+
+                    <table>
+                        <tr>
+                            <th>Day</th>
+                            <th>Students</th>
+                        </tr>
+
+                        <tr><td>Monday</td><td>Zoe, Chloe</td></tr>
+                        <tr><td>Tuesday</td><td>Kanon, Ida</td></tr>
+                        <tr><td>Wednesday</td><td>Lukas, Messi</td></tr>
+                        <tr><td>Thursday</td><td>Sho, Aaron</td></tr>
+                        <tr><td>Friday</td><td>Eason, Nilana</td></tr>
+
+                    </table>
+                </div>
+
+            </div>
+        </div>
+    </div>
+</body>
+</html>
\ No newline at end of file

Commit: a8cb8d0
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 16 17:16:22 2026 +1200
Message: security fix
---
 logic.py | 2 ++
 main.py  | 8 +++++---
 2 files changed, 7 insertions(+), 3 deletions(-)

diff --git a/logic.py b/logic.py
new file mode 100644
index 0000000..43edf8c
--- /dev/null
+++ b/logic.py
@@ -0,0 +1,2 @@
+import secrets
+print(secrets.token_hex(32))
\ No newline at end of file
diff --git a/main.py b/main.py
index babc8a3..cf43b26 100644
--- a/main.py
+++ b/main.py
@@ -2,6 +2,9 @@ from flask import Flask, render_template, request, jsonify, session, redirect, u
 from google.oauth2 import id_token
 from google.auth.transport import requests as grequests
 import sqlite3
+import os
+from dotenv import load_dotenv
+load_dotenv(override=True)
 
 DATABASE = "prefectconnect.db"
 
@@ -11,9 +14,8 @@ def get_db():
     return conn
 
 app = Flask(__name__)
-app.secret_key = "super_secret_key"  
-
-GOOGLE_CLIENT_ID = "689612344288-p5f54jmflbfeh3f12p0o4bpmns3t9k8f.apps.googleusercontent.com"
+app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
+GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
 
 
 @app.route("/")

Commit: e180cfd
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 16 17:16:05 2026 +1200
Message: deleted env
---
 .env | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

diff --git a/.env b/.env
deleted file mode 100644
index e69de29..0000000

Commit: 3487cb1
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 16 17:04:22 2026 +1200
Message: secutrity
---
 .env       | 0
 .gitignore | 6 ++++++
 2 files changed, 6 insertions(+)

diff --git a/.env b/.env
new file mode 100644
index 0000000..e69de29
diff --git a/.gitignore b/.gitignore
new file mode 100644
index 0000000..3ef1e0e
--- /dev/null
+++ b/.gitignore
@@ -0,0 +1,6 @@
+/.vscode
+/.vs
+/bin
+.env
+*.db
+*.exe
\ No newline at end of file

Commit: 514a568
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 16 16:53:04 2026 +1200
Message: test
---
 main.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/main.py b/main.py
index 4bc4718..babc8a3 100644
--- a/main.py
+++ b/main.py
@@ -98,7 +98,7 @@ def login():
             "message": str(e)
         }), 401
 
-
+#testing#
 @app.route("/logout")
 def logout():
     session.clear()

Commit: e0287cf
Author: BHS23113 <23113@burnside.school.nz>
Date: Thu Jul 16 16:40:23 2026 +1200
Message: initializing
---
 db.py                    |  86 +++++++++++++++++++++++++++++++++++++
 main.py                  | 109 +++++++++++++++++++++++++++++++++++++++++++++++
 prefectconnect.db        | Bin 0 -> 40960 bytes
 static/dashboard.css     |  89 ++++++++++++++++++++++++++++++++++++++
 static/script.js         |  23 ++++++++++
 static/style.css         |  98 ++++++++++++++++++++++++++++++++++++++++++
 templates/dashboard.html |  60 ++++++++++++++++++++++++++
 templates/index.html     |  76 +++++++++++++++++++++++++++++++++
 8 files changed, 541 insertions(+)

diff --git a/db.py b/db.py
new file mode 100644
index 0000000..f5cadbc
--- /dev/null
+++ b/db.py
@@ -0,0 +1,86 @@
+import sqlite3
+
+connection = sqlite3.connect("prefectconnect.db")
+cursor = connection.cursor()
+
+# USERS TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS users (
+    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    email TEXT NOT NULL UNIQUE,
+    name TEXT NOT NULL,
+    role TEXT NOT NULL,
+    is_active BOOLEAN NOT NULL DEFAULT 1
+)
+""")
+
+# LOCKER DUTY TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS locker_duty (
+    duty_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    user_id INTEGER NOT NULL,
+    duty_date DATE NOT NULL,
+    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
+)
+""")
+
+# MESSAGE POST TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS message_post (
+    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    user_id INTEGER NOT NULL,
+    content TEXT NOT NULL,
+    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
+    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
+)
+""")
+
+# NOTICE TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS notice (
+    notice_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    title TEXT NOT NULL,
+    content TEXT NOT NULL,
+    created_by INTEGER NOT NULL,
+    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
+    is_active BOOLEAN NOT NULL DEFAULT 1,
+    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE CASCADE
+)
+""")
+
+# ASSEMBLY TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS assembly (
+    assembly_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    title TEXT NOT NULL,
+    date DATE NOT NULL
+)
+""")
+
+# ASSEMBLY IDEA TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS assembly_idea (
+    idea_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    assembly_id INTEGER NOT NULL,
+    content TEXT NOT NULL,
+    updated_by INTEGER NOT NULL,
+    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE,
+    FOREIGN KEY (updated_by) REFERENCES users(user_id) ON DELETE CASCADE
+)
+""")
+
+# RUN SHEET TABLE
+cursor.execute("""
+CREATE TABLE IF NOT EXISTS run_sheet (
+    runsheet_id INTEGER PRIMARY KEY AUTOINCREMENT,
+    assembly_id INTEGER NOT NULL,
+    content TEXT NOT NULL,
+    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
+    FOREIGN KEY (assembly_id) REFERENCES assembly(assembly_id) ON DELETE CASCADE
+)
+""")
+
+connection.commit()
+connection.close()
+
+print("✅ PrefectConnect database created successfully!")
\ No newline at end of file
diff --git a/main.py b/main.py
new file mode 100644
index 0000000..4bc4718
--- /dev/null
+++ b/main.py
@@ -0,0 +1,109 @@
+from flask import Flask, render_template, request, jsonify, session, redirect, url_for
+from google.oauth2 import id_token
+from google.auth.transport import requests as grequests
+import sqlite3
+
+DATABASE = "prefectconnect.db"
+
+def get_db():
+    conn = sqlite3.connect(DATABASE)
+    conn.row_factory = sqlite3.Row
+    return conn
+
+app = Flask(__name__)
+app.secret_key = "super_secret_key"  
+
+GOOGLE_CLIENT_ID = "689612344288-p5f54jmflbfeh3f12p0o4bpmns3t9k8f.apps.googleusercontent.com"
+
+
+@app.route("/")
+def index():
+    user = session.get("user")
+    return render_template("index.html", user=user)
+
+
+# DASHBOARD ROUTE
+@app.route("/dashboard")
+def dashboard():
+
+    if "user" not in session:
+        return redirect(url_for("index"))
+
+    return render_template(
+        "dashboard.html",
+        user=session["user"]
+    )
+
+
+@app.route("/login", methods=["POST"])
+def login():
+
+    token = request.json.get("credential")
+
+    try:
+        idinfo = id_token.verify_oauth2_token(
+            token,
+            grequests.Request(),
+            GOOGLE_CLIENT_ID
+        )
+
+        google_id = idinfo["sub"]
+        email = idinfo["email"]
+        name = idinfo.get("name")
+
+        db = get_db()
+        cursor = db.cursor()
+
+        # Check if user exists
+        cursor.execute(
+            "SELECT * FROM users WHERE email=?",
+            (email,)
+        )
+
+        user = cursor.fetchone()
+
+        # Create user if first login
+        if user is None:
+            cursor.execute("""
+                INSERT INTO users (email, name, role)
+                VALUES (?, ?, ?)
+            """, (email, name, "prefect"))
+
+            db.commit()
+
+            cursor.execute(
+                "SELECT * FROM users WHERE email=?",
+                (email,)
+            )
+            user = cursor.fetchone()
+
+        # Store DB user in session
+        session["user"] = {
+            "user_id": user["user_id"],
+            "email": user["email"],
+            "name": user["name"]
+        }
+
+        db.close()
+
+        # UPDATED RESPONSE
+        return jsonify({
+            "status": "success",
+            "redirect": "/dashboard"
+        })
+
+    except Exception as e:
+        return jsonify({
+            "status": "error",
+            "message": str(e)
+        }), 401
+
+
+@app.route("/logout")
+def logout():
+    session.clear()
+    return redirect(url_for("index"))
+
+
+if __name__ == "__main__":
+    app.run(debug=True)
\ No newline at end of file
diff --git a/prefectconnect.db b/prefectconnect.db
new file mode 100644
index 0000000..28d731c
Binary files /dev/null and b/prefectconnect.db differ
diff --git a/static/dashboard.css b/static/dashboard.css
new file mode 100644
index 0000000..87045ba
--- /dev/null
+++ b/static/dashboard.css
@@ -0,0 +1,89 @@
+/* RESET */
+* {
+    margin: 0;
+    padding: 0;
+    box-sizing: border-box;
+    font-family: Arial, Helvetica, sans-serif;
+}
+
+/* LAYOUT */
+.layout {
+    display: flex;
+    min-height: 100vh;
+}
+
+/* SIDEBAR */
+.sidebar {
+    width: 250px;
+    background-color: #003d52;
+    color: white;
+    padding: 20px;
+
+    display: flex;
+    flex-direction: column;
+    gap: 20px;
+}
+
+.sidebar h2 {
+    margin-bottom: 20px;
+}
+
+.sidebar a {
+    color: white;
+    text-decoration: none;
+    padding: 10px;
+    border-radius: 6px;
+}
+
+.sidebar a:hover {
+    background-color: rgba(255,255,255,0.1);
+}
+
+.logout {
+    margin-top: auto;
+    background-color: white;
+    color: #003d52 !important;
+    text-align: center;
+    font-weight: bold;
+}
+
+/* MAIN */
+.main {
+    flex: 1;
+    background-color: #f2f2f2;
+    padding: 30px;
+}
+
+/* TOP BAR */
+.topbar {
+    margin-bottom: 30px;
+}
+
+.topbar h1 {
+    font-size: 2.5rem;
+    color: #003d52;
+}
+
+.topbar p {
+    color: #555;
+}
+
+/* CARDS */
+.cards {
+    display: grid;
+    grid-template-columns: repeat(3, 1fr);
+    gap: 20px;
+}
+
+.card {
+    background: white;
+    padding: 20px;
+    border-radius: 12px;
+
+    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
+}
+
+.card h3 {
+    margin-bottom: 10px;
+    color: #003d52;
+}
\ No newline at end of file
diff --git a/static/script.js b/static/script.js
new file mode 100644
index 0000000..195f8d6
--- /dev/null
+++ b/static/script.js
@@ -0,0 +1,23 @@
+function handleCredentialResponse(response) {
+    console.log("TOKEN:", response.credential);
+
+    fetch("/login", {
+        method: "POST",
+        headers: {
+            "Content-Type": "application/json"
+        },
+        body: JSON.stringify({
+            credential: response.credential
+        })
+    })
+    .then(res => res.json())
+    .then(data => {
+        console.log("SERVER RESPONSE:", data);
+
+        if (data.status === "success") {
+            window.location.href = data.redirect;
+        } else {
+            alert("Login failed");
+        }
+    });
+}
\ No newline at end of file
diff --git a/static/style.css b/static/style.css
new file mode 100644
index 0000000..3ee8807
--- /dev/null
+++ b/static/style.css
@@ -0,0 +1,98 @@
+/* RESET */
+* {
+    margin: 0;
+    padding: 0;
+    box-sizing: border-box;
+}
+
+/* BODY */
+body {
+    font-family: Arial, Helvetica, sans-serif;
+    background-color: #ececec;
+    color: white;
+    min-height: 100vh;
+}
+
+/* NAVBAR */
+.navbar {
+    background-color: #003d52;
+    height: 100px;
+
+    display: flex;
+    justify-content: space-between;
+    align-items: center;
+
+    padding: 0 50px;
+}
+
+.logo {
+    font-size: 2rem;
+    font-weight: bold;
+}
+
+.nav-login {
+    color: white;
+    text-decoration: none;
+    font-size: 1.7rem;
+    font-weight: bold;
+}
+
+/* MAIN SECTION */
+.main-container {
+    display: flex;
+    justify-content: center;
+    align-items: center;
+
+    padding-top: 80px;
+}
+
+/* LOGIN CARD */
+.login-card {
+    background-color: #003d52;
+
+    width: 650px;
+    height: 700px;
+
+    display: flex;
+    flex-direction: column;
+    align-items: center;
+
+    padding-top: 100px;
+}
+
+.login-card h2 {
+    font-size: 4rem;
+    margin-bottom: 140px;
+}
+
+/* GOOGLE BUTTON */
+.google-btn-wrapper {
+    transform: scale(1.6);
+}
+
+/* USER INFO */
+.user-info {
+    text-align: center;
+}
+
+.user-info img {
+    border-radius: 50%;
+    margin-bottom: 20px;
+}
+
+.user-info p {
+    margin-bottom: 20px;
+    font-size: 1.4rem;
+}
+
+/* LOGOUT BUTTON */
+.logout-btn {
+    background-color: white;
+    color: #003d52;
+
+    padding: 12px 24px;
+    border-radius: 5px;
+
+    text-decoration: none;
+    font-weight: bold;
+}
\ No newline at end of file
diff --git a/templates/dashboard.html b/templates/dashboard.html
new file mode 100644
index 0000000..98aa1d0
--- /dev/null
+++ b/templates/dashboard.html
@@ -0,0 +1,60 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>Dashboard</title>
+
+    <link rel="stylesheet" href="{{ url_for('static', filename='dashboard.css') }}">
+</head>
+
+<body>
+
+    <div class="layout">
+
+        <!-- SIDEBAR -->
+        <div class="sidebar">
+            <h2>PREFECTS</h2>
+
+            <a href="#">Dashboard</a>
+            <a href="#">Locker Duty</a>
+            <a href="#">Notices</a>
+            <a href="#">Chat</a>
+            <a href="#">Assemblies</a>
+
+            <a href="/logout" class="logout">Logout</a>
+        </div>
+
+        <!-- MAIN CONTENT -->
+        <div class="main">
+
+            <div class="topbar">
+                <h1>Dashboard</h1>
+                <p>Welcome {{ user.name }}</p>
+            </div>
+
+            <div class="cards">
+
+                <div class="card">
+                    <h3>Locker Duty</h3>
+                    <p>Next duty: Tomorrow</p>
+                </div>
+
+                <div class="card">
+                    <h3>Notices</h3>
+                    <p>3 new announcements</p>
+                </div>
+
+                <div class="card">
+                    <h3>Chat</h3>
+                    <p>Open discussions</p>
+                </div>
+
+            </div>
+
+        </div>
+
+    </div>
+
+</body>
+</html>
\ No newline at end of file
diff --git a/templates/index.html b/templates/index.html
new file mode 100644
index 0000000..8373cc7
--- /dev/null
+++ b/templates/index.html
@@ -0,0 +1,76 @@
+<!DOCTYPE html>
+<html lang="en">
+<head>
+    <meta charset="UTF-8">
+    <meta name="viewport" content="width=device-width, initial-scale=1.0">
+    <title>Prefects BHS</title>
+
+    <!-- Google Sign In -->
+    <script src="https://accounts.google.com/gsi/client" async defer></script>
+
+    <!-- CSS -->
+    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
+</head>
+
+<body>
+
+    <!-- NAVBAR -->
+    <header class="navbar">
+        <h1 class="logo">PREFECTS BHS</h1>
+        <a href="#" class="nav-login">LOG IN</a>
+    </header>
+
+    <!-- MAIN LOGIN CARD -->
+    <main class="main-container">
+
+        <div class="login-card">
+
+            <h2>LOG IN</h2>
+
+            {% if user %}
+
+                <div class="user-info">
+
+                    <img src="{{ user.picture }}" width="100">
+
+                    <p>Welcome {{ user['name'] }}</p><br>
+
+                    <a href="/logout" class="logout-btn">
+                        Logout
+                    </a>
+
+                </div>
+
+            {% else %}
+
+                <!-- Google Login Setup -->
+                <div id="g_id_onload"
+                    data-client_id="689612344288-p5f54jmflbfeh3f12p0o4bpmns3t9k8f.apps.googleusercontent.com"
+                    data-callback="handleCredentialResponse">
+                </div>
+
+                <!-- Google Login Button -->
+                <div class="google-btn-wrapper">
+
+                    <div class="g_id_signin"
+                        data-type="standard"
+                        data-theme="filled_blue"
+                        data-size="large"
+                        data-text="signin_with"
+                        data-shape="rectangular"
+                        data-width="300">
+                    </div>
+
+                </div>
+
+            {% endif %}
+
+        </div>
+
+    </main>
+
+    <!-- JS -->
+    <script src="{{ url_for('static', filename='script.js') }}"></script>
+
+</body>
+</html>
\ No newline at end of file
