# result  = []
# result = [i **2 for i in range(1,11)]
# print(result)

# result =[i for i in range(1,51) if i % 2 == 0] 
# print(result)

# result =[i for i in range(1,51) if i % 2 != 0]
# print(result)

# lst = [1,2,3,4,5,6,7,8,9,10]
# result = [str(i) for i in lst ]
# print(result)

# L = ["aditya","sumit","nita","suni"]
# result = [i.upper() for i in L]
# print(result)

# L = ["aditya","sumit","nita","sunil"]
# result = [i for i in L if len(i) > 5]
# print(result)

# result = [i ** 3 for i in range(1,21)]
# print(result)

# result = [i for i in range(1 ,100) if i % 3 == 0]
# print(result)

# L = [-2,-4,5,6,7,-1,-5,12,6]
# result = [i for i in L if i > 0 ]
# print(result)

# result = [abs(i) for i in L]
# print(result)

# result = [i for i in range(10,0,-1)]
# print(result)

# L = [-2,-4,5,6,7,-1,-5,12,6]
# result = [0 if i < 0   else i for i in L ]
# print(result)

# string = "aditya vaishnav"
# result = [i for i in string]
# print(result)


# string = "Aditya vaishnav"
# vowels = "aeiou"
# result = [i for i in string if i.lower() not in vowels]
# print(result)

# string = "Aditya vaishnav"
# result = [ord(i) for i in string]
# print(result)

# L = [2,3,4,5,6,7,8,9,11,12,14,13,15,17]
# result = [i**2 if i % 2 == 0 else i for i in L ]
# print(result)


# L = ["aditya","sumit","nita","sunil","akshay"]
# result = [i for i in L if i[0] == "a"]
# print(result)


# L = [[1,2,3],[4,5,6],[7,8,9]]
# result = [item for row in L for item in row]
# print(result)

# result= list(x**2 for x in range(1,11))
# print(result)

# result =[[]]
# result= [[f"{j}*{i}= {i * j}"for i in range(1,11)]for j in range(1,11)]
# print(result)

# lst1 = [1,2,3,4]
# lst2 = [5,6,7,8]
# result = [(i,j) for i in lst1 for j in lst2]
# print(result)

# result = [i for i in range(1,101) if i % 3 == 0 and i % 5 == 0]
# print(result)

# lst_str = ['1','2','3','4','5','6','7','8','9','10']
# result = [int(i) for i in lst_str]
# print(result)

# lst_str = ['1','','3','','5','6','','8','','10']
# result = [i for i in lst_str if i !='']
# print(result)

# string = "a4d54i24t1y2a42"
# result = [i for i in string if i.isdigit()]
# print(result)


# string = "aditya vaishnav i am from sandip university"
# lst = string.split()
# print(lst)
# result = [len(i) for i in lst]
# print(result)

# lst = [43,54,57,75,23,44,45]
# result = [(1.8 * i)+32 for i in lst]
# print(result)

# lst1 =[1,2,2,3,4,5,6]
# lst2 =[2,3,4,5,6,7,10,11]
# result = []
# [result.append(i) for i in lst1 for j in lst2 if i == j and i not in result]
# print(result)

# lst = [1,2,3,1,3,3,4,2,5,5,6,5,3]
# result = [i for i in lst if i not in lst[:lst.index(i)]]
# print(result)

# lst = [1,2,3,1,3,3,4,2,8,8,8,5,5,6,5,3,7]
# result = [lst[i] for i in range(len(lst)) if lst[i] not in lst[:i]]
# print(result)


# lst = [1,3,4,1,10,12,24,35,1,42]
# # result = [i ** 2  for i in lst if i > 10]
# print(result)

# n = 5
# result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
# for i in result:
#     print(i)

# matrix = [[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16]]
# for i in matrix:
#     print(i)
# matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# for i in matrix:
#     print(i)
    

# lst_words = ["apple","Mango","pineapple"]
# lst_words = [i[::-1] for i in lst_words]
# print(lst_words)


# lst = [10,20,30,40,50,60,70,80]
# lst = [lst[i] * i for i in range(len(lst))]
# print(lst)


# lst = [(a,b,c) for a in range(1,21) for b in range(a,21) for c in range(b,21) if a**2 + b**2 == c**2]
# print(lst)

# lst = [[(i,j)for i in range(3)] for j in range(3)]
# print(lst)




# students = [
#     {"name": "Aditya", "age": 20},
#     {"name": "Rahul", "age": 22},
#     {"name": "Priya", "age": 21}
# ]
# lst = [i['name'] for i in students]
# print(lst)


# words = ["apple", "banana", "apple", "cherry", "apple"]
# r = "orange"
# words = ["orange " if i == "apple" else i for i in words]
# print(words)

# lst = [1,2,3,4,5,6,7,8,9,10]
# lst = ['even' if i % 2 == 0 else 'odd' for i in lst]
# print(lst)

# lst = [n for n in range(2,101) if all(n % i != 0 for i in range(2,int(n ** 0.5) + 1))]
# print(lst)

# lst = ["apple12","orange","mang2o","banana","lemon","ginger3"]
# lst = [word for word in lst if not any(char.isdigit() for char in word)]
# print(lst)


# lst = [1,2,3,4,5]
# lst = [(lst[i],lst[j]) for i in range(len(lst)) for j in range(i + 1,len(lst))]
# print(lst)


# import math
# lst = [math.factorial(i) for i in range(1,11)]
# print(lst)


# lst = ["aditya vaishnav from sandip university","Sunil vaishnav","Nita Vaishnav","Nita Vaishnav","sumit vaishnav"]
# lst = [len(i.split()) for i in lst]
# print(lst)



# lst = [['b' if (i + j)%2 == 0 else 'w' for i in range(8)] for j in range(8)]
# for i in lst:
#     print(i)



# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# lst = [i**2 if i % 2 == 0 else i**3 for i in lst ]
# print(lst)


# lst = ["abc@gmail.com", "xyz@yahoo.com"]
# lst = [email.split('@')[1] for email in lst]
# print(lst)

# lst = ["apple","madam","mom","nun","malayalam"]
# lst = [i for i in lst if i == i[::-1]]
# print(lst)

# string = "abc"
# lst = [string[i:j] for i in range(len(string)) for j in range(i+1,len(string) + 1)]
# print(lst)
