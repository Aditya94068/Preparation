# list is a data type where you can store multiple items under 1 name . More technically,lists act like dynamic arrays which means you can add more items on the fly
# ---------------------------------------------------------------------------------------------
# Array Vs lists
# Fixed Vs Dynamic Size
# Convenience -> Hetrogeneous
# Speed of Execution
# Memory
# ---------------------------------------------------------------------------------------------
#Python list joh hai wo ek object ko point karta hai 
#list ke andar addresses (references) hote hai
#Actual values heap memory me alag objects hote hain
# ---------------------------------------------------------------------------------------------
#Characterstics of list

#Ordered
# L = [1,2,3]
# L2 = [3,2,1]
# print(L == L2) # Python stricly ordered ko follow karta hai

# #Changeable/Mutable
# L[0] = 1000
# print(L)

# #Hetrogeneous list
# L = ["aditya",20,"3 year"]
# print(L)

#Can have duplicates
#Are dynamic
#can be nested
#items can be accessed
#can contain any kind of objects in python


# ---------------------------------------------------------------------------------------------
# Creating a list
#Empty
# print([])
#1D -> Homo
# print([1,2,3,4,5])
# #2D
# print([1,2,3,4,[4,5]])
# #3D
# print([[[1,2],[3,4]],[[5,6],[7,8]]])
# #Hetrogeneous
# print([1,True,5.6,5 + 6j,'Hello'])
# #Using type conversion
# print(list('hello')) # ye kya karega ki her correct ko alag - alag item bna dega aur list main dal dega
# ---------------------------------------------------------------------------------------------

# Accessing items from a list
#Indexing
# L = [[[1,2],[3,4]],[[5,6],[7,8]]]
#Positive indexing
# print(L[0])
# print(L[3][1])
# print(L)
# print(L[0])
# print(L[1])
# print(L[0][0])
# print(L[0][1])
# print(L[1][0])
# print(L[1][1])
# print(L[0][0][0])
# print(L[0][0][1])
# print(L[0][1][0])
# print(L[0][1][1])
# print(L[1][0][0])
# print(L[1][0][1])
# print(L[1][1][0])
# print(L[1][1][1])
# ---------------------------------------------------------------------------------------------
#Negative indexing
# print(L[-1][-2])
# print(L[-2])
# print(L[-3])
# #Slicing
# L = [1,2,3,4,5,6]
# print(L[0::2])
# print(L[-5:-2:2])
# print(L[::-1])
# ---------------------------------------------------------------------------------------------
#4D Array
# L = [[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15]]]]
# print(L[0][0][0][2])

# ---------------------------------------------------------------------------------------------
#Adding Items to a list
#Append --> Append jo hai wo single (ek) item ko list ke last main append kar deta hai
# L = [1,2,3,4,5]
# L.append("aditya")
# print(L)
# L.append(["aditya",5,6,7,8]) #ye pe append jo a is puri list ko ["aditya",5,6,7,8] as a single item samj ke list main append kar dega
# print(L)

#extend -->extend jo hai wo multiple items ko add karne ke liye hota hai
# L = [1,2,3,4,5]
# L.extend(["aditya",5,6,7,8])
# print(L)
# L.extend('delhi') # yha pe extend kya kar rha hai delhi ko ek ek character tod kar add kar rha hai like this [1,2,3,4,5,'d','e','l','h','i']
# print(L)

#insert -->apni desired location pe add karne ke liye hum insert function ka use karte hai
# L = [1,2,3,4,5]
# L.insert(1,100)
# print(L)

# -------------------------------------------------------------------------------------------------------
# Editin items in a list
#List are mutable

#Editing with indexing
# L = [1,2,3,4,5]
# L[-1] = 500
# L[0] = 1000
#Editing with slicing
# L[1:4] = [200,300,400]
# print(L)
# -------------------------------------------------------------------------------------------------------
#Deleting items from a list

#del
# L = [1,2,3,4,5]
# print(L)
#indexing
# del L[-1]
# #slicing
# del L[1:3]
# print(L)
# del L
# print(L) # here we are deleting whole list 
# 

#remove --> iss function main hum directly value de sakte jo hume remove karni hai
# L = [1,2,3,4,5]
# L.remove(5)
# print(L)


