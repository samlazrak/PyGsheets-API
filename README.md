# Experiment to extract info from Excel files in Google Drive 

# PyGsheets-API
### This project is a work in progress. Use it at your risk of your own data.

A library for Google Sheets API v4 bundled with a Flask API.

Will help with extracting data from various sources and accessing the gsheets api. 

Example use cases: 

1. Taking data from spreadsheets and inputting into database
2. Taking data from database/csv/file and inputting into spreadsheet
3. Using google-sheets as a backup for data sources

# Usage:

### To use the Library bundled with the Flask API:

0. ```pip install PyGsheetAPI``` or clone the repo and in PyGsheetAPI/ ```pip install .```
1. Create an Oauth credential as detailed here: https://developers.google.com/sheets/api/quickstart/python
2. Create your own secrets.py from the example
3. Import and initalize:
```python
from flask import Flask
from PyGsheetAPI import PyGsheetAPI

app = Flask(__name__)

PyGsheetAPI = PyGsheetAPI()
```
4. Refer to Gsheets API for usage and use as the service:
```
PyGsheetAPI.service.*
```

5. Example function at '/':
```python
@app.route("/")
def test():
  result = PyGsheetAPI.service.spreadsheets().values().get(spreadsheetId=secrets.spreadsheet_id,
                                                           range=secrets.range_name).execute()
  numRows = result.get('values') if result.get('values') is not None else 0
  print('{0} rows retrieved'.format(numRows))
  return '{0} rows retrieved'.format(numRows)
```

### If you only want to use the wrapper library install from PyPi or locally from the PyGsheets-Api folder:

0. ```pip install PyGsheetAPI``` or clone the repo and in PyGsheetAPI/ ```pip install .```
1. Create an Oauth credential as detailed here: https://developers.google.com/sheets/api/quickstart/python
2. Create your own secrets.py from the example
3. Import and initalize:
```python
from PyGsheetAPI import PyGsheetAPI

PyGsheetAPI = PyGsheetAPI()
```
4. Refer to Gsheets API for usage and use as the service:
```
PyGsheetAPI.service.*
```
