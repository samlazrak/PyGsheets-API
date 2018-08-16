from __future__ import print_function

from googleapiclient import discovery
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools
import argparse
import time
import sqlite3

from secrets import SCOPES

# Authorization®

store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
  flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
  creds = tools.run_flow(flow, store)
service = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

DATA = {'properties': {'title': 'Toy orders [%s]' % time.ctime()}}
res = service.spreadsheets().create(body=DATA).execute()
SHEET_ID = res['spreadsheetId']
print('Created %s' % res['properties']['title'])

FIELDS = ('ID', 'Customer Name', 'Product Code', 'Units Ordered',
          'Unit Price', 'Status', 'Created at', 'Updated at')

cxn = sqlite3.connect('db.sqlite')
cur = cxn.cursor()
raw = cur.execute('SELECT * FROM orders').fetchall()
cxn.close()

raw.insert(0, FIELDS)
DATA = [row[:6] for row in raw]

service.spreadsheets().values().update(spreadsheetId=SHEET_ID,
                                       range='A1', body={'values': DATA}, valueInputOption='RAW').execute()
print('Wrote data to Sheet:')
rows = service.spreadsheets().values().get(spreadsheetId=SHEET_ID,
                                           range='Sheet1').execute().get('values', [])
for r in rows:
  print(r)
