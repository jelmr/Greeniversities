from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
import logging
from backend import *

## FLASK
app = Flask(__name__)
api = restful.Api(app)
api.add_resource(UniversityList, '/university/')
api.add_resource(UniversityScore, '/university/<int:university_id>')

app.config.from_object('config')
logging.basicConfig(level=logging.DEBUG)

## SQL ALCHEMY
db = SQLAlchemy(app)

