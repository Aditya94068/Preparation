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
    try:
         cursor = connnection.cursor()
         cursor.execute("SELECT * FROM tasks")
         data = cursor.fetchall()
    except Exception as e:
        return jsonify({"error" :"Data base error"}),500
    finally:
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
    return jsonify({"message" : "Tasks Fetched Successfully",
                    "tasks" : result}),200

@app.route("/api/tasks/<int:id>",methods=["GET"])
def task_by_id(id):
    connection = get_db_connection()
    task_id = id
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?",(task_id,))
        data = cursor.fetchone()
        if data is None:
          return jsonify({"error" : "id not found"}),404
    except Exception as e:
        return jsonify({"error" : "Database error"}),500
    finally:
        connection.close()

    result = { "id" : data[0],
             "title" : data[1],
             "category" : data[2],
             "description" : data[3]
             }
    return jsonify({"message" : "Task Fetched Successfully",
                    "task" :result}),200

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
    cursor = connection.cursor()
    try:
          cursor.execute("""
            INSERT INTO tasks(title,category,description)
            VALUES(?,?,?)
        """,(data["title"],data["category"],data["description"]))
          connection.commit()
          task_id = cursor.lastrowid
    except:
        connection.rollback()
        return jsonify({"error" : "data base error"}),500
    finally:
        connection.close()
    return jsonify({
                   "message" : "Task Added Successfully",
                   "task":{
                       "id" : task_id,
                       "title" : data["title"],
                       "category" : data["category"],
                       "description" :data["description"]
                   }
                }),201

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
    try:
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE tasks
        SET title = ?,category = ?,description = ?
        WHERE id = ?
    """,(data["title"],data["category"],data["description"],id))
        if cursor.rowcount == 0:
            return jsonify({"error" : "task not found"}),404
        connection.commit()

    except Exception as e:
        connection.rollback()
        return jsonify({"error" :"database error"}),500
    finally:
        connection.close()
    return jsonify({"message" :"Task Update successfully",
                    "task" : {
                        "id" : id,
                         "title" : data["title"],
                         "category" : data["category"],
                         "description" :data["description"]
                    }
                    }),200

@app.route("/api/tasks/<int:id>",methods=['DELETE'])
def delete_task(id):
    connections = get_db_connection()
    try:
        cursor = connections.cursor()
        cursor.execute("""
        SELECT * FROM tasks WHERE id = ?
""",(id,))
        data = cursor.fetchone()
        if data is None:
            return jsonify({"error" : "Task not found"}),404
        response = {
            "message" : "Task Deleted Successfully",
            "task" : {
                "id" : id,
                "title" :data[1],
                "category" : data[2],
                "description" : data[3]
            }
        }
        cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """,(id,))
        connections.commit()
    except Exception as e:
           connections.rollback()
           return jsonify({"error" :"database error"}),500
    finally:
        connections.close()
    return jsonify(response),200

@app.route("/api/tasks/filter",methods=["GET"])
def filter_by_category():
    category = request.args.get("category")
    if category is None or category.strip() == "":
        return jsonify({"error" : "category not found"}),400
    connections = get_db_connection()
    try:
         cursor = connections.cursor()
         cursor.execute("""
         SELECT * FROM tasks 
         WHERE category = ?
    """,(category,))
         data = cursor.fetchall()
    except Exception as e:
        return jsonify({"error" : "Data base error" }),500
    finally:
        connections.close()

    result = []

    for row in data:
        result.append(
            {
                "id" : row[0],
                "title" : row[1],
                "category":row[2],
                "description":row[3]
            }
        )
    return jsonify({"message" : "Task Filter successfully",
                    "tasks" : result}),200
@app.route("/api/tasks/search",methods=["GET"])
def searching():
    connection = get_db_connection()
    search = request.args.get("search")
    if search is None or search.strip() =="":
        return jsonify({"error":"Search cannot be empty"}),400
    try:
         cursor = connection.cursor()
         cursor.execute("""
         SELECT * FROM tasks
          WHERE title LIKE ?
     """,("%" + search + '%',))
         data = cursor.fetchall()
    except Exception as e:
         return jsonify({"error" : "Database error"}),500
    finally:
        connection.close()
    if not data:
        return jsonify({"error" : "task is not present"}),404
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
    return jsonify({"message" :"Task Search Successfully",
                    "tasks": result}),200

@app.route("/api/tasks/search/filter",methods=["GET"])
def search():
    connections=get_db_connection()
    category = request.args.get("category")
    search = request.args.get("search")
    if category is None or category.strip() == "":
        return jsonify({"error" :"category Cannot be empty"}),400
    if search is None or search.strip() == "":
        return jsonify({"error" :"search Cannot be empty"}),400
    try:
            cursor = connections.cursor()
            cursor.execute("""
            SELECT * FROM tasks
            WHERE category = ? AND title LIKE ?
        """,(category,"%" + search + "%"))
            data = cursor.fetchall()
    except Exception as e:
        return jsonify({"error" : "Database error"}),500
    finally:
         connections.close()
    if not data:
        return jsonify({"error" :"task is not present"}),404
    result = []
    for row in data:
        result.append({
            "id" : row[0],
            "title":row[1],
            "category":row[2],
            "description":row[3],

        })
    return jsonify({"message" : "Task Successfully Found",
                    "tasks" : result}),200
if __name__ == "__main__":
    app.run(debug=True)