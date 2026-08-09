# D = {
#     'name' : "Aditya",
#     'Maths' : 84,
#     'age' : 21,

# }
# print(D['name'])

# D['gender'] = 'male'
# print(D)
# D['gender'] = 'none' 
# print(D)
# del D['name']
# print(D)

# print(len(D))

# print(D.keys())
# for key in D.keys():
#     print(key)
# for key in D:
#     print(key)

# print(D.values())
# for values in D.values():
#     print(values)
# for key in D:
#     print(D[key])

# print(D.keys(),D.values())
# for key in D:
#     print(key,D[key])

# for key , value in D.items():
#     print(key,":",value)


# target_key  = 'name'
# is_found = False
# for key in D.keys():
#     if target_key == key:
#         is_found = True
#         break
  
# if is_found:
#     print("Found")
# else:
#     print("Not Found")



# if "name" in D:
#     print("Found")
# else:
#     print("Not Found")

# print("found" if 'name' in D else "not Found")

# D1 = D.copy()
# print(D1)
# D1['gender'] = 'none'
# print(D1)
# print(D)

# D1.clear()
# print(D1)

# D1.popitem()
# print(D1)

# result = list(D1.items())
# print(result)

# result =[]
# for key,values in D1.items():
#     result.append((key,D1[key]))
# print(result)

# result = list(D1.items())
# print(result)

# lst_sample = [('a',1),('b',2),('c',3),('d',4),('e',5)]
# result = dict(lst_sample)
# print(result)

# key = [1,2,3,4,5]
# value = ['a','b','c','d','e']
# result = dict(zip(key,value))
# print(result)


# D1 = {}
# for key , value in lst_sample:
#     D1[key] = value
# print(D1)

# arr = [1, 2, 2, 3, 3, 3, 4]
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] +=1
#     else:
#         freq[num] = 1
# print(freq)

# freq = {}
# for num in arr:
#     freq[num] = freq.get(num,0) + 1
# print(freq)



# s = "Adityavaishnav"
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] +=1
#     else:
#         freq[ch] = 1

# print(freq)


# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch,0) + 1
# print(freq)




# sentence = "apple banana apple mango banana apple"
# words = sentence.split()
# freq = {}
# for w in words:
#     if w in freq:
#         freq[w] +=1
#     else:
#         freq[w] = 1

# print(freq)

# freq = {}
# for w in words:
#     freq[w] = freq.get(w,0) + 1
# print(freq)





# d = {
#     'c' : 10,
#     'd' :20,
#     'a' :30,
#     'e' : 40,
#     'b' :50
# }
# max_val = float('-inf')
# max_key = None
# for key , value in d.items():
#     if value > max_val:
#         max_val = value
#         max_key = key
# print(max_key)


# maxi = max(d, key = d.get)
# print(maxi)


# min_val = float('inf')
# min_key = None
# for key,value in d.items():
#     if value < min_val:
#         min_val = value
#         min_key = key
# print(min_key,min_val)

# mini = min(d,key=d.get)
# print(mini)

# sum = 0
# for value in d.values():
#     sum = sum + value
# print(sum)





# d = {
#     'c' : 10,
#     'd' :20,
#     'a' :30,
#     'e' : 40,
#     'b' :50
# }
# result = dict(sorted(d.items()))
# print(result)

# print(dict(sorted(d.items(), key=lambda x: x[1])))


# d = {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 40,
#     'b' :10
# }
# values = list(d.values())
# lst = []
# for val in values:
#     if values.count(val) > 1 and val not in lst:
#         lst.append(val)
# print(lst)





# d = {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 30,
#     'b' :50
# }

# swapped = {}
# for key , values in d.items():
#     swapped[values] = key
# print(swapped)

# swapped = {values : key for key ,values in d.items()}
# print(swapped)


# d1= {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 30,
#     'b' :50,

# }
# d2 = {
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }

# d1['others'] = d2
# print(d1)

# print(d1 | d2)

# d1.update(d2)
# print(d1)



# print({**d1,**d2})

# d= {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 30,
#     'b' :50,
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }

# for key , value in d.items():
#     if value % 2 == 0:
#         print(key,value)

# d = {
#     'name': 'aditya',
#     'city': 'mumbai',
#     'course': 'python'
# }
# for key , value in d.items():
#     d[key] = value.upper()
# print(d)




# d = {
#     'name': 'aditya',
#     'city': 'mumbai',
#     'course': 'python',
#     'gender' : 'male',
#     'course' : 'cse'
# }
# selected_keys = ['name','course','gender']
# result ={}
# for key , values in d.items():
#     if key in selected_keys:
#         result[key] = values
# print(result)


# d = {
#     'student1': {
#         'name': 'Aditya',
#         'age': 21,
#         'city': 'Mumbai'
#     },
#     'student2': {
#         'name': 'Rahul',
#         'age': 22,
#         'city': 'Delhi'
#     }
# }
# print(d['student1']['age'])
# print(d['student2']['city'])



# d= {
#     'a' :40,
#     'c' : 10,
#     'd' :20,
#     'e' : 30
    
# }
# count = 0
# total = 0
# for value in d.values():
#     total += value
#     count += 1
# ans = total // count
# print(ans)

# ans = sum(d.values()) // len(d)
# print(ans)




# d= {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 30,
#     'b' :50,
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }
# ans_dict = dict(sorted(d.items(),key = lambda x : x[1],reverse=True) [:3])
# print(ans_dict)

# dict_ans =  dict(reversed(list(d.items())))
# print(dict_ans)


