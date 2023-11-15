"""
Connecting to a database

pip install mysql-connector-python

"""

# import sqlalchemy as db
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

from pymysql import *
from sqlalchemy import create_engine
connection_string = "mysql+pymysql://root:my123@localhost:3306/stem1421_db2"
engine = create_engine(connection_string, echo=True)

connection = engine.connect()

print(connection)

