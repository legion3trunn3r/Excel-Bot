import os

from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

# Spreadsheet token
sheet_id = '<Your sheet id token>'

def get_service_sacc():
    creds_json = os.path.dirname(__file__)[:-4] + "/creds/googleAPI/token.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)



service = get_service_sacc()
sheet = service.spreadsheets()
