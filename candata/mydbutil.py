"""
test database connection
remote server:
"""

import pymysql


def get_connection(dbhost, db=None):
    connection = None
    try:
        if db:
            connection = pymysql.connect(host=dbhost, user='root', passwd='athensoft', port=3306, database=db)
        else:
            connection = pymysql.connect(host=dbhost, user='root', passwd='athensoft', port=3306)
        print(f'[DEBUG] Connected successfully! database:{db} used.', file=open('log.txt', 'a'))

    except pymysql.DatabaseError as e:
        print('[ERROR] Connection failed!', file=open('log.txt', 'a'))
        print(e)
    finally:
        return connection



