"""
2.3 CRUD Operations
2.3.1 insert a record
sql statement with parameters
cursor.execute(sql, params)

"""
import pymysql

# connection
conn = pymysql.connect(host='localhost', user='root', password='my123', database='test', charset='utf8')

# get cursor
cursor = conn.cursor()

# insert a record
sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
params = ('Tom', '123456')
cursor.execute(sql, params)

# commit transaction
conn.commit()

# close
cursor.close()
conn.close()