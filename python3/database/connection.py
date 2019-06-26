import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root", db="world")

cursor = db.cursor()
cursor.execute("SELECT * FROM city")


for i in cursor:
    print(i)

print(cursor.fetchone())



