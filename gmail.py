import os
import base64
from email.message import EmailMessage

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


SCOPES = [
    "https://www.googleapis.com/auth/gmail.send"
]

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


def create_flow():

    flow = Flow.from_client_config(
        CLIENT_CONFIG,
        scopes=SCOPES
    )

    flow.redirect_uri = "http://localhost:5000/gmail/callback"

    return flow


def send_email(to_email, subject, body):

    token_file = "gmail_token.json"

    if not os.path.exists(token_file):
        raise Exception("Gmail has not been connected yet.")

    from google.oauth2.credentials import Credentials

    credentials = Credentials.from_authorized_user_file(
        token_file,
        SCOPES
    )

    if credentials.expired and credentials.refresh_token:

        credentials.refresh(Request())

        with open(token_file, "w") as token:
            token.write(credentials.to_json())

    service = build(
        "gmail",
        "v1",
        credentials=credentials
    )

    message = EmailMessage()

    message["To"] = to_email
    message["Subject"] = subject

    message.set_content(body)

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    message_body = {
        "raw": encoded_message
    }

    service.users().messages().send(
        userId="me",
        body=message_body
    ).execute()