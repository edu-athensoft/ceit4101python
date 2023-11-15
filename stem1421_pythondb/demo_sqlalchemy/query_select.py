"""
Connecting to a database

pip install mysql-connector-python

"""

# import sqlalchemy as db
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

# from pymysql import *
from sqlalchemy import create_engine, text
connection_string = "mysql+pymysql://root:my123@localhost:3306/stem1421_db2"
engine = create_engine(connection_string, echo=True)

connection = engine.connect()


result = connection.execute(text("SELECT * FROM student WHERE id = :id"), dict(id=2))


for row in result.mappings():
    print(row)