#pop --> pop ke andar hum agar index dete hai toh wo uss index ki particlar value delete karta hai 
# per agar hum koi value nhi dete hai toh woh last index pe rakhi value ko delete kar dega aur ye uska default behavior hai
# L = [1,2,3,4,5]
# L.pop()
# print(L)


#clear --> ye function list main rakhe saare values ko delete kar deta hai list ko empty bna deta hai
# L = [1,2,3,4,5]
# L.clear()
# print(L)

# ------------------------------------------------------------------------------------------------------

#Operations on lists
# Arithmetic
# Membership
# Loop
# ======================================
# Arithmetic
# L1 = [1,2,3,4]
# L2 = [5,6,7,8]

#Concatenation/Merge
# print(L1 + L2)
# print(L1 * 3)
# =========================================

# # Membership
# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]
# print(5 not in L1)
# print(5 in L2[4])
# =============================================

# L1 = [1,2,3,4,5]
# L2 = [1,2,3,4,[5,6]]
# L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
# for i in L1:
#     print(i)
# for i in L2:
#     print(i)
# for i in L3:
#     print(i)
#--------------------------------------------------------------------------------------------------------------
#List function
#len/min/max/sorted
# L = [2,1,5,7,0]
# print(len(L)) # kitne function hai list main wo nikal ke deta hai
# print(min(L)) 
# print(max(L))
# print(sorted(L,reverse= True))

#count ---> this function is used to count the particular  elment in the list
# L = [1,2,1,3,4,1,5]
# print(L.count(5))


#index --> ye function use hota hai kisi element ka index find karne ke liye agar list main duplicate element hai toh ye function us element ka first occurance ka index return karta hai
# L = [1,2,1,3,4,1,5]
# print(L.index(5))


#reverse --> ye function orginal list ko reverse kar deta hai
# L = [1,2,1,3,4,1,5]
#permeantly reverses the list
# L.reverse()
# print(L)


#sort(vs sorted) ---> sort main parmenent changes hote hai list main but sorted function original list ko touch nhi karta wo memory main new list bnata hai aur usse sort karta hai
# L = [1,2,1,3,4,1,5]
# print(L)
# print(sorted(L))
# print(L)
# L.sort()
# print(L)

#copy -->ye ek shallow copy bnata hai ye function memeory main ek copy create karta hai list ka
# L = [2,1,5,7,0]
# print(id(L))
# L1 = L.copy()
# print(L1)
# print(id(L1))
# print(L[::-1])
# print(L)

#--------------------------------------------------------------------------------------------------------------
# List Comprehension
#List Comprehension provides a concise way of creating lists.
#newlist = [expression for item in iterable if condition == True]
#Adventages of list Comprehension:-

# 1.More time-efficien and space-efficient than loops
# 2.Require fewer lines of code.
# 3.transforms iterative statement into a formula.

#Examples to understand the list comprehension :-

#Add 1 to 10 numbers  to a list

  # Normal loop
# L = []
# for i in range(1,11):
#     L.append(i)
# print(L)

   #use  list comprehension
# L = [i  for i in range(1,11)]
# print(L)
# ==============================================
#scalar multiplication on a vector --> using list comprehension
# v = [2,3,4]
# s = -3
# ans: [-6,-9,-12]
# x = []
#NORMAL LOOP
# for i in v:
#     x.append(i*s)
# print(x)

#list comprehension
# print([s*i for i in v])
# v-->iterable list
# i-->list ke har element
# s * i ---> calculation
# [] ---> nayi list banane ke liye
# ==================================================

#Add squares
# L = [1,2,3,4,5]
# square = []
# square = [i ** 2 for i in L]
# print(square)

# =============================================================
#Print all numbers divisible by 5 in the range of 1 to 50
# lst = []
# lst = [i for i in range(1 , 51) if i % 5 == 0 ]
# print(lst)

# ===================================================================================
#find languages which start with letter p
# languages = ['java','python','php','c','javascript']
# print([language for language in languages if language.startswith('p')])

