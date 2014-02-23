from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.lesscss import lesscss
from flask.ext.login import LoginManager
import os
import flask_sijax


## FLASK
app = Flask(__name__)
app.config.from_object('config')

## SQL ALCHEMY
db = SQLAlchemy(app)

## LESS
lesscss(app)

## SIJAX
path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_STATIC_PATH'] = path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
flask_sijax.Sijax(app)

## FLASK_LOGIN
lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

from app import views, models
