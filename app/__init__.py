from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.lesscss import lesscss

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lesscss(app)

from app import views, models

