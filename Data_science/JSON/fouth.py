import json
with open("this.json","r") as file:
    file = json.load(file)
print(file,type(file))