from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
university = Table('university', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR),
    Column('username', VARCHAR),
    Column('pw_hash', VARCHAR),
    Column('description', VARCHAR(length=2000)),
    Column('location', VARCHAR),
    Column('logo_url', VARCHAR),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['university'].columns['pw_hash'].drop()
    pre_meta.tables['university'].columns['username'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['university'].columns['pw_hash'].create()
    pre_meta.tables['university'].columns['username'].create()
