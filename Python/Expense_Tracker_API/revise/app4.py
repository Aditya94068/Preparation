from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = []
required_field = ["id","title","category","description"]
required_field_put = ["title","category","description"]
@app.route("/api/create_task",methods=["POST"])
def create_task():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error" : "JSON body is required"}),400
    for field in required_field:
        if field not in data:
            return jsonify({"error" : f"{field} is not present"}),400
    if not isinstance(data["id"],int):
        return jsonify({"error":"id must be integer "}),400
    elif not isinstance(data["title"],str):
        return jsonify({"error":"title must be string"}),400
    elif not isinstance(data["category"],str):
        return jsonify({"error" : "category must be string"}),400
    elif not isinstance(data["description"],str):
        return jsonify({"error" : "description must be string"}),400
    for task in tasks:
        if task["id"] == data["id"]:
            return jsonify({"error" : "task id already exists"}),400
    for field in ["title","category","description"]:
        if data[field].strip() == "":
            return jsonify({"error" : f"{field} cannot be empty"}),400
    tasks.append(data)
    return jsonify(tasks),201
@app.route("/api/get_all_task",methods=["GET"])
def get_all_task():
    if not tasks:
        return jsonify({"Error":"Tasks Do not exists"}),404
    else:
        return jsonify(tasks),200
@app.route("/api/get_task_by_id/<int:id>",methods=["GET"])
def get_task_by_id(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task),200
    return jsonify({"error" : "task not exist"}),404
@app.route("/api/update_task/<int:id>",methods=["PUT"])
def update_task(id):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error" : "json is empty"}),400
    for field in required_field_put:
        if field not in data:
            return jsonify({"error" : f"{field} is not present"}),400
        
    if not isinstance(data["title"],str):
        return jsonify({"error":"title must be string"}),400
    elif not isinstance(data["category"],str):
        return jsonify({"error" : "category must be string"}),400
    elif not isinstance(data["description"],str):
        return jsonify({"error" : "description must be string"}),400
    
    for field in ["title","category","description"]:
        if data[field].strip() == "":
            return jsonify({"error" : f"{field} cannot be empty"}),400
    for task in tasks:
        if task["id"] == id:
            task["category"] = data["category"]
            task["description"] = data["description"]
            task["title"] = data["title"]
            return jsonify(task)
    return jsonify({"error" : "task not found"}),404

@app.route("/api/delete_task/<int:id>",methods=["DELETE"])
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            deleted = task
            tasks.remove(task)
            return jsonify({
                "message" : "Task deleted successfully",
                "task":deleted
                }),200
    return jsonify({"error" : "task not found"}),404

@app.route("/api/search_task",methods=["GET"])
def search_task():
    title = request.args.get("title")
    if title is None:
        return jsonify({"error" : "title not found"}),400
    result = []
    for task in tasks:
       if title.lower() in task["title"].lower():
          result.append(task)
    if result:
        return jsonify(result) ,200     
    return jsonify({"error" : "task is not found"}),404

@app.route("/api/filter_task",methods=["GET"])
def filter_task():
    category = request.args.get("category")
    if category is None:
            return jsonify({"error" : "category not found"}),400
    result = []
    for task in tasks:
        if task["category"] == category:
            result.append(task)
    if result:
            return jsonify(result) ,200     
    return jsonify({"error" : "task is not found"}),404

@app.route("/api/task_statistics",methods=["GET"])
def task_statistics():
    total_task = len(tasks)
    category_count = {}
    title_count = {}
    for task in tasks:
        category = task["category"]
        if category in category_count:
            category_count[category] +=1
        else:
            category_count[category] = 1
    for task in tasks:
        title = task["title"]
        if title in title_count:
            title_count[title] +=1
        else:
            title_count[title] = 1   
    return jsonify({"total_task" : total_task,"category_count" : category_count,"title_count" : title_count})
if __name__ == "__main__":
    app.run(debug=True)