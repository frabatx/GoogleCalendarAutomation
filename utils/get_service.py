from os import path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
        ]

def get_credentials_google():
    flow = InstalledAppFlow.from_client_secrets_file("google-credentials.json", SCOPES)

    creds = flow.run_local_server(port = 80)

    pickle.dump(creds, open('token.txt', 'wb'))
    return creds

def get_calendar_service():
    creds = None
    if path.exists('token.txt'):
        creds = pickle.load(open('token.txt', 'rb'))
        print("token exist")
    # If expired, refresh credentials
    if not creds or not creds.valid:
        print('credentials not valid')
        if creds and creds.expired and creds.refresh_token:
            print(f"are_credsexpired? {creds.expired}")
            creds.refresh(Request())
            print("refresh creds")
        else:
            creds = get_credentials_google()
            print(f'get_credential because not valid: {creds}')
    service = build('calendar', 'v3', credentials = creds)
    return service
