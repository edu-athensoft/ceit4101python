"""
3.1 Create connection
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