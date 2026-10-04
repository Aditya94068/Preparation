import sqlite3

connection = sqlite3.connect("task_tracker.db")

task_id = 10
new_title = "sqlite3 in Python"
new_category = "revisise sqlite 3"
new_description = "for better understanding"
cursor = connection.cursor()

cursor.execute("""
    UPDATE tasks
    SET title = ?,
    category = ?,
    description = ?
    WHERE id =  ?
""",(new_title,new_category,new_description,task_id))

if cursor.rowcount == 0:
    print("task Not found")
else:
    connection.commit()
    print("data updated successfully")
