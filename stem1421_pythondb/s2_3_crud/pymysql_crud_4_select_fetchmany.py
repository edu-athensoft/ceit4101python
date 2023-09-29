"""
2.3 CRUD Operations
2.3.4 select

sql statement with parameters
cursor.execute(sql, params)
cursor.fetchmany()

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='stem1421_db1', charset='utf8')

# get cursor
cursor = conn.cursor()

# retrieve a few rows
sql = "SELECT * FROM users"
cursor.execute(sql)
SIZE = 3
results = cursor.fetchmany(SIZE)
print(results)

results = cursor.fetchmany(SIZE)
print(results)

results = cursor.fetchmany(SIZE)
print(results)

results = cursor.fetchmany(SIZE)
print(results)

# close
cursor.close()
conn.close()