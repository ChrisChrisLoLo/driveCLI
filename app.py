#!/usr/bin/env python3
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

drive_service = build('drive','v3')

flow = InstalledAppFlow.from_client_secret_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/drive.metadata.readonly']
)

if __name__ == 'main':
    print('HIIIIII')