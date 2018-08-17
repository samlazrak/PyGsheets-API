import os

from flask import Flask
from PyGsheetAPI import PyGsheetAPI, spreadsheet
from config import secrets

PyGsheetAPI = PyGsheetAPI(secrets.scope)

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
    PyGsheetAPI.spreadsheets.append(spreadsheet(secrets.spreadsheet_id, secrets.range_name,
                                                secrets.value_input_option))
    print(PyGsheetAPI.read_single_range(PyGsheetAPI.spreadsheets[0]))
  
  return app
