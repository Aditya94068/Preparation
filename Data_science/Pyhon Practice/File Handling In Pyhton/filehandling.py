# f = open('Sample.txt','w')
# f.write("Hello World")
# f.close()

# f = open('Sample1.txt','w')
# f.write("Hello World")
# f.write("\nHow are you")
# f.close

# f = open('Sample.txt','w')
# f.write('Aditya Vaishnav')
# f.close()

#append mode
# f = open('Sample1.txt','a')
# f.write('\nI am fine')
# f.close()

# writelines() function add more line in the txt file
# L = ['hello\n','hi\n','how are you\n','I am find']
# f = open('Sample.txt','w')
# f.writelines(L)


# L = ['hello\n','hi\n','how are you\n','I am find']
# f = open('D:\\Data_science\\Pyhon Practice\\File Handling In Pyhton\\Sample.txt','w')
# f.writelines(L)



# Reading from files

# Using read() function
# f = open('D:\Data_science\Pyhon Practice\File Handling In Pyhton\Sample.txt','r')
# s = f.read()
# print(s)
# f.close

#reading upto n chars
# f = open('Sample.txt','r')
# s = f.read(3)
# print(s,end = '')
# f.close()

#readline() -> to read line by line
# f = open('Sample.txt','r')
# print(f.readline(),end = '')
# print(f.readline(),end = '')
# print(f.readline(),end = '')
# f.close()

# Reading entire using readline() function 
# f = open('Sample.txt','r')
# while True:
#     data = f.readline()
#     if data == '':
#         break
#     else:
#         print(data , end ='')


#with keyword
# with open('Sample.txt','w') as f:
#     f.write('aditya vaishnav')

# with open('Sample.txt','r') as f:
#     print(f.read(10))
#     print(f.read(10))


# big_L = ['hello world' for  i in range(100)]
# with open('big.txt','w') as f:
#     f.writelines(big_L)
# with open('big.txt','r') as f:
#     chunks_size = 10
#     while len(f.read(chunks_size)) > 0:
#         print(f.read(chunks_size),end = '@@')
#         f.read(chunks_size)


# with open('list.py','r') as f:
#     data = f.read()
#     print(data)


# with open('D:\\Data_science\\Pyhon Practice\\File Handling In Pyhton\\Sample.txt','r') as f:
#     print(f.read(10))
#     print(f.tell())
#     f.seek(0)
#     print(f.read(10))
#     print(f.tell())
    


# with open("D:\\Data_science\\Pyhon Practice\\File Handling In Pyhton\\Sample.txt",'w') as f:
#     f.write("hello")
#     f.seek(0)
#     f.write('Xa')



# with open('screenshot.png','rb') as f:
#     with open('screenshot_file.png','wb') as wf:
#         wf.write(f.read())


# with open('Sample.txt','w') as f:
#     f.write('5')

# with open('Sample.txt','r') as f:
#     print(f.read())

# d = {
#     'name' : 'aditya',
#     'age' : 22,
#     'gender' : 'male'
# }
# with open('Sample.txt','w') as f:
#     f.write(str(d))


# with open('Sample.txt','r') as f:
#     print(f.read())



# Topic Json
# import json
# L = [1,2,3,4,5]
# with open('demo.json','w') as f:
#     json.dump(L,f)


# d = {
#     'name' : 'Aditya',
#     'age' : '21',
#     'gender' : 'male'
# }
# with open('demo.json','w') as f:
#     json.dump(d,f,indent = 3)


# with open('demo.json','r') as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))



# d = {
#     'student' : 'Aditya',
#     'marks' : [22,35,46,57,68]
# }
# with open('demo.json','w') as f:
#     json.dump(d,f)

# class Person:
#     def __init__(self,fname,lname,age,gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender
# person = Person('aditya','vaishnav',21,'male')

# As a string fromat
# Aditya Vaishnav age --> 21 gender -> amel
# def show_object(person):
#     if isinstance(person,Person):
#         return "{} {} age --> {} gender --> {}".format(person.fname,person.lname,person.age,person.gender)
# with open('demo.json','w') as f:
#     json.dump(person,f,default=show_object)

# As a dictionary format
# def show_data(person):
#     if isinstance(person,Person):
#         return {'name' : person.fname + ' ' + person.lname , 'age' : person.age,'gender':person.gender}
# with open('demo.json','w') as f:
#     json.dump(person,f,default= show_data,indent = 4)

# with open('demo.json','r') as f:
#     print(json.load(f))


# Topic Pickle
# import pickle
# class Person:
#     def __init__(self,name,age):
#         self.name  = name
#         self.age = age
#     def display_info(self):
#         print('Hi my name is ',self.name,'and i ame ', self.age,'years old')
# p  = Person('Aditya',23)

# with open('person.pkl','wb') as f:
#     pickle.dump(p,f)
# with open('person.pkl','rb') as f:
#     p = pickle.load(f)
# p.display_info()









