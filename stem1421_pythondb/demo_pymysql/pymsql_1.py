"""
PyMySql

create connection
and check the dbms version
"""

import pymysql

# create a connection
try:
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306)
    print('Connected successfully!')
except pymysql.DatabaseError as e:
    print('Connection failed!')


# create a cursor
cursor = db.cursor()

# execute a sql statement
cursor.execute("SELECT VERSION()")

# get a single result set by fetchone()
data = cursor.fetchone()

print(f"MySQL Database version : {data}")

cursor.close()

# close connection
db.close()
