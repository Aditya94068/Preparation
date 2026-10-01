import sqlite3

connection = sqlite3.connect("task_tracker.db")

task = 44
cursor = connection.cursor()

cursor.execute("SELECT * FROM tasks WHERE id = ?",(task,))

data = cursor.fetchone()

print(data)