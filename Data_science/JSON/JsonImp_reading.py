import json
with open("data.json","r") as f:
    data = json.load(f)

for i in (data):
    print(i["subjects"])
    print("type of inner thingss:",type(i))
    print("type of the data :",type(data))