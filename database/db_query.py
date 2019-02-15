# import driver
import mysql.connector

# get connection
conn = mysql.connector.connect(user='root', password='Timon@927', database='nytaxitrip')

cursor = conn.cursor()

cursor.execute('select * from test where itemid = %s', ('1',))
values = cursor.fetchall()
print(values)
print()


cursor.execute('select * from test ')
values = cursor.fetchall()

for i in values:
    print(i)

cursor.close()
conn.close()