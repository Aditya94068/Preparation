import json

# Ya code json string ko python dictionary me converty karta hai (mtlb python object me convert karta hai)
# d = '[{"course" : "python","fees" : 12000}]'
# x = json.loads(d)
# print(x)
# print(type(x))
# print("\n-----------\n")
# for a in x:
#     print(a)
#     print(type(a))

#Ye code python dictionary ko json string me convert karta hai
c = {"course":"c++","fees":18000}
c = json.dumps(c)
print(c,type(c))



