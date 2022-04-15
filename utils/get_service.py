from os import path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import google.oauth2.credentials
import google_auth_oauthlib.flow

SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
        ]

def get_credentials_google():
    flow = InstalledAppFlow.from_client_secrets_file("google-credentials.json", SCOPES)

    creds = flow.run_local_server(port = 80)

    pickle.dump(creds, open('token.txt', 'wb'))
    return creds

def get_credentials_google_heroku():
    

    # Use the client_secret.json file to identify the application requesting
    # authorization. The client ID (from that file) and access scopes are required.
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])

    # Indicate where the API server will redirect the user after the user completes
    # the authorization flow. The redirect URI is required. The value must exactly
    # match one of the authorized redirect URIs for the OAuth 2.0 client, which you
    # configured in the API Console. If this value doesn't match an authorized URI,
    # you will get a 'redirect_uri_mismatch' error.
    flow.redirect_uri = 'https://cus-calendar.herokuapp.com'

    # Generate URL for request to Google's OAuth 2.0 server.
    # Use kwargs to set optional request parameters.
    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

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
            creds = get_credentials_google_heroku()
            print(f'get_credential because not valid: {creds}')
    service = build('calendar', 'v3', credentials = creds)
    return service
