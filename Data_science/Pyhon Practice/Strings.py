# valid string format
# s = 'Hello'
# print(s)
# s = "hello"
# print(s)
# # multiline string 
# s = '''hello'''
# s = """hello"""
# print(s)
# print('aditya"vaishnav"')
# ----------------------------------------------------------------------------
# Indexing 
# s = 'hello world'
# # Positive indexing
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# print(s[5])
# # Negative indexing
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-5])
# ---------------------------------------------------------------------------------------------
# Slicing
# s = "hello World"
# print(s[0:12:3]) # start , stop , step size
# print(s[6:0:-2])

# reverses string 
# print(s[::-1])

# print(s[-5:])
# print(s[-1:-6:-1])
# print(s[-7:-12:-1])

# in python strings are immutable

# Delete string
# s = 'hello world'
# del s
# print(s)


# s = 'hello world'
# del s[-1:-5:2] # error this is not possible pura string delete ho sakta hai uska part delete nhi hoga kyu ki agar hum uska koi part delete karte hai toh uska mtlb hai ki hum string main change kar rahe per string main koi change possible nhi hai string is immutable
# print(s)
# ------------------------------------------------------------------------------
# Operations on string 
# Arithmetic Operations
# Relational Operations
# Logical Operatioins
# loops on string 
# Membership Operations
# ------------------------------------------------------------------------------
# Arithmetic Operations
#String Concatenation
# print('helhi' + ' ' + 'mumbai')
# multiplication Operator
# print('delhi' * 5 )
# ------------------------------------------------------------------------------
# Relational Operations
# print('delhi' != 'delhi')
# print('mumbai' > 'pune') # lexicographically comparison 
# print('Pune' > 'pune') # ASCII value of 'P = 80' is less than 'p= 112'
# ------------------------------------------------------------------------------
# logical Operation
# print('hello' and 'world')
# print('hello' or 'world')

# print('' and 'world')
# print('hello' and '')

# print('hello' or '')
# print('' or 'world')

# print(not '')
# print(not 'hello')

# ------------------------------------------------------------------------------
# loops on string 

# for i in 'hello' :
#     print(i)

# for i in 'hello' :
#     print(i,end='')
# print()
# for i in 'delhi':
#     print('pune')
# -------------------------------------------------------------------------------------
# Membership Operations
# print('D'  in 'Delhi')
# print('D' not in 'Delhi')

# ---------------------------------------------------------------------------------------------
#String function
# len
# max
# min
# # sorted

# # len
# print(len("Aditya vaishnav"))

# # max
# print(max("Aditya vaishnav"))

# # min
# print(min("hellow World"))

# #sorted
# print(sorted("Aditya Vaishnav"))
# # sort in reverse
# print(sorted("Aditya vaishnav",reverse = True))


# --------------------------------------------------------------------------------------
# function which are only applicable on strings
# 1. Capitalize
# s = 'aditya vaishnav'
# print(s.capitalize())

# 2. Title --> title aur Capitalize ka joh behavior same hai kyu ki har word ka phala letter capital hota hai
# print(s.title())

# 3 .upper()
# print(s.upper())

# # 4.lower()
# print(s.lower())

# swapcase --> capital wale ko lower kar dega aur lower wale ko capital kar dega
# s =" HelLo WoRld"
# print(s.swapcase())


# ----------------------------------------------------------------------------------------------------

# More and comman function
# 1.count
# print("my name is Aditya".count('i'))

# 2.find
# print("my name is Aditya".find("is"))

#3.index -->index aur find function same hai per difference      ye hai ki hum find function ke andar hum character ke sath substring bhi find kar sakte hai per index function ke andar hum sirf character ka index find kar sakte hai
# print("my name is Aditya ".index('a'))


# ------------------------------------------------------------------------------------------------
#koi string particular chizz se start ho rha hai ki nhi ya kisi particular chizz se end ho rha hai ki nhi ye check karne ke liye hamare pass doh function hote hai

# 1.endswith --> true aur false return karte hai ye function
# print('my name is Aditya'.endswith('itya'))
# 2.startswith -->true aur false return karte hai ye function
# print('my name is Aditya'.startswith('m'))

# ----------------------------------------------------------------------------------------------------
# format --> format function string ke andar variable ki value dal ne ka kaam karta hai

