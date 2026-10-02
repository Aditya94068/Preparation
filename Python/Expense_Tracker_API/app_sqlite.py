import sqlite3
from flask import Flask,request,jsonify

app = Flask(__name__)
def get_db_connection():

    connection = sqlite3.connect("task_tracker.db")

    return connection

@app.route("/")
def home():
    connection = get_db_connection()
    connection.close()
    return "Database connected successfully"

@app.route("/api/tasks",methods=["GET"])
def tasks():
    connnection = get_db_connection()
    cursor = connnection.cursor()
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    connnection.close()
    result = []
    for row in data:
        result.append(
           {
               "id" : row[0],
               "title" : row[1],
               "category" : row[2],
               "description" : row[3]
           }
        )
    return jsonify(result)

@app.route("/api/tasks/<int:id>",methods=["GET"])
def task_by_id(id):
    connection = get_db_connection()
    task_id = id
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?",(task_id,))
    data = cursor.fetchone()
    connection.close()
    if data is None:
        return jsonify({"error" : "id not found"}),404
    result = { "id" : data[0],
             "title" : data[1],
             "category" : data[2],
             "description" : data[3]
             }
    return jsonify(result),200

@app.route("/api/tasks",methods=["POST"])
def add_task():
    required_field = ['title','category','description']
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error" : "json is missing"}),400
    
    for field in required_field:
        if field not in data:
            return jsonify({"error" : f"{field} is required"}),400
    if not isinstance(data["title"],str):
        return jsonify({"error" : "title must be string"}),400 

    if not isinstance(data["category"],str):
        return jsonify({"error" : "category must be string"}),400

    if not isinstance(data["description"],str):
        return jsonify({"error" :"description must be string"}),400
    for field in required_field:
        if data[field].strip() == "":
            return jsonify({"error" : f"{field} cannot be empty"}),400
            
    connection = get_db_connection()
    connection.execute("""
    INSERT INTO tasks(title,category,description)
    VALUES(?,?,?)
""",(data["title"],data["category"],data["description"]))
    connection.commit()
    connection.close()
    return jsonify("Task Added Successfully"),201

@app.route("/api/tasks/<int:id>",methods = ["PUT"])
def update_task(id):
    required_field = ["title","category","description"]
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error" : "JSON is missing"}),400
    for field in required_field:
        if field not in data:
            return jsonify({"error" : f"{field} is required"}),400
    if not isinstance(data["title"],str):
        return jsonify({"error" : "title must be string"}),400

    if not isinstance(data["category"],str):
        return jsonify({"error":"category must be string"}),400
    if not isinstance(data["description"],str):
        return jsonify({"error" :"description must be string"}),400

    for field in required_field:
        if data[field].strip() == "":
            return jsonify({"error" : f"{field} cannot be empty"}),400    
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE tasks
    SET title = ?,category = ?,description = ?
    WHERE id = ?
""",(data["title"],data["category"],data["description"],id))
    if cursor.rowcount == 0:
        connection.close()
        return jsonify({"error" : "task not found"}),404
    connection.commit()
    connection.close()
    return jsonify("Update successfully")

@app.route("/api/tasks/<int:id>",methods={'DELETE'})
def delete_task(id):
    connections = get_db_connection()
    cursor = connections.cursor()
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = ?
""",(id,))
    if cursor.rowcount == 0:
        connections.close()
        return jsonify({"error":"task not found"}),404
    else:
        connections.commit()
        connections.close()
        return jsonify({"message" :"task deleted successfully"}),200
if __name__ == "__main__":
    app.run(debug=True)