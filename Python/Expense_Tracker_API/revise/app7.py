import sqlite3

connection = sqlite3.connect("task_tracker.db")

cursor = connection.cursor()

cursor.execute("""SELECT * FROM tasks WHERE id = 2""")

data = cursor.fetchone()
print(data)