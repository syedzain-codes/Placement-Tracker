import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MASHALLAH",
    database="placement_tracker"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM problems")

for row in cursor.fetchall():
    print(row)

conn.close()