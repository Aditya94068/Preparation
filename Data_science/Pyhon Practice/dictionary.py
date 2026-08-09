# Dictionary in python is a collection of keys values, used to store data values  like a map, which,unlike other data tuples which hold only a single value as an element
# In some languages it is known as map or assosiative arrays

# dict = {'name':'aditya','age':20,'gender':'male'}

# Characterstics
# Mutable
# Indexing Has no meaning
# keys can't be duplicated
# keys can't be mutable 
# --------------------------------------------------------------------------
# Create Dictionary:-


# empty dictionary
# d = {}
# print(d)


# 1D dictionary
# d1 = {
#     'name' : 'Aditya',
#     'gender' : 'male'
# }
# print(d1)


# with mixed keys
# d2 = {(1,2,3) : 1,'hello':'world'}
# print(d2)


# 2D dictionary
# student = {
#     'name' : 'Aditya',
#     'college' : 'SOCSE',
#     'sem'  : 5,
#     'subject' :{
#         'dsa' : 50,
#         'maths' : 67,
#         'english':34
#     }
# }
# print(student)


# using sequence and dict function
# d3 = dict([(1,1),(2,2),(3,3)])
# print(d3)
# d4 = dict([('name','aditya'),('age',21)])
# print(d4)
# d4 = dict([(4,5)])
# print(d4)


# duplicate keys
#you can not have the duplicate keys --> agar duplicate hai toh last wali key-value print hoga
# d5 = {'name' : 'aditya','name':'sumit','name':'nita'}
# print(d5)


# mutable items as keys
# d6 = {
#     'name' : 'aditya',
#     (1,2,3) : 3
# }
# print(d6)
# -----------------------------------------------------------------------------------
#Accessing items:-
# my_dict = {'name' : 'jack','age':26}
# print(my_dict[0]) --> ye wrong hai dictionary main index nhi hote hai

#[]
# print(my_dict['name'])
# print(my_dict['age'])
#get
# print(my_dict.get('name'))
# print(my_dict.get('age'))
# print(student['subject']['maths'])
# ------------------------------------------------------------------------------------
#Adding new key-value pair:-
# print(d4)
# d4['gender'] = 'male'
# print(d4)
# d4['weight'] = 56
# print(d4)
# student['subject']['data science'] = 45
# print(student)
# ---------------------------------------------------------------------------------------
#Remove key-value pair:-
# d = {'name': 'aditya', 'age': 21,3:3, 'gender': 'male', 'weight': 56}

#pop
# print(d)
# d.pop(3)
# print(d)

#popitem --> last wale key-value pair ko delete karta hai
# d.popitem()
# print(d)

#del
# del d['name']
# print(d)
#clear -->empty dictionary ban jayega
# d.clear()
# print(d)

# 2d dictionary
# del student['subject']['dsa']
# print(student)

# ---------------------------------------------------------------------
#Editing key-value pair:-
# student = {
#     'name' : 'Aditya',
#     'college' : 'SOCSE',
#     'sem'  : 5,
#     'subject' :{
#         'dsa' : 50,
#         'maths' : 67,
#         'english':34
#     }
# }
# student['sem'] = 6
# print(student)
# student['subject']['dsa']=80
# print(student)
# -------------------------------------------------------------------------------

# Dictionary Operations
# 1.Membership
# 2.Iteration
# student = {
#     'name' : 'Aditya',
#     'college' : 'SOCSE',
#     'sem'  : 5,
#     'subject' :{
#         'dsa' : 50,
#         'maths' : 67,
#         'english':34
#     }
# }
# 1.Membership --> ye operators sirf keys ke upar kaam karta hai
# print(student)
# print('name' in student)
# print('' in student)

# 2.Iteration
# d = {'name' :'nitish' , 'gender' : 'male','age' : 33}
# for i in d:
#     print(i,d[i])

# -------------------------------------------------------------------------
# Dictionary Functions
#len/sorted/min/max

#len
d = {'name' :'nitish' , 'gender' : 'male','age' : 33}
# print(len(d))

#sorted
# print(sorted(d,reverse=True))

#min --> ASCII value ke hisab se min kaam karta hai
# print(min(d))

#max --> ASCII value ke hisab se max kaam karta hai
# print(max(d))

#items/keys/values
# print(d)
# items
# print(d.items())
# keys
# print(d.keys())
# values
# print(d.values())


# update
# d1 = {1:2,3:4,4:5}
# d2 = {4:7,6:8}
# d1.update(d2)
# print(d1)

# Dictionary Comprehension
# {key : value for vars in iterable}

# # print 1st 10 numbers ans their squares
# ans = {}
# ans = {i : i ** 2 for i in range(1,11)}
# print(ans)

#using existing dict
# distance = {'delhi ' : 1000,'mumbai' : 2000,'bangalore' : 3000}
# ans = {}
# ans = {key : value * 0.62 for (key,value) in distance.items() }
# print(ans)

#using zip -- zip function do ya usse zyada iterable (jaise list , tuple) ko pair (jod) bana kar ek sath iterate karne ke kaam aata hai
# Zip function example
# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]

# print(list(zip(x, y, z)))

# days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
# ans = {}
# ans = {i : j for (i,j) in zip(days,temp_C)}
# print(ans)

# using if condition
# products = {'phone' : 10 , 'laptop' : 0,'charger' : 32,'tablet' : 0}
# ans = {}
# ans = {key : value for (key , value) in products.items() if value > 0}
# print(ans)

# Nested Comprehension
# print tables of number from 2 to 4
# ans = {}
# ans = {i :{j: i * j for j in range(1 , 11)} for i in range(2,5)}
# print(ans )