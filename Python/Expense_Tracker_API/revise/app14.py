import sqlite3

connection = sqlite3.connect("task_tracker.db")

task_id = 64

cursor = connection.cursor()

cursor.execute("""
    DELETE FROM tasks
    WHERE id = ?

""",(task_id,))

if cursor.rowcount == 0:
    print("No Task is present")
else:
    connection.commit()
    print("Task Deleted Successfully")

connection.close()