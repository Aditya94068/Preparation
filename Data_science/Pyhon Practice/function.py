# function are of two types 
# builtin function
# user defined function
# function use two principle
# 1.Abstraction :- isme chizze hide rehti hai
# 2.Deccomposition :- part by part chize create karna mtlb function by function program banana
# ---------------------------------------------------------------------------------------------------------------------------
#Defining function
# def is_even(num):
#     """
#     this function returns if a given number is odd or even
#     input - any valid integr
#     output - odd/even
#     """
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
    
# # calling function
# for i in range(1,11):
#     x = is_even(i)
#     print(x)

# --------------------------------------------
# # documentation of a particular function
# print(is_even.__doc__)
# ---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
#point of views
# whenever we are designing a function agar hamara function main koi bhi problem ho rahi hai toh wo hamari galti hai 
# koi bhi bad error screen pe na aaye
# whenever we create a function
# ---------------------------------------------------------------------------------------------------------------------------
#parameter & argument
#parameter = jab hum function create karete hai toh we parameter kehlata hai
#argument = jab hum function ko use kar rahe ho aur kuch value bhej rahe ho to woh argument kehlata hai
# ================================
# types of argument

# 1.Default Argument 
# def power(a = 1,b = 1):
#     return a ** b
# power()
# ================================

# 2.Positional argument --> isme jo default behavior hai phala phale wale ke pass jayega aur dusra wala dusre wale ke paas jayega mtlb jis oreder main hum argument bhaj te hai usse order main parameter usko reseive karta hai
# print(power(2,3)) 
# ================================
# keyword argument ---> python main keyword argument ka precedence sab se jayada hai aur ye karta hai name ke according argument receive karta hai
# print(power(b = 3, a = 2))

# ---------------------------------------------------------------------------------------------------------------------------

# *args and ** kwargs
# *args and ** kwargs that are special Python keywords that are used to pass the variable length of arguments to a function

#*args --> Allows us to pass a variable number of non-keyword arguments to a function.
# 1 .args jo hai wo jitne chahe utne argument resieve karne ke liye allowed karta hai
# 2 .args ke aage jo * hai uska mtlb hai ki variable inputs aane waale hai
# 3 .args internally unn inputs ko tuple ke andar dal deta hai
# def multiply(*args):
#     product = 1
#     for i in args:
#         product = product * i

#     return product
# print(multiply(1,2,3,4,4,5,6,6,7,8))
# -----------------
# documentation
# print(print.__doc__)
# -----------------

# **kwargs
# **kwargs allows us to pass any number of keyword argument.
# Keyword arguments mean that they contain a key-value pair, like a python dictionary.
#agar  hame key value pair bhejna hai as input to our function toh hum kwargs use karte hai baake kuch bhi bhajna hai toh hum args bhjte hai
# def display(**kwargs):
#     for(key,value) in kwargs.items():
#         print(key,'->',value)
# display(india = 'delhi',srilanka = 'colombo',nepal = 'kathmandu',russia = 'moscow')

# Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
#The words "args" and "kwargs" are only a convention , you can use any name of you choice
# ---------------------------------------------------------------------------------------------------------------------------
# How functions are executed in memory ?
# -------------------------------------------------------------------------------------------------
# without return statement
# agar kisi function main return nhi hai toh bhi python return bhejega python return main none bhejta hai
# ex :- 
# L = [1,2,3]
# print(L.append(4)) --> yha pe append function jo hai wo kuch return nhi kar rha hai is liye return main none mil rha hai
# ---------------------------------------------------------------------------------------------------------------------------
# Variable Scope
#Global Variable :-jo bhi variable hamare main program scope ke andar aate hai unko hum gloabal variable bolte hai 
#Local Variable :- aur jo bhi variable hamare function ke scope ke andar aate hai unhe hum local variable bolte hai
#  local ko global use nhi kar sakta par global ko local use kar sakta hai

#In this example x is the example of global variable 
# and y is the example of local variable
# ex1:
# def g(y):
#     print(x)
#     print(x + 1)
# x = 5
# g(x)
# print(x)
# ex2:
# yhape x jo hai function ke andar wala uska koi relation nhi hai function ke bhar wale x se
# def f(y):
#     x = 1
#     x +=1
#     print(x + 1)
# x = 5
# f(x)
# print(x)
# ex3: ki agar function ke andar variable nhi hai toh wo global variable ko use kar sakta hai par usme koi change nhi kar sakta hai
# def h(y):
#     x +=1
# x = 5
# h(x)
# print(x)
# ex4:we can change the global variable using global keyword
# def h(y):
#     global x
#     x +=1
# x = 5
# h(x)
# print(x)

# ex5:
# def f(x):
#     x = x + 1
#     print('in f(x) : x = ',x)
#     return x
# x = 3
# z = f(x)
# print('in main program scope : z = ',z)
# print('in main program scope : x = ',x)

# ---------------------------------------------------------------------------------------------------------------------------
# Nested function
# Hum nested function ko main program se excess nhi kar sakte hai andar wale function ko sirf uske bhar wala function access kar sakta hai
# def f():
#     def g():
#         print("inside function g")
#     g()
#     print("inside function f")
# f()
# Ex1:
# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(X) : x = ', x)
#     h()
#     return x
# x = 3
# z = g(x)
# print(z)

