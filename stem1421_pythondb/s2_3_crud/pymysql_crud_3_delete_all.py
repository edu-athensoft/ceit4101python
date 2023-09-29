"""
2.3 CRUD Operations
2.3.3 delete a record
sql statement with parameters
cursor.execute(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='stem1421_db1', charset='utf8')

# get cursor
cursor = conn.cursor()

# delete a record
sql = "DELETE FROM users"
cursor.execute(sql)

# commit transaction
conn.commit()

# close
cursor.close()
conn.close()