# name = 'Aditya'
# gender = 'male'
# print('Hi my name is {} and I amd a {}'.format(name , gender))
# print('Hi my name is {1} and I amd a {0}'.format(gender,name))
# print(f"my name is {name} , I am {gender}")

# -----------------------------------------------------------------------------
# isalnum(),isalpha(),isdigit()/isidentifier() --> bool methods of string

# 1 . isalnum()
# print("aditya1244".isalnum())  # alpha numeric character se milkar bna hua hai ya toh alphabet se milkar bna hua hai ya toh character se 

# print("aditya12234%".isalnum()) # ye valid nhi hai kyu ki isme special character % hai

# 2 . isalpha()
# print("aditya".isalpha())

# 3 . isdigit()
# print("1234".isdigit())

# 4 . isidentifier() --> ye use hota hai ki variable ka name valid ha ya nhi
# print('1name'.isidentifier()) 
# print('name1'.isidentifier()) 
# print('first_name'.isidentifier()) 

# -----------------------------------------------------------------------------------------------------

# Split/join function
#1.split() --> ye ek list ke andar dal deta hai saare characters ko split karne ke baaad . agar hum kuch pass nhi karege toh space ke bases pe break karega aur agar hum kuch pass karenge toh uss chizz ke bases pe break karega

# print("hi my name is aditya ".split())
# print("hi my name is aditya ".split('i'))
# print("hi my name is aditya ".split('is'))


# 2.join()
# print(" ".join(['hi', 'my', 'name', 'is', 'aditya']))
# print("-".join(['hi', 'my', 'name', 'is', 'aditya']))
# print("*".join(['hi', 'my', 'name', 'is', 'aditya']))

# ---------------------------------------------------------------------------------------------------------------
# Replace
# print('hi my name is aditya'.replace('aditya','adi'))


# -----------------------------------------------------------------------------------------------------------------------

# strip --> ye function string main se sare trailing space hta deta hai
# print('aditya     vaishnav  '.strip())


# -------------------------------------------------------------------------------------------------------------------------------
#Find the length of a given string without using the len() function
# s = input("Enter the string :")
# count = 0
# for i in s:
#     count = count + 1
# print(count)

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Extract username from a given email
# Eg if the email is nitish24singh@gmail.com
#then the username should be nitish24singh
# Use both function find and index
#1.find function
# email = input("Enter a email : ")
# pos = email.find("@")
# print(email[0:pos])

#2.index function
# email = input("Enter a string :")
# pos = email.index("@")
# print(email[0:pos])


# -----------------------------------------------------------------------------------------------------------------------
#Count the frequency of a particular character in a provided string.
#Eg 'hello how are you' is the string , the frequency of h in this string is 2
# s = input("Enter a string :")
# term = input("What would you like to search for :")
# count = 0
# for i in s :
#     if i == term:
#         count = count + 1
# print(term,count)

#--------------------------------------------------------------------------------------------------------------------------------------------------
#write a program which can remove a particular character from a string
# s = input("Enter a string :")
# ch = input("Enter the character which want you to remove :")
# result = ""
# for i in s:
#     if i != ch:
#         result += i
# print(result)

# ------------------------------------------------------------------------------------------
#write a program that can check whether a given string is palindrome or not
# s1 = input("Enter a string :")
# i = 0 
# j = len(s1)-1
# flag = True
# while(i<=j):
#     if s1[i] == s1[j]:
#         i = i + 1
#         j = j - 1
#     else:
#         flag = False
#         break
# if flag:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")

# ------------------------------------------------------------------------------------------------------------
# Write a program to count the number of words in a string without split()
# s1 = input("Enter the string :")
# L = []
# temp = ''
# for i in s1:
#     if i != ' ':
#         temp +=i
#     else:
#         L.append(temp)
#         temp = ' '
# L.append(temp)
# count = 0
# for i in L:
#     count = count + 1
# print(count)

# ------------------------------------------------------------------------------------------------------------
#Write a pytho program to convert a string to title case without using title()
# s1 = input("Enter the string :")
# L = []
# for i in s1.split():
#     L.append(i[0].upper() + i[1:].lower())
# print(L)
# print(" ".join(L))

# ------------------------------------------------------------------------------------------------------------
# Write a program that can convert an integer to string
# number = int(input("Enter a number :"))
# digits = "0123456789"
# result = ""
# while number != 0:
#     result = digits[number % 10] + result
#     number = number//10
# print(result,type(result))
