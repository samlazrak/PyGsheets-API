import os

from flask import Flask
from PyGsheetAPI import PyGsheetAPI
from config import secrets

PyGsheetAPI = PyGsheetAPI()

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
  )
  
  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)
  
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  @app.route('/')
  def test():
    result = PyGsheetAPI.service.spreadsheets().values().get(spreadsheetId=secrets.spreadsheet_id,
                                                             range=secrets.range_name).execute()
    numRows = result.get('values') if result.get('values') is not None else 0
    print('{0} rows retrieved'.format(numRows))
    return '{0} rows retrieved'.format(numRows)
  
  return app
