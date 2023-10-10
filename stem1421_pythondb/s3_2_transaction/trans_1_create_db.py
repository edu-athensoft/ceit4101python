"""
PyMySql
Transaction

create a db
"""

import pymysql

# create a connection
try:
    conn = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306)
    # print('Connected successfully!')

    # create a cursor
    cursor = conn.cursor()

    # execute a sql statement
    DB_NAME = 'stem1421_db1'
    cursor.execute(f"create database if not exists {DB_NAME}")
    print(f"Database: {DB_NAME} created.")

except pymysql.DatabaseError as e:
    print('Database creation failed!')
except Exception as e2:
    print("Error!")
finally:
    cursor.close()
    conn.close()
