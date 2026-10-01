import sqlite3

connection = sqlite3.connect("task_tracker.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM TASKS")

data = cursor.fetchone()

print(data)