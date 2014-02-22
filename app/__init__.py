from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.lesscss import lesscss
import os
import flask_sijax

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lesscss(app)

from app import views, models

path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)