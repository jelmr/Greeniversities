web: gunicorn --debug app:app
db_init:  python db/manage.py version_control
db_version:  python db/manage.py db_version
migrate: python db/manage.py upgrade