# ================================================================================
#Nested if with list Comprehension
# basket = ['apple','guava','cherry','banana']
# my_fruits = ['apple','kiwi','grapes','banana']
# add new list from my fruits and items if the fruit exists in basket and also starts with 'a'
# result = []
# # result = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
# print(result)
# ==============================================================================================
#Print a (3,3) matrix using list comprehension -> Nested list comprehension
# matrix = [] 
# matrix = [[i * j for i in range(1,4)] for j in range(1,4)]
# print(matrix)

# ==========================================================================================
#cartesian products --> list comprehension on 2 lists together
# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
# result = [i * j for i in L1 for j in L2]
# print(result)

# ==========================================================================================
# 2 Ways to traverse a list
# itemwise
# indexwise

#itemwise
# L = [1,2,3,4]
# for  i in L:
#     print(i)

#indexwise
# L = [1,2,3,4]
# for i in range(0,len(L)):
#     print(L[i])

# ======================================================================================
#Zip -->
# L1 = [1,2,3,4]
# L2 = [-1,-2,-3,-5]
# print(list(zip(L1,L2)))
# print([i + j for i,j in zip(L1,L2)])
# -----------------------------------------------------------------------------------------

#can contain any kind of objects in python
#python list ke andar hum function classes object and methods ko bhi rakh sakte hai
# L = [1,2,print,type,input]
# print(L)


# -----------------------------------------------------------------------------------------
# Disadvantages of Python lists
#Slow
#Risky usage
#eats up more memory

# a = [1,2,3]
# b = a.copy()
# print(a)
# print(b)
# a.append(4)
# print(a)
# print(b)
# ------------------------------------------------------------------------------
# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 

# L = [1,2,3,4,5,6]
# L1 = []
# L2 = []
# L1 = [i for i in L if i % 2 == 0]
# print(L1)
# L2 = [i for i in L if i % 2 != 0]
# print(L2)
# ---------------------------------------------------------------------------------
# How to take list as input from user
# n = int (input("Enter the size of the list :"))
# lst = []
# for i in range(n):
#     lst.append(int(input("Enter a number :")))
# print(lst)
# ---------------------------------------------------------------------------------
# Write a program to merge 2 list without using the + operator
# L1 = [1,2,3,4]
# L2 = [5,6,7,8]
# for item in L2:
#    L1.extend(L2)
# print(L1)
# for item in L2:
#    L1.append(L2)
# print(L1)
# ---------------------------------------------------------------------------------
# Write a program to replace an item with a different item if found in the list 
# replace 3 with 300
# L = [1,2,3,4,5,3]
# key = 3
# for i in range(0,len(L)):
#     if key == L[i]:
#         L[i] = 300
# print(L)
# ----------------------------------------------------------------------------------------------
# Write a program that can convert a 2D list to 1D list
# lst = [[1,2,3,4],[5,6,7,8]]
# print(lst)
# print(type(lst))

# Summary
# List	                     Dimension
# [1,2,3]	                  1D
# [[1,2,3]]	                  2D
# [[[1,2,3]]]	               3D
# [[1,2,3,4],[5,6,7,8]]     ✅2D
# -------------------------------------------------------------------------------------------------
# Write a program to remove duplicate items from a list
# method 1:
# L = [1,2,1,2,3,4,5,3,4]
# unique_list = []
# for item in L:
#     if item not in unique_list:
#         unique_list.append(item)
# print(unique_list)

# unique_list = []
# for item in L:
#     if item not in unique_list:
#         unique_list.append(item)
# print(unique_list)

# method 2:
# L = [1,2,1,2,3,4,5,3,4]
# L1 = set(L)
# L3 = list(L1)
# print(L3)
# --------------------------------------------------------------------------------------------------

# Write a program to check if a list is in ascending order or not
# METHOD 1 :
# lst = [1,2,3,4,5]
# x = 0
# flag = False
# while x < len(lst) - 1:
#     if lst[x] > lst[x + 1] :
#         flag = True
#         break
#     x = x + 1
# if flag:
#     print("List not in ascending order")
# else:
#     print("List is ascending order")

# METHOD :2
# lst = [1,2,3,4,5]
# if lst == sorted(lst):
#     print("List is sorted in asceding order")
# else:
#     print("List is not sorted in ascending order")