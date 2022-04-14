from os import path
import pickle
from google.auth.transport.requests import Request
from google_auto_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
        ]

def get_credentials_google():
    flow = InstalledAppFlow.from_client_secrets_file("google-credentials.json")
    creds = flow.run_local_server(port = 80)

    pickle.dump(creds, open('tocken.txt', 'wb'))
    return creds

def get_calendar_service():
    creds = None
    if path.exists('tocken.txt'):
        creds = pickle.load(open('tocken.txt', 'rb'))
    # If expired, refresh credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_tocken:
            creds.refresh(Request())
        else:
            creds = get_credentials_google()
    service = build('calendar', 'v3', credentials = creds)
    return service
