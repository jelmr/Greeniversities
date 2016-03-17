import os
basedir = os.path.abspath(os.path.dirname(__file__))

## SQL alchemy ---------------------------------------------------------------

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
if 'DATABASE_URL' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_MIGRATE_REPO = os.path.join("./", 'db_repository')

## What the forms ------------------------------------------------------------

CSRF_ENABLED = True
SECRET_KEY = '<redacted>'
