"""
2.3 CRUD Operations
2.3.4 select
sql statement with parameters
cursor.execute(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='stem1421_db1', charset='utf8')

# get cursor
cursor = conn.cursor()

# select one
sql = "SELECT * FROM users where id = %s"
params = (2,)
cursor.execute(sql, params)
result = cursor.fetchone()

# process data
print(result)

# close
cursor.close()
conn.close()