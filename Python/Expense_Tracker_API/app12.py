import sqlite3

connection = sqlite3.connect("task_tracker.db")

task_id = 4
new_title = "DSA practice For logic building"
new_category = "DSA "
new_description= "Prepare DSA for Interview Preparation"

cursor = connection.cursor()
cursor.execute("""
    UPDATE tasks
    SET title = ?,
    category = ?,
    description = ?
    WHERE id = ?
""",(new_title,new_category,new_description,task_id))

if cursor.rowcount == 0:
    print("Task Not Found")
else:
    connection.commit()
    print("Task Updated Successfully")