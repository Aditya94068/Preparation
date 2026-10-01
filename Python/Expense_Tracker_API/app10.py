import sqlite3

connection = sqlite3.connect("task_tracker.db")
task_id = 4
title = "DSA practice"

cursor = connection.cursor()

cursor.execute("""UPDATE tasks SET title = ? WHERE id = ?""",
               (title,task_id))
connection.commit()
print("ID update successfully")

connection.close()