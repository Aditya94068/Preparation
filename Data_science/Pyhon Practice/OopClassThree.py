# Class Relationship :- There Are two types of relationship
# 1.Aggregation
# 2.Inheritance
# ============================================================

# 1.Aggregation (HAS-A Relationship):One Class owns the other class
# Jab bhi hum iss tarah ka application bna rahe hai jahape one class is the owner of second class inke bich main jo relationship hai it is called Aggregation

# Example:
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def display(self):
#         print(self.address.city,self.address.pin,self.address.state)
# class Address:
#     def __init__(self,city,pin,state):
#         self.city = city
#         self.pin = pin
#         self.state = state

# add1 = Address("Khandwa",450001,'Madhya Pradesh')
# cust1 = Customer("aditya","male",add1)
# cust1.display()

# ============================================================
#Example :- Private attribute jo hai wo accisible nhi hota hai toh uske liye hum getter ka use karengay
# class Customer:
#     def __init__(self,name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def display(self):
#         print(self.address.get_city(),self.address.pin,self.address.state)
# class Address:
#     def __init__(self,city,pin,state):
#         self.__city = city
#         self.pin = pin 
#         self.state = state
#     def get_city(self):
#         return self.__city
# add1 = Address("Khandwa",450001,'Madhya Pradesh')
# cust1 = Customer("aditya","male",add1)
# cust1.display()
# ============================================================
#Method 2 : Call Private attribute using Class name
# class Customer:
#     def __init__(self, name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def display(self):
#         print(self.address._Address__city,self.address.pin,self.address.state)
# class Address:
#     def __init__(self,city,pin,state):
#         self.__city = city
#         self.pin = pin 
#         self.state = state
#     def get_city(self):
#         return self.__city
# add1 = Address("Khandwa",450001,'Madhya Pradesh')
# cust1 = Customer("aditya","male",add1)
# cust1.display()
# ============================================================

#Using Aggreation in a smart way
# class Customer:
#     def __init__(self, name,gender,address):
#         self.name = name
#         self.gender = gender
#         self.address = address
#     def display(self):
#         print(self.address._Address__city,self.address.pin,self.address.state)
#     def edit_profile(self,new_name,new_city,new_pin,new_state):
#         self.name = new_name
#         self.address.edit_address(new_city,new_pin,new_state)
# class Address:
#     def __init__(self,city,pin,state):
#         self.__city = city
#         self.pin = pin 
#         self.state = state
#     def get_city(self):
#         return self.__city
#     def edit_address(self,new_city,new_pin,new_state):
#         self.__city = new_city
#         self.pin = new_pin
#         self.state = new_state
# add1 = Address("Khandwa",450001,'Madhya Pradesh')
# cust1 = Customer("aditya","male",add1)
# cust1.display()
# add1 = Address("Nashik",422001,"Maharashatra")
# cust1.edit_profile("Aditya",'Nashik',422001,"Maharashtra")
# cust1.display()
# ============================================================


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# Inheritance in python
class User:
    def __init__(self):
        self.name = 'Aditya'
        self.gender = 'male'
    def login(self):
        print("login")
class Student(User):
    def enroll(self):
        print("enroll into the course")
u = User()
s = Student()
print(s.name)
s.login()
s.enroll()







