from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive.file']
def get_drive_service():
    # Load the service account credentials from the JSON key file.
    account_info = {
        "type": "service_account",
        "project_id": "bx-telegram",
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": "googleapis.com"
        }
    credentials = Credentials.from_service_account_info(account_info)
    credentials.with_scopes(SCOPES)
    # Create the Calendar API client using the service account credentials.
    service = build("drive", "v3", credentials=credentials)
    return service

