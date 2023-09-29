"""
2.3 CRUD Operations
2.3.2 update a record
sql statement with parameters
cursor.execute(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='test', charset='utf8')

# get cursor
cursor = conn.cursor()

# update all records
sql = "UPDATE users SET password = %s"
params = ('123456',)
cursor.execute(sql, params)

# commit transaction
conn.commit()

# close
cursor.close()
conn.close()