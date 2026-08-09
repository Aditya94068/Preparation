#Arithmetic Operator
#Relational Operator 
#Logical Operator
#Assignment Operator
#Membership Operator
#Bitwise Operator




#Arithmetic Operator
# print(5+4)
# print(5-4)
# print(5*4)
# print(5/4)
# print(5//4) #Integer Division
# print(5%4)
# print(5**4) #Power-OFF 



# #Relational Operator
# print(4<5)
# print(4>5)
# print(4<=5)
# print(4>=5)
# print(4==5)
# print(4!=5)



# #Logical Operator
# print(1 and 0) 
# print(1 or 0)
# print(not 1) #python internally 0 ko false aur 1 ko true bna deta hai



# #Bitwise Operators ---> Bitwise operators operates on binary values
# #Bitwise and 
# print(2 & 3)
# #Bitwise Or operator
# print(2 | 3)
# #Bitwise xor
# print(8 ^ 4)
# #Bitwise not
# print(~3)
# #Bitwise left shift operator
# print(4 >>2)
# #Bitwise Right shift operator
# print(4 << 2)



# Assignment Operator
# =
# a = 2
# a += 2
# a = a + 2
# # python c and c++ ki tarah a++ ya ++a  aur a-- ya --a use nhi hota hai
# # yha pe sirf do tarike hote hai increment karne ke
# # 1. a = a + 1
# # 2. a += 1
# print(a)

# MemberShip Operator
# in/not in 
# print('D' in 'Delhi')
# print('D' not in 'Delhi')
# print(1 in [2,3,4,5,6])
# print(1 not in [2,3,4,5,6])

# n = int(input("Enter a number :"))
# a =  n % 10
# n = n//10
# b =  n % 10
# n = n//10
# c =  n % 10
# print(a + b + c)

# If-else Statement in python

# Example of if-else statement
# login program and identation
# email -> adityavaishnav633@gmail.com
# password ->1234

# email = input("Enter email :")
# password = input('Enter a password :')
# if email == 'adityavaishnav633@gmail.com' and password == '1234':
#     print("Welcome")
# elif email =='adityavaishnav633@gmail.com' and password != '1234':
#     print("Incorrect Password")
#     password = input('Enter a password again :')
#     if password == '1234':
#         print('welcome')
#     else:
#         print("Not correct")
# else:
#     print("Not Correct")


# if-else examples
# 1.Find the min of 3 gives numbers
# a = int(input("Enter a first number :"))
# b = int(input("Enter a second number :"))
# c = int(input("Enter a third number :"))

# if a == b and a == c:
#     print("All are same")
# elif a <  b and a < c :
#     print("Is smallest number is :",a)
# elif b < c:
#     print('smallest is ', b)
# else :
#     print("smallest is ", c)


#menu driven calculator
# fnum = int(input("Enter the 1st number : "))
# snum = int(input("Enter the 2nd number : "))

# op =input("Enter the operation : ")
# if op == '+':
#     print(fnum + snum)
# elif op == '-':
#     print(fnum - snum)
# elif op == '*':
#     print(fnum * snum)
# else:
#     print(fnum / snum)

#menu driven program
# menu = input("""
# Hi! how can I help you
# 1.Enter 1 for pin Change
# 2.Enter 2 for balance check
# 3.Enter 3 for withdrawl
# 4.Enter 4 for exit
# """)
# if menu == '1':
#     print("Pin change")
# elif menu == '2':
#     print("balance check")
# elif menu == '3':
#     print("Withdrawl")
# else :
#     print("Exit")

# Modules in Python
# Modules -->ek python file hai jike andar kuch function likhe hai main kya kar sakte hu ki main uus file ko import karke apne code main la sakta hu uus ye hoga ki main dusre ke likhe hue function ko use kar sakta hu 
# 1. math
# 2.keywords
# 3.random
# 4.datetime

# import math
# print(math.factorial(5))
# print(math.floor(4.5))
# print(math.sqrt(144))


#keyword
# import keyword
# print(keyword.kwlist)

#random module
# import random
# print(random.randint(1,100))

#datetime module
# import datetime
# print(datetime.datetime.now())

#how many modules is present we can use this syntax for understand that how many modules are present in python
# help('modules')





# loops in python
# While loop
# For loop

#while loop
# program to print table
# number = int (input('Enter the number '))
# i = 1
# while i <= 10:
#     print(number , '*', i ,'=',number * i)
#     i += 1

# WEBSITE -->   https://pythontutor.com/render.html#mode=display YE WEBSITE USE HOTI PYTHON KE CODE KO VISUALISE KARNE MAIN


#while loop with else
# x = 1
# while x < 3:
#     print(x)
#     x +=1
# else:
#     print("limit Crossed")




# Guessing game
#generate a random integer between 1 and 100
# import random
# jackpot = random.randint(1,100)
# guess = int(input('guess karo : '))
# counter = 1
# while guess != jackpot:
#     if guess < jackpot:
#         print('wrong ! guess higher')
#     else : 
#         print('wrong!guess lower')
#     guess = int(input("guess karo :"))
#     counter +=1
# else :
#     print("correct guess")
#     print('attempts', counter)


# for loop in python
# print 1 to 10
# for i in range(1,11): # 11 is not included 
#     print(i)
# Example 1 : print odd value used only for loop dont use any condition
# for i in range(1,11,2): # range(start , end , step)
#     print(i)
# Example 2 : print reverse number 
# for i in range(10,0,-1):
#     print(i)


# Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.


# 10 % --> 10 per jo hai wo hota hai 0.1 means 10% ko decimal main conver karne ke liye hume 10 divided by hundered karna padta hai 10 / 100 = 0.1

# curr_pop = 10000
# for i in range(10,0,-1):
#     print(i,curr_pop)
#     curr_pop = curr_pop /1.1





# Sequence sum --> this is the exponentiation series
# 1/1! + 2/2! + 3/3! + ... 
# n = int(input("Enter number :"))
# fac = 1
# result = 0
# for i in range(1,n+1):
#     fac = fac * i
#     result = result + i / fac
# print(result)

# nested loops
#print pair ---> unique pairs
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# pattern 1
# n = int(input("Enter a number :"))
# for i in range(1,n + 1):
#     for j in range(1,i + 1):
#         print('*',end ='')
#     print()


# n = int(input("Enter a number :"))
# for i in range(1,n + 1):
#     print('*'*i)


# pattern 2
# n = int(input("Enter a number :"))
# for i in range(1,n + 1):
#     for j in range(1,i+1):
#         print(j,end = "")
#     for k in range(i - 1,0,-1):
#         print(k,end ='')
#     print()

# Break statement
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# lower = int(input("Enter a number :"))
# higher = int(input("Enter a number :"))
# for i in range(lower,higher + 1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# continue statement
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

  
# pass statement
# for i in range(1,10):
#     pass

