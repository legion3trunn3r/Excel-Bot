

from data.googleAPI_creating import sheet_id, sheet

import creds.googleAPI as googleAPI

class Sheets():

    def get_data_from_sheet(range_query):
        resp = sheet.values().get(spreadsheetId=sheet_id, range=range_query).execute()
        return resp['values']