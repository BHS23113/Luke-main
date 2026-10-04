# PrefectConnect

PrefectConnect is a web-based system designed to help manage school prefects. It allows administrators to manage users, assign locker duties, post notices, and manage other prefect information from one place.

## Features

* Google account login
* User and role management
* Admin and prefect permissions
* Locker duty scheduling
* Automatic Gmail locker-duty reminders
* Noticeboard
* Notice read tracking
* Assembly management
* Week A / Week B school-week calculation
* Dashboard showing important information
* SQLite database

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* Google OAuth
* Gmail API
* APScheduler

## Project Structure

```text
PrefectConnect/
│
├── main.py
├── gmail.py
├── prefectconnect.db
├── requirements.txt
├── .env
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── dashboard.html
│   ├── users.html
│   ├── locker_duty.html
│   ├── notices.html
│   └── ...
│
└── static/
    ├── css/
    └── script.js
```

## Running the Project

### 1. Install Python

Python 3 is required.

### 2. Install the required packages

Open a terminal in the project folder and run:

```bash
python3 -m pip install -r requirements.txt
```

### 3. Create the `.env` file

The `.env` file is **not included in the GitHub repository** because it contains private credentials.

Create a new file named:

```text
.env
```

in the main PrefectConnect folder.

Add:

```text
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
SECRET_KEY=your-secret-key
```

The actual values must be provided separately and should **not** be uploaded to GitHub.

### 4. Configure Google OAuth

PrefectConnect uses Google OAuth for login.

The Google OAuth client needs to be configured for local development.

In Google Cloud, use a **Web application** OAuth client and add:

```text
http://localhost
http://localhost:5000
```

under **Authorized JavaScript origins**.

The redirect URI used by the Gmail authorisation system is:

```text
http://localhost:5000/gmail/callback
```

This also needs to be listed under the OAuth client's **Authorized redirect URIs**.

Google requires the redirect URI used by the application to exactly match an authorized redirect URI.

### 5. Run the application

From the project folder, run:

```bash
python3 main.py
```

The application should start at:

```text
http://localhost:5000
```

Open this address in a web browser.

## Setting Up the Project on Another Computer

The GitHub repository does not contain the `.env` file or other private credentials.

This is intentional. The `.env` file contains sensitive Google OAuth information and should not be committed to GitHub.

When setting up PrefectConnect on another computer:

1. Download or clone the repository.
2. Install the required Python packages.
3. Create a new `.env` file in the project folder.
4. Add the required Google OAuth credentials.
5. Make sure the Google OAuth client allows `http://localhost:5000`.
6. Run `python3 main.py`.
7. Open `http://localhost:5000` in a browser.

The computer running the application has its own `localhost`. For example, if the teacher runs PrefectConnect on their computer, `localhost:5000` refers to **their computer**, not the original development computer.

Google supports localhost for development, but the relevant localhost origin and port need to be configured in the OAuth client.

## Gmail Reminders

PrefectConnect can automatically send locker-duty reminder emails using the Gmail API.

The application uses APScheduler to run the reminder system on school days.

The system:

1. Finds the next school day.
2. Determines whether it is Week A or Week B.
3. Finds users assigned to locker duty.
4. Checks whether a reminder has already been sent.
5. Sends the reminder email.
6. Records the reminder in the `reminder_log` table.

The reminder log prevents the same user from receiving duplicate reminders for the same duty date.

The Flask application must be running for the scheduled reminders to run.

## User Roles

### Prefect

Prefects can access the main prefect features of the application, such as:

* Dashboard
* Locker duty
* Notices
* Other features available to normal users

### Admin

Administrators have additional permissions, including:

* Adding users
* Removing users
* Changing user roles
* Adding locker-duty assignments
* Removing locker-duty assignments
* Creating notices
* Removing notices

Administrators cannot delete their own account or remove their own admin privileges.

## Database

PrefectConnect uses SQLite.

The main database tables are:

### `users`

Stores prefect accounts and their roles.

### `locker_duty`

Stores locker-duty assignments, including the assigned user, school week, and day.

### `reminder_log`

Stores when locker-duty reminders have been sent.

### `notice`

Stores notices displayed to users.

### `notice_read`

Stores which users have read which notices.

## Security

Private credentials should not be committed to GitHub.

The following files should remain private:

```text
.env
gmail_token.json
```

The `.env` file contains Google OAuth credentials and the Flask secret key.

`gmail_token.json` contains the OAuth credentials used to send Gmail messages.

Google recommends keeping OAuth client secrets outside publicly accessible source code and outside repositories such as GitHub.

## Development

PrefectConnect was developed and tested using a local Flask development server.

The current development address is:

```text
http://localhost:5000
```

The application is currently intended for local development and school project demonstration rather than public production use.

## Troubleshooting

### Login gives a 401 error

Check that:

* The `.env` file exists.
* `GOOGLE_CLIENT_ID` is set correctly.
* The Google OAuth client is configured for `http://localhost:5000`.
* The application is being accessed through `http://localhost:5000`.
* The computer's date and time are correct.

### Gmail reminders do not send

Check that:

* The Flask application is running.
* Gmail has been authorised.
* `gmail_token.json` exists.
* The locker-duty assignment is for the correct school week and day.

### Missing Python packages

Run:

```bash
python3 -m pip install -r requirements.txt
```
