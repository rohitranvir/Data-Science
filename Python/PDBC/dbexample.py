import mysql.connector as ms

conn = ms.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="campusx"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM marks")

for row in cursor:
    print(row)

conn.close()