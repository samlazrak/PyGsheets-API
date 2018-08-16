from __future__ import print_function

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

from secrets import SCOPES, spreadsheet_id, value_input_option

# Authorization

store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Functions
data = [
    {
        "range": "Sheet1!A1:A4",
        "majorDimension": "COLUMNS",
        "values": [
            ["Item", "Wheel", "Door", "Engine"]
        ]
    },
    {
        "range": "Sheet1!B1:D2",
        "majorDimension": "ROWS",
        "values": [
            ["Cost", "Stocked", "Ship Date"],
            ["$20.50", "4", "3/1/2018"]
        ]
    }
]
body = {
    'valueInputOption': value_input_option,
    'data': data
}
result = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id, body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')));
