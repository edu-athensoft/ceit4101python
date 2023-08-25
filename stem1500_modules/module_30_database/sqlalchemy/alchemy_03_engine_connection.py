"""
database orm
alchemy
ver:    1.4.11

engine
directly use it without delay

connection

RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods

"""

from sqlalchemy import create_engine

# settings
SCHEMA = 'mysql+pymysql'
USERNAME = 'stemlearner'
PASSWORD = 'athensoft'
HOST = '192.168.1.3'
PORT ='3306'
DBNAME = 'stem1421pythondb'

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
print("connecting...")
connection = engine.connect()
print("connected.")
print()

# connection attribute
print(connection)
print(connection.connection)
print(connection.connection.connection)
print()

# closing
print("closing connection...", end="")
connection.close()
print("[Closed]")

print("closing db engine...", end="")
engine.dispose()
print("[Closed]")