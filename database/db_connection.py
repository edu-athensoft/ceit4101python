# import driver
import mysql.connector

# get connection
conn = mysql.connector.connect(user='root', password='Timon@927', database='nytaxitrip')

cursor = conn.cursor()

print(cursor)

cursor.close()
conn.close()