from flask import Flask,jsonify,request


app = Flask(__name__)
tasks = []
@app.route('/')
def home():
    return "Aditya Vaishnav"

@app.route('/api/tasks',methods=['POST'])
def add_task():
    data = request.get_json()
    tasks.append(data)
    return jsonify(tasks)

@app.route('/api/tasks',methods=['GET'])
def all_task():
    if tasks:
        return jsonify(tasks)
    return jsonify({"error" : "tasks not fount"}), 404
@app.route("/api/tasks/<int:id>",methods=['GET'])
def one_task(id):
     for task in tasks:
         if task["id"] == id:
             return jsonify(task)
     return jsonify({"error" : "Task Not Found"}),404

@app.route("/api/tasks/<int:id>",methods = ['PUT'])
def update_task(id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == id:
            task["category"] = data["category"]
            task["title"] = data["title"]
            task["description"] = data["description"]
            return jsonify(task)
    return jsonify({"error" : "Task Not Found"}),404

@app.route("/api/tasks/<int:id>",methods=['DELETE'])
def delete_task(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            return jsonify(tasks)
    return jsonify({"error" : "Task Not Found"}),404
if __name__ == "__main__":
    app.run(debug=True)