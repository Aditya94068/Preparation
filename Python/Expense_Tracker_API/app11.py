import sqlite3

connection = sqlite3.connect("task_tracker.db")

task_id = 4
new_title = "DSA practice"
new_category = "DSA"
new_description= "Prepare DSA for Interview Preparation"

cursor = connection.cursor()
cursor.execute("""
UPDATE tasks
SET title = ?,
category = ?,
description = ?
WHERE id = ?
""",(new_title,new_category,new_description,task_id))
connection.commit()
print("Successfully Updated")
