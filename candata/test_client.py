"""
test client
"""

import mydbutil, setupdb, setuptable

DB_HOST = '138.197.159.95'
DB_NAME = "candata_db1"

# test connection
conn = mydbutil.get_connection(db=DB_NAME, dbhost=DB_HOST)
print(conn)

# create database remotely
setupdb.create_db(database=DB_NAME, dbhost=DB_HOST)

# create a table
# table schema

TABLE_NAME = 'financial_summary'
sql = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "(" \
      + "id int auto_increment, " \
      + "source varchar(100), " \
      + "summary TEXT, " \
      + "sentiment_score decimal, " \
      + "primary key (id) " \
      + ")"
setuptable.create_table(sql,conn, DB_NAME, DB_HOST)