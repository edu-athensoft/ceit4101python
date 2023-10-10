"""
PyMySql
2.2.6 Create Database

create a db
"""

import pymysql

# settings
DB_NAME = 'stem1421_db1'

# create a connection
try:
    conn = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306,
                         database=DB_NAME)
    # print('Connected successfully!')

    # create a cursor
    cursor = conn.cursor()

    # execute a sql statement
    sql = "create table if not exists account(" \
          + "id int auto_increment, " \
          + "client_name varchar(20), " \
          + "acct_name varchar(20), " \
          + "balance decimal(20,2), " \
          + "trans_date date, " \
          + "primary key (id) " \
          + ")"
    cursor.execute(sql)

    TABLE_NAME = 'account'
    print(f"Table: {TABLE_NAME} created.")

except pymysql.DatabaseError as e:
    # print('Connection failed!')
    print('Table creation failed!')

except Exception as e2:
    print("Error!")
finally:
    cursor.close()
    conn.close()
