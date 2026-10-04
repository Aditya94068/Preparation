import sqlite3

connection = sqlite3.connect("task_tracker.db")

task_id = 5
title = "OOPS in C++"
category = "Building Scalable application"
description ="System Desiging Preparation"

cursor = connection.cursor()

cursor.execute("""
    INSERT INTO tasks(id,title,category,description)
    VALUES(?,?,?,?)
""",(task_id,title,category,description))

connection.commit()
print("Data inserted successfully")
connection.close