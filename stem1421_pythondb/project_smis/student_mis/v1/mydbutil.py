"""
mydbutil.py

utilities of db
"""
import pymysql


def get_connection(db=None):
    connection = None
    try:
        if db:
            connection = pymysql.connect(host='localhost', user='root', passwd='my123', port=3306, database=db)
        else:
            connection = pymysql.connect(host='localhost', user='root', passwd='my123', port=3306)
        print(f'[INFO] Connected successfully! database:{db} used.', file=open('log.txt','a'))

    except pymysql.DatabaseError as e:
        print('[ERROR] Connection failed!', file=open('log.txt','a'))
    finally:
        return connection

# test get_connection()
# myconn = get_connection()
# if myconn:
#     myconn.close()
#     print("[INFO] Connection closed.")
# else:
#     print("[WARNING] No connection created.")

# get_connection('smis')