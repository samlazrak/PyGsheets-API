from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import secrets

store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', secrets.SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

result = service.spreadsheets().values().get(spreadsheetId=secrets.SPREADSHEET_ID, range=secrets.RANGE_NAME).execute()
numRows = result.get('values') if result.get('values') is not None else 0
print('{0} rows retrieved'.format(numRows))

