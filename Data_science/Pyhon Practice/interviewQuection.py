# mutable datatypes python dictionaries main keys ho hi nhi sakte hai
# This is used in python because in python set is immutable
d = {(1,2,3) : 'Aditya'}
print(d)

#This is not used in python because list are mutable 
# d = {[1,2,3] : "Sumit"}
# print(d)


# enumerate function
#The enumerate() method adds a counter to an iterable and returns it (the enumberate object).
# L = [('nitish',45),('ankit',31),('ankita',40)]
# print(sorted(L,key=lambda x:x[0],reverse=True))
# isme hum decide kar sakte hai ki kha se start hoga
# L = [15,21,13,13]
# print(list(enumerate(L)))
# print(list(enumerate(L)),reverse = True)


# destructor
# Object ke banne main constructor call hota hai aur object ke delete hone pe destructor call hota hai
# Jab tak saare ki saare references(Object) delete nhi ho jaate tab tak destructor call nhi hota hai
# isme hum wo configuration code likhte hai jisme hum database close karne ka code likhe te hai
# class Example:
#     def __init__(self):
#         print("Constructor call")
#     #destructor
#     def __del__(self):
#         print("destructor called")
# obj = Example()


# dir --> aapke saare ki saare attributes hai class ke andar jitne bhii magic methods hai ya private methods hai sabko display kar deta hai in one go 
# class Test:
#     def __init__(self):
#         self.foo = 11
#         self._bar = 24
#         self.__baz = 23
#     def greet(self):
#         print('hello')
# t = Test()
# print(dir(t))



# isinstance methods
# class Example:
#     def __init__(self):
#         print('hello')
# obj = Example()
# print(isinstance(obj,Example))


#issubclass
# class A:
#     def __init__(self):
#         pass
# class B(A):
#     pass
# print(issubclass(B,A))




# The Diamond Problem



