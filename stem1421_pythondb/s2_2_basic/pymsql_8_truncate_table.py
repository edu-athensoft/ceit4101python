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
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306,
                         database=DB_NAME)
    print('Connected successfully!')

    # create a cursor
    cursor = db.cursor()

    # execute a sql statement
    TABLE_NAME = 'users'
    sql = f"TRUNCATE TABLE {TABLE_NAME}"
    cursor.execute(sql)

    print(f"Table: {TABLE_NAME} truncated.")

except pymysql.DatabaseError as e:
    # print('Connection failed!')
    print('Database creation failed!')

except Exception as e2:
    print("Error!")

# close cursor
cursor.close()
# close connection
db.close()
