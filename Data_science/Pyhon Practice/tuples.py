# Tuple :- A tuple in python is similar to a list.The difference between the two is that we cannot change the element of a tuple once it is assigned whereas we can change the element of a list
# Tuples is an immutable list . A tuple can not be changed in any way once it is created.
#Characterstics
#Ordered
#Unchangeble
#Allows duplicate
# -----------------------------------------------------------------------------------------
#Plan of attack :-
#Creating a tuple
#Accessing items
#Editing items
#Adding items
#Deleting items
#Operations on tuples
#Tuple Functions

# Creating Tuples :-
#empty
# t1 = ()
# print(t1)
#Create a tuple with a single item
# t2 = ('hello',)
# print(t2)
#homo
# t3 = (1,2,3,4)
# print(t3)
#hetro
# t4 = (1,2.5,True,[1,2,3,4])
# print(t4)
#tuple in tuple
# t5 = (1,2,3,(4,5))
# print(t5)
#using type conversion
# t6 = tuple('hello')
# print(t6)



# Accessing Items :-
# Indexing
# Slicing

# Indexing :-
# print(t3)
# print(t3[0])
# print(t3[-1])
# print(t5[-1][0])

#Slicing :-
# print(t3[-3::])
# print(t3[::-1])

# ------------------------------------------------------------------------------------------------------------
# Editing items
# they are immutable just like strings ek baar agar tuple ban gya toh uske adar ke item hum edit nhi kar sakte 

# ------------------------------------------------------------------------------------------------------------

#Adding items
#Adding items is not possible
# ------------------------------------------------------------------------------------------------------------

#deleting items
#hum yhape tuple ko pura delete kar sakete per uske andar ke items ko hum delete nhi kar sakte 
#deletion tuple main sirf ek case main work karta hai jab hume pura tuple delete karna hota hai tab
# print(t3)
# del t3
# print(t3)
# ------------------------------------------------------------------------------------------------------------

#Operations on tuples :-
# Arithmetic operation (+ and *)
# t1 = (1,2,3,4)
# t2 = (5,6,7,8)
# t3 = (10,20,30,40,50,5,6,7,8)
# print(t1 + t2 + t3)
# print(t1*3 + t3)
# 
# Membership Operations
# print(1 in t1 )

#Iterations Operations
# for i in t1:
#     print(i)

# ------------------------------------------------------------------------------------------------------------

# tuple functions:-
#len/sum/min/max/sorted
# t = (1,2,3,4)
# print(len(t))
# print(sum(t))
# print(min(t))
# print(max(t))
# print(sorted(t,reverse= True))

#count
# t = (1,2,3,4,5,6)
# print(t.count(5))
# print(t.count(-244))

#index 
# t = (1,3,3,5,54,5)
# print(t.index(1))

# ---------------------------------------------------------------------------------------------
# Difference between lists and tuples
# Syntax
# Mutability
# Speed --> tuples is faster than lists
# Memory
# Built in functionality
# Error prone
# Usability

# -----------------------------------------------------------------------------------------------
#SPECIAL SYNTAX:-
# Tuple unpacking:-
# a,b,c = (1,2,3)
# print(a,b,c)
# ----------------------------------------------------------------------------------------------
# a = 1
# b = 2
# a,b = b,a
# print(a,b)
# ------------------------------------------------------------------------------------
# a,b,*others = (1,2,3,4) #-->is line main a = 1,b = 3 and bakki jitna bhi bach wo iss others main chala jayega aur list ke form main store ho jayega
# print(a,b)
# print(others)
# --------------------------------------------------------------------------------
#zipping tuples --> item by item do iterables ka value ke upar iterate karta hai
# a = (1,2,3,4)
# b = (5,6,7,8)
# print(list(zip(a,b)))

# ------------------------------------------------------------------------------------
# jitne bhi read operations hai wo sab tuples pe apply hote hai aur jitne bhi write operations hai wo apply nhi hote hai

# tuple comprehension

# tuple(expression for item in iterable if condition)

t = (tuple(i for i in range(0,5)))
print(t)
t = tuple(i * i for i in range(5))
print(t)