from flask import Flask,jsonify,request

app = Flask(__name__) 

expenses = []

@app.route("/api/expenses",methods = ["POST"])
def add_expense():
    data = request.get_json()
    expenses.append(data)
    return jsonify(data)
@app.route("/api/expenses/<int:id>",methods=["GET"])
def get_expenses(id):
    
    for expense in expenses:
        if expense["id"] == id:
             return jsonify(expense)
    return jsonify({"error":"Expense not found"}),404

@app.route("/api/expenses/<int:id>",methods=["PUT"])
def update_expenses(id):
    data = request.get_json()
    for expense in expenses:
        if expense["id"] == id:
            expense["amount"] = data["amount"]
            expense["category"] = data["category"]
            expense["description"] = data["description"]
            return jsonify(expense)
    return jsonify({"error" : "Expense Not Found"}),404

@app.route("/api/expenses/<int:id>",methods=["DELETE"])
def delete_expense(id):
    for expense in expenses:
        if expense["id"] == id:
            expenses.remove(expense)
            return jsonify(expenses)
    return jsonify({"error" : "Expense Not Found"}),404
if __name__ == "__main__":
    app.run(debug= True)