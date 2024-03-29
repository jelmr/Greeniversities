from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
university = Table('university', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('username', String),
    Column('pw_hash', String),
    Column('description', String(length=2000)),
    Column('location', String),
    Column('logo_url', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['university'].columns['logo_url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['university'].columns['logo_url'].drop()
