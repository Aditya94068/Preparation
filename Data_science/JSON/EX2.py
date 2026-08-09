import json
json_string ='{"Name":"Aditya", "age" :20,"Branch":"CSE"}'
d = json.loads(json_string)
print(type(d),"\n",d)