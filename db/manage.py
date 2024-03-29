#!/usr/bin/env python

from migrate.versioning.shell import main
import os
from app import db

if __name__ == '__main__':
    db.create_all()
    db_url = os.environ.get('DATABASE_URL', 'postgresql://localhost:5432/cihui')
    db_url = db_url.replace('postgres:', 'postgresql:', 1)
    main(url=db_url, debug='False', repository='db')
