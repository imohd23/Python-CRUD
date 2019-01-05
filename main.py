import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='mysql')
print (cnx)
cursor = cnx.cursor()

q = "select * from db"

print (cursor.execute(q))
