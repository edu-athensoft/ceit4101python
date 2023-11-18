"""
Connecting to a database

pip install mysql-connector-python
https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples
"""

# import sqlalchemy as db
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

# from pymysql import *
from sqlalchemy import create_engine, text
connection_string = "mysql+pymysql://root:my123@localhost:3306/stem1421_db2"
engine = create_engine(connection_string, echo=True)

connection = engine.connect()

sql = "insert into student(student_name, school_name, grade) value(:student_name, :school_name, :grade)"
params = [{'student_name':'Kate', 'school_name':'Saint Mary', 'grade':'g7'},
          {'student_name':'Sandy', 'school_name':'International', 'grade':'g9'}]
connection.execute(text(sql), params)

connection.commit()

