"""
PyMySql
Transaction

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
    TABLE_NAME = 'account'
    sql = f"TRUNCATE TABLE {TABLE_NAME}"
    cursor.execute(sql)

    # no need to commit

    print(f"Table: {TABLE_NAME} truncated.")

except pymysql.DatabaseError as e:
    # print('Connection failed!')
    print('Database creation failed!')
except Exception as e2:
    print("Error!")
finally:
    cursor.close()
    conn.close()
