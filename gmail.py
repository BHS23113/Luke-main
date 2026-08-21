import os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

import base64
from email.message import EmailMessage
from email.utils import parseaddr

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


# Gmail permission required to send emails
SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]


# Google OAuth configuration
CLIENT_CONFIG = {
    "web": {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": [
            "http://localhost:5000/gmail/callback"
        ]
    }
}


# Creates the Google OAuth authentication flow
def create_flow():

    print("GMAIL CLIENT ID LOADED:", bool(os.getenv("GOOGLE_CLIENT_ID")))
    print("GMAIL CLIENT SECRET LOADED:", bool(os.getenv("GOOGLE_CLIENT_SECRET")))

    flow = Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=SCOPES
    )

    flow.redirect_uri = "http://localhost:5000/gmail/callback"

    print("GMAIL REDIRECT URI:", flow.redirect_uri)

    return flow


# Sends an email through the connected Gmail account
def send_email(to_email, subject, body):

    # Extract the actual email address from the recipient
    name, address = parseaddr(to_email)

    if not address or "@" not in address:
        raise ValueError(f"Invalid recipient email address: {to_email}")

    # Load the saved Gmail OAuth credentials
    token_file = "gmail_token.json"

    if not os.path.exists(token_file):
        raise Exception("Gmail has not been connected yet.")

    from google.oauth2.credentials import Credentials

    credentials = Credentials.from_authorized_user_file(
        token_file,
        SCOPES
    )

    # Refresh the access token if it has expired
    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

        with open(token_file, "w") as token:
            token.write(credentials.to_json())

    # Connect to the Gmail API
    service = build(
        "gmail",
        "v1",
        credentials=credentials
    )

    # Create the email
    message = EmailMessage()

    message["To"] = address
    message["Subject"] = subject
    message.set_content(body)

    # Gmail API requires the email to be Base64 encoded
    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    message_body = {
        "raw": encoded_message
    }

    # Send the email
    service.users().messages().send(
        userId="me",
        body=message_body
    ).execute()