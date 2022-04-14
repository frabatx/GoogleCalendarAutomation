from os import path
import pickle
from google.auth.transport.requests import Request
from google_auto_oauthlib.flow import InstalledAppFlow

SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
        ]

def get_credentials_google():
    InstalledAppFlow.from_client_secrets_file("google-credentials.json")
