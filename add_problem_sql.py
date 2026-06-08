import mysql.connector
from datetime import date

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MASHALLAH",
    database="placement_tracker"
)

cursor = conn.cursor()

name = input("Problem Name: ")
topic = input("Topic: ")
difficulty = input("Difficulty: ")

query = """
INSERT INTO problems
(name, topic, difficulty, solved_date)
VALUES (%s, %s, %s, %s)
"""

values = (
    name,
    topic,
    difficulty,
    date.today()
)

cursor.execute(query, values)

conn.commit()

print("Problem Added Successfully!")

conn.close()