import sqlite3
connection = sqlite3.connect("task_tracker.db")
cursor = connection.cursor()
# cursor.execute("""
#    CREATE TABLE tasks(
#        id INTEGER PRIMARY KEY,
#        title TEXT NOT NULL,
#        category TEXT NOT NULL,
#        description TEXT NOT NULL
#    )
# """)

# cursor.execute("""
#     INSERT INTO tasks(id,title,category,description)
#     VALUES(1,'Learn flask','backend','learn flask basics')
# """)

# cursor.execute("""
#     INSERT INTO tasks(id,title,category,description)
#     VALUES(2,'Learn SQLlite3','database','learn basics of sqlite')
# """)

# cursor.execute("""
#     INSERT INTO tasks(id,title,category,description)
#     VALUES(3,'java','core java','backend')
# """)
connection.commit()
print("Task Table creted successfully ")
connection.close()