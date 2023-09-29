"""
3.2 Create connection and specify DB
"""

import pymysql

# create a connection
try:
    db = pymysql.connect(host='localhost',
                         user='root',
                         passwd='my123',
                         port=3306)

    db.select_db('abccompany')

    print('Connected successfully!')
except pymysql.DatabaseError as e:
    print('Connection failed!')