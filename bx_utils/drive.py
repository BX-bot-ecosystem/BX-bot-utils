from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from dotenv import load_dotenv
from googleapiclient.http import MediaFileUpload
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
    credentials = credentials.with_scopes(SCOPES)
    # Create the Calendar API client using the service account credentials.
    service = build("drive", "v3", credentials=credentials)
    return service

def get_files(folder_id):
    service = get_drive_service()
    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                   fields="files(id, name, mimeType)").execute()
    files = results.get('files', [])
    return files

def upload_image(image_path, folder_id):
    service = get_drive_service()

    # Prepare the media file upload
    media = MediaFileUpload(image_path, mimetype='image/jpeg')
    file_metadata = {
        'name': os.path.basename(image_path),
        'parents': [folder_id]
    }

    # Upload the image
    uploaded_file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Image uploaded. File ID: {uploaded_file['id']}")

def create_folder(name, parent_id):
    service = get_drive_service()

    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }

    created_folder = service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()

    print(f"Folder '{name}' created. Folder ID: {created_folder['id']}")

def create_committee_folder(committee_name):
    create_folder(committee_name, os.getenv("DRIVE_FOLDER"))

def get_folders(folder_id):
    service = get_drive_service()
    results = service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                   fields="files(id, name, mimeType)").execute()
    files = results.get('files', [])
    folders = [file for file in files if file['mimeType']=='application/vnd.google-apps.folder']
    return folders

def add_committee_files(committee_name, file_path):
    service = get_drive_service()
    folders = get_folders(os.getenv("DRIVE_FOLDER"))
    committees_folders = {file["name"]: file["id"] for file in folders}
    if not committee_name in committees_folders.keys():
        create_committee_folder(committee_name)
        folders = get_folders(os.getenv("DRIVE_FOLDER"))
        committees_folders = {file["name"]: file["id"] for file in folders}
    folder_id = committees_folders[committee_name]
    upload_image(file_path, folder_id)

def get_committee_files(committee_name):
    service = get_drive_service()
    folders = get_folders(os.getenv("DRIVE_FOLDER"))
    committee_folders = {file["name"]: file["id"] for file in folders}
    if not committee_name in committee_folders.keys():
        return []
    return get_files(committee_folders[committee_name])
def download_committee_files(committee_name, file_name, file_path):
    files = get_committee_files(committee_name)
    file_to_download = [file for file in files if file["name"] == file_name][0]
    file_to_download.