# d= {
#     'c' : 10,
#     'd' :20,
#     'a' :40,
#     'e' : 30,
#     'b' :50,
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }
# dic_val_lst = list(d.values())
# print(dic_val_lst)


# d= {
#     'c' : 10,
#     'd' :22,
#     'a' :40,
#     'e' : 30,
#     'b' :50,
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }
# result ={}
# for key , values in d.items():
#     result.setdefault(values,[]).append(key)
# print(result)



# list_of_dict = [
#     {'a' : 10,'b' : 20},
#     {'c' : 30 , 'd' : 40},
#     {'e':50}
# ]
# result = {}
# for dic in list_of_dict:
#     result.update(dic)
# print(result)


# d= {
#     'c' : 10,
#     'd' :22,
#     'a' :40,
#     'e' : 30,
#     'b' :50,
#     'f' : 54,
#     'g' :22,
#     'h' : 30,
#     'i' : 89,
#     'j' :53,
#     'k' :53
# }
# count = 0
# unique_value_list = []
# for values in d.values():
#     if values not in unique_value_list:
#        unique_value_list.append(values)
# print(len(unique_value_list))
# print(unique_value_list)


# result_lst = set(d.values())
# print(len(result_lst))

# from collections import Counter
# counts = Counter(d.values())
# unique_count = len(counts)
# print(unique_count)




# d= {
#     'c' : 1,
#     'd' :2,
#     'a' :4,
#     'e' :3,
#     'b' :5,
#     'f' :7,
#     'g' :8,
#     'h' :9,
#     'i' :11,
#     'j' :12,
#     'k' :9
# }
# mul = 1
# for key , values in d.items():
#     mul *= values
# print(mul)




# d = {
#     'a': 10,
#     'b': None,
#     'c': 20,
#     'd': None,
#     'e': 30,
#     'f' : 53
# }
# result = {}
# for key , values in d.items():
#     if values != None :
#             result[key] = values
# print(result)








# nested_dict = {
#     'a': 1,
#     'b': {
#         'b1': 21,
#         'b2': 22
#     },
#     'c': {
#         'c1': 31,
#         'c2': 32
#     }
# }

# flat_dict = {}

# for key, value in nested_dict.items():
#     if isinstance(value, dict):
#         for sub_key, sub_value in value.items():
#             flat_dict[key + '.' + sub_key] = sub_value
#     else:
#         flat_dict[key] = value

# print(flat_dict)

# words = ['apple', 'bat', 'ball', 'cat', 'apple', 'dog']
# grouped = {}
# for word in words:
#     length = len(word)
#     grouped.setdefault(length,[]).append(word)
# print(grouped)

# s = "adidtyavaistyshnhnav"
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch] =1
# print(freq)
# characher = ""
# for key,values in freq.items():
#     if values == 1:
#         print( key)
#         break




# d = {
#     'a': 10,
#     'b': 20,
#     'c': 40,
#     'd': 30,
#     'e': 40
# }
# sorted_dic =  sorted(set(d.values()),reverse=True)
# print(sorted_dic[1])
# print(sorted_dic)


# result ={num : num ** 2 for num in range(1,11)}
# print(result)

# result = {}
# for num in range(1,11):
#     result[num] = num ** 2
# print(result)

# d = {
#     'a': 10,
#     'b': 20,
#     'c': 10,
#     'd': 30,
#     'e': 20,
#     'f': 10
# }
# freq = {}
# for values in d.values():
#     freq[values] = freq.get(values,0) + 1
# print(freq)
# grouped ={}
# for key , values in d.items():
#     grouped.setdefault(values,[]).append(key)
# print(grouped)


# students = {
#     'Alice': 85,
#     'Bob': 72,
#     'Charlie': 90,
#     'David': 65,
#     'Eva': 55
# }
# result = {}
# for key , val in students.items():
#     if val >= 90:
#         result[key] = 'A'
#     elif val >= 80:
#         result[key] = 'B'
#     elif val >= 70:
#         result[key] = 'C'
#     elif val >= 60:
#         result[key] = 'D'
#     else :
#         result[key] = 'F'
# print(result)



# d = {
#     'level': 10,
#     'radar': 20,
#     'python': 30,
#     'civic': 40,
#     'data': 50
# }
# result = []
# for key in d.keys():
#     if key == key[::-1]:
#         result.append(key)
# print(result)



# nested_dict = {
#     'a': 1,
#     'b': {
#         'b1': 21,
#         'b2': 22
#     },
#     'c': {
#         'c1': 31,
#         'c2': {
#             'c21': 321
#         }
#     }
# }

# target = 'c21'
# found = False

# Outer loop
# for k1, v1 in nested_dict.items():
#     if k1 == target:
#         found = True
#         break
#     # Check if value is a dictionary
#     if isinstance(v1, dict):
#         for k2, v2 in v1.items():
#             if k2 == target:
#                 found = True
#                 break
#             if isinstance(v2, dict):
#                 for k3, v3 in v2.items():
#                     if k3 == target:
#                         found = True
#                         break
#         if found:
#             break

# print(found)



# synonyms = {
#     'happy': 'joyful',
#     'sad': 'unhappy',
#     'fast': 'quick',
#     'slow': 'lethargic',
#     'smart': 'intelligent'
# }


# word_to_search = 'fast'

# if word_to_search in synonyms:
#     print(f"Synonym of '{word_to_search}' is '{synonyms[word_to_search]}'")
# else:
#     print(f"No synonym found for '{word_to_search}'")

# word_to_search = 'strong'

# if word_to_search in synonyms:
#     print(f"Synonym of '{word_to_search}' is '{synonyms[word_to_search]}'")
# else:
#     print(f"No synonym found for '{word_to_search}'")

