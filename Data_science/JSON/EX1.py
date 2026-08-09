import json
data = {

    "name":"Aditya",
    "age":21,
    "Branch":"CSE"
}
d = json.dumps(data)
print(type(d),"\n",d)