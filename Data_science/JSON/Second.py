import json
file_string =open("data.json","r")
x = file_string.read()
finaldata = json.loads(x)
for a in finaldata:
    print(a["subjects"],a["name"])