from flask import Flask,request,jsonify

app = Flask(__name__)
required_fields = ["id","title","category","description"]
tasks = []
@app.route("/api/tasks",methods=["POST"])
def create_task():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error" : "JSON body is required"}),400
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is not present"}),400
    if not isinstance(data["id"],int):
        return jsonify({"error" : "id must be an integer"}),400
    
    elif not isinstance(data["title"],str):
        return jsonify({"error" : "title must be string "}),400
    
    elif not isinstance(data["category"],str):
        return jsonify({"error" : "category must be an string  "}),400
    
    elif not isinstance(data["description"],str):
        return jsonify({"error" : "description must be an string "}),400
    
    tasks.append(data)
    return jsonify(tasks)
if __name__ == "__main__":
    app.run(debug=True)