"""
database orm
alchemy
ver:    1.4.11

engine
directly use it without delay

connection
"""

from sqlalchemy import create_engine

# settings
SCHEMA = 'mysql+pymysql'
USERNAME = 'appdev'
PASSWORD = 'athensoft2019'
HOST = '159.203.16.118'
PORT ='3306'
DBNAME = 'zhenzhen_db'

# title
print("SQLAlchemy - engine\n")

# create db url
DB_URL = f'{SCHEMA}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'
print("DB_URL")
print(DB_URL)
print()

# create engine
print("engine")
engine = create_engine(DB_URL)
print(engine)
print()

# connect directly
connection = engine.connect()
print("connection")
print(connection)
print()

# connection attribute
print(connection)
print(connection.connection)
print(connection.connection.connection)