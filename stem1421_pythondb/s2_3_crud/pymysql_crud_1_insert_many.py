"""
2.3 CRUD Operations
2.3.1 insert a record
sql statement with parameters
cursor.execute(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='stem1421_db1', charset='utf8')

# get cursor
cursor = conn.cursor()

# insert record
sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
params = ('Jason', '999')
cursor.execute(sql, params)

params = ('John', '101010')
cursor.execute(sql, params)

# commit transaction
conn.commit()

# close
cursor.close()
conn.close()