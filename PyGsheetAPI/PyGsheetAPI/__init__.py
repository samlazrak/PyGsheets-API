from googleapiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

# Initializes Gsheet API service and authorization

class PyGsheetAPI:
  def __init__(self, scope):
    self.store = file.Storage('config/credentials.json')
    self.creds = self.store.get()
    if not self.creds or self.creds.invalid:
      self.flow = client.flow_from_clientsecrets('credentials.json', scope)
      self.creds = tools.run_flow(self.flow, self.store)
    self.service = discovery.build('sheets', 'v4', http=self.creds.authorize(Http()))
    self.spreadsheets = list()
  
  def read_single_range(self, spreadsheet):
    self.service.spreadsheets().values().get(spreadsheetId=spreadsheet.id, range=spreadsheet.range).execute()
