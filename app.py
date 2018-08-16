import secrets

from flask import Flask
from PyGsheetAPI import PyGsheetAPI

app = Flask(__name__)

PyGsheetAPI = PyGsheetAPI()

@app.route("/")
def test():
  result = PyGsheetAPI.service.spreadsheets().values().get(spreadsheetId=secrets.spreadsheet_id,
                                                           range=secrets.range_name).execute()
  numRows = result.get('values') if result.get('values') is not None else 0
  print('{0} rows retrieved'.format(numRows))
  return '{0} rows retrieved'.format(numRows)
