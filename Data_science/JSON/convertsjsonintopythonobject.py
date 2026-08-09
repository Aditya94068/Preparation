import json
data = '{"name":"aditya","bname":"Sumit","fname":"sunil"}'

with open("this.json","r") as f:
    x = json.loads(data)


print(type(x),x)
