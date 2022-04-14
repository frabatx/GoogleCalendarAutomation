#!/usr/bin/env python
from typing import Optional
from fastapi import FastAPI, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn
from pprint import pprint
from Google import Create_Service

# Costants
CLIENT_SECRET_FILE = 'google-credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_app() -> FastAPI:
  """
  Costruttore oggetto FastAPI e settaggi environment
  """
  # Creazione oggetto API
  app = FastAPI()
  return app


app = create_app()

@app.get('/cus')
def get_response():
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    return dir(service)


if __name__ == '__main__':
    uvicorn.run(app)