# Ex2:
# def g(x):
#     def h(x):
#         x = x + 1
#         print("in h(x):x = ", x)
#     x = x + 1
#     print('in g(x) : x + ', x)
#     h(x)
#     return x
# x = 3
# z = g(x)
# print('in main program scope : x = ', x)
# print('in main program scope : z = ', z)

# ---------------------------------------------------------------------------------------------------------------------------
# Functions are 1st claass citizens in Python
# Functions in python are a datatype jaise int list , tuple,waise hi function will act as a datatype

# type and id
# def square(num):
#     return num **2
# print(type(square))
# print(id(square))
# =====================================================

# reaasign
# x = square
# print(id(x))
# print(x(3))
# =====================================================

# deleting a function
# del square
# print(square(3))
# =====================================================

# storing --> hum kisi function ko bhi list ke andar dal sakte hai
# def square(num):
#     return num **2
# print(type(square))
# print(id(square))
# L = [1,2,3,4,5,6,square]
# print(L[-1](3))
# =====================================================

# functions are immutable dataype aur agar hame ye check karna hai toh set ka use kar sakte hai

# s = {square}
# print(s)
# =====================================================
#returning a function
# yhape f jo hai fuction ko return kar rha hai jiska naam x hai
# hum main program se andar wale prgram ko call kar pa rahe hai kyu ? kyu ki bhar wale function ne andar wale function ka reference bheja
# def f():
#     def x(a,b):
#         return a + b
#     return x
# val = f()(3,4)
# print(val)
# =====================================================

#function as argument
# Ex1: 
# def func_a():
#     print("inside func_a")
# def func_b(z):
#     print('inside func_c')
#     return z()
# print(func_b(func_a))
# =====================================================
# Benefits of using a function
# 1 Code Modularity
# 2 Code Readibility
# 3 Code Reuablility
# =====================================================
# Lambda Function
# A lambda function is a small anonymous function (iss function ka koi naam nhi hota hai)
# A lambda function can take any number of arguments , but can only have one expression
# Syntax
# lambda          a,b          :      a + b
#   ^              ^           ^        ^
#   |              |           |        |
#   |              |           |        |
# Lambda keyword   Parameter   Colon  Expression
# toh over all syntax = 
# lambda a,b: a + b
# Questions on lambda function
# 1.x --> x^2 print(square)
# x = lambda x : x**2
# print(x(4))

# 2.x --> x + y
# a = lambda x,y: x + y
# print(a(2,3))

# =====================================================
# Difference between lambda function vs Normal function
# No name
# Lambda has no return value(infact,return a function)
# lambda is written in 1 line
# not reusable
# more questions on lambda function
# 3.Check if a string has 'a'
# a = lambda s : 'a' in s
# print(a('hello'))
# 4.odd or even
# ans = lambda n: 'even' if n % 2 == 0 else 'odd'
# print(ans(4))
# =====================================================
# Higher order function 
# Higher order function ek aisa function hota hai jiske return main khud ek function aapko milta hai. ek aisa function jo ek function ko return kare  usse hum higher order function kehte hai
# ya fir ek aisa function jo input main dusre function ko recieve kare usko hum higher order function kehte hai

# Example
# def square(x):
#     return x**2

#This is a HOF(Higher order function)
# def transform(f,L):
#     output = []
#     for i in L :
#      output.append(f(i))
#     print(output)
# L = [1,2,3,4,5]
# print(transform(lambda x : x ** 3,L))

# =====================================================
# Map
# Map hamesha do chize excepact karta hai ek lambda function aur ek iterable list hum mapping kar sakte hai using map function

# square the items of a list
# print(list(map(lambda x : x ** 2,[1,2,3,4,5])))

#odd/even labelling of list items
# L = [1,2,3,4,5]
# print(list(map(lambda x : 'even' if x % 2 == 0 else 'odd',L)))

#Fetch names from a list of dict
# users = [
#     {
#         'name':'Rahul',
#         'age':45,
#         'gender':'male'
#     },
#     {
#         'name':'Nitish',
#         'age':33,
#         'gender':'male'
#     },
#     {
#         'name':'Ankita',
#         'age':50,
#         'gender':'femmale'
#     }
# ]
# print(list(map(lambda users:users['name'],users)))

# =====================================================
# filter
# number greater than 5
# L = [3,4,5,6,7]
# print(list(filter(lambda x : x > 5 , L)))

# fetch fruits starting with 'a'
# fruits = ['apple','guava','cherry']
# print(list(filter(lambda x : x.startswith('a'),fruits)))
# =====================================================
# Reduce
# sum of all item
# import functools
# print(functools.reduce(lambda x,y: x + y , [1,2,3,4,5]))
# find min
# print(functools.reduce(lambda x , y : x if x < y else y , [23,11,24,10,1]))
# print(functools.reduce(lambda x , y : x if x > y else y , [23,11,24,10,1]))

# ===================================================================================

# import builtins
# print([f for f in dir(builtins) if callable(getattr(builtins, f))])
