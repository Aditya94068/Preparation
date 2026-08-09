# Our focus - Time
#Techniques to measure time efficiency
#Techniques
# ------------------------
# 1.Measuring Time to execute
# import time
# start = time.time()
# for i in range(1,1000):
#     print(i)
# i = 0
# while i != 100:
#     print(i)
#     i = i + 1
# end = time.time()
# print(end - start)
#issue --> it is system independent like machine depended techniques like kis machine ke upar ye program execute ho rha hai

# Problems with this approach --- true
#Different time for different algorithm --- false
#Time varies if implementation changes  --- false
#Different Machines different time   --- false
#Does not work for extremely small input  --- false
#Time varies for different inputs , but can't establish a relationship --- false
#------------------------------
# 2. Counting Operations
# assume these steps take
# constant time
# 1.mathematical operations
# 2.camparisons
# 3.assignments
# 4.accessing objects in memory
#then count the number of operations executed as function of size of input
# Problems with this approach

#Different time for different algorithm --- True
#Time varies if implementation changes  --- False
#Different Machines different time     --- True
#Does not work for extremely small input  --- False
#Time varies for different inputs , but can't establish a relationship   --- True

#----------------------------------
# 3. What do we want
# 1.We want to evaluate the algorithm
# 2.We want to evaluate scalability
# 3.We want  to evalueate in terms of input size
#Different inputs change how the program Runs
#a function that searches for an elment in a list
# def search_for_elmt(L,e):
#     for i in L:
#         if i == e:
#             return True
#     return False
# When e is first element in the list --> Best Case
# When e is not in list --> worst case
# When look through about half of the elements in list --> Average Case
# Orders of Growth
# Goals
# want to evaluate program's efficiency when input is very big
# want to express the growth of program's run time as input size grows
# want to put an upper bound on growth - as tight as possible 
# do not need to be precise : "order of" not "exact" growth 
# we will look at largest factors in run time (which section of the program will take the longest to run ?)

#Exact steps vs O()
# def fact_iter(n):
#     """assumes n ans int>=0"""
#     answer = 1
#     while n > 1:
#         answer *= n
#         n -= 1
#     return answer
#Computes Factorial
#Number of steps:
#worst case asymptotic complexity:
# 1.ignore additive constants
# 2.ignore multiplicative constants
# solve the given equation
# n ^ 2 + 2n + 2 ----> O(n ^ 2)
# n ^ 2 + 1000000n + 3^1000 -----> O(n ^ 2)
# log(n) + n + 4 ------> O(n)
# 0.0001 * n * log(n) + 300n ------> o(n*log(n))
# 2n ^ 30 + 3 ^ n ----> O(3 ^ n)
# -------------------------------------------------------
#Types of orders of growth
# Constant ---> O(1)
# linear ---->O(n)
# quadratic ---->O(n^2)
# logarithmic -----> O(log(n))
# nlogn  ------> O(nlogn) --->sorting algorithm (merge sort)
# exponential ------> O(2 ^ n)
# -------------------------------------------------------------------
# Law of addition 
#Law of addition for o():
# 1. used with sequental statements
# 2.O(f(n)) + O(g(n)) is O(f(n) + g(n))
# 3.for example,
# n = int(input("Enter a number :"))
# for i in range(n):
#     print('a')
# for j in range(n * n):
#     print('b')
# is O(n) + O(n * n) = O( n + n ^ 2) = O(n ^ 2) because of dominant term

# --------------------------------------------------------------------------------
# law of multiplication
# Law of Multiplication for O():
# 1. used with nested statements / loops
# 2.O(f(n)) * O(g(n)) is O(f(n) * g(n))
# for example,
# n = int(input("Enter a number :"))
# for i in range(n):
#     for j in range(n):
#         print('a')
# is O(n) * O(n) = O(n * n) = O(n ^ 2) because the outer loop goes n times and the inner loop goes n times for every outer loop iter.
# ----------------------------------------------------------------------------------------------
#Find the Time Complexity of the following code
# 1.
# number = int(input("Enter a number :"))
# digits = "0123456789"
# result = ""
# while number != 0:
#     result = digits[number % 10] + result
#     number = number//10
# print(result,type(result))
# timecomplexty of this code  --> O(log(n))

# 2.
# L = [1,2,3,4]
# sum = 0
# for i in L:
#     sum = sum + i
# product = 1
# for i in L:
#     product = product * i
# print(sum,product)
# TC : O(n) + O(n) = O(2n) = O(n)

#3.
# A = [1,2,3,4]
# B = [5,6,7,8]
# for i in A:
#     for j in B:
#         print(i,j)
# TC : O(n^2)
# A = [1,2,3,4]
# B = [5,6,7,8]
# for i in A:
#     for j in B:
#         for k in range(1000000):
#             print(i,j)
# TC : O(n) * O(n) * O(1000000) = O(10000000*n^2) = O(n^2)

# 4.
# L = [1,2,3,4,5]
# for i in range(0,len(L)//2):
#     other = len(L) - i -1
#     temp = L[i]
#     L[i] = L[other]
#     L[other] = temp
# print(L)
# TC : O(n)

# 5.
# n = 10
# k = 0
# for i in range(n // 2,n):
#     for j in range(2,n,pow(2,j)):
#         k = k + n /2
# print(k)
# TC : O(nlog(n))

# 6.
# a = 10
# b = 3
# if b <=0:
#     print(-1)
# div = a // b
# print(a - div - b)
# TC : O(1)

#7.
# n = 345
# sum = 0
# while n > 0:
#     sum = sum + n % 10
#     n = n//10
# print(n //10)

# TC : O(log(n))

#8.
# def fib(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
# print(fib(50))
# TC : O(2 ^ n)

# 9.
# Subset Algo
# TC = 2 ^ n

# 10.
#3T(n-1) if n > 0 
# T(n) = {1,otherwise}
# TC = O(3^n)

# 11.
#2T(n-1) - 1 if n > 0 
# T(n) = {1,otherwise}
# T(n) = 2T(n-1) - 1
#      = 2[2T(n-2) - 1] - 1
#      = 2 ^ 2T(n-2) - 2 - 1
#      = 2 ^ 2[2T(n-3) - 1] - 2 -1
#      = 2 ^ 3 T(n-3) - 2 ^ 2 - 2 ^ 1 - 2 ^ 0
#      = 2 ^ n T(n - n) - 2 ^ n-1 - 2 ^ n-2 ------2 ^ 1 - 2 ^ 0
#      = 2 ^ n - [2 ^ n -1 + 2 ^ n-2 + ------+2^1+ 2^0]
#      = 2 ^ n - [2 ^ n - 1]  = 2^n - 2 ^ n+1
#      = O(1) ---> constant