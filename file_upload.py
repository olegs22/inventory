from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient.http import MediaFileUpload,MediaIoBaseDownload
import io

# Setup the Drive v3 API
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('drive', 'v3', http=creds.authorize(Http()))

def upload_line_inventory(line):
    folder_id ="11eI6k0sNr7uahvcaUdLCZIKZWLAQQnQM"
    file_metadata ={
        "name": line+"_inventory_count.csv",
        "mimeTyoe": "application/vnd.google-apps.spreadsheet",
        "parents": [folder_id]
    }

    media = MediaFileUpload("inventory_count.csv",
                            mimetype="text/csv",
                            resumable=True)

    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return None
