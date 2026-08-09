import json
data = {"name":"Aditya Vaishnav","age":21,"course":"python","college":"Sandip University","laptop":"HP"}
with open("this.json","w") as f:
    json.dump(data,f)


data =[{"name":"Aditya vaishnv","Bname":"Sumit Vaishnav","Mname":"Nita vaishnav","Fname":"Sunit Vaishnv"}]
json_string = json.dumps(data)

print(json_string,"\n",type(json_string))