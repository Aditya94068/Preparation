# L = [1,2,3]
# print(max(L))
# def max():
#     print('hello')

# print(max(L))


#DECORATOR
# Problem 3:
# import time
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         print('time taken by ',func.__name__,time.time()-start,'sec')
#     return wrapper
# @timer
# def hello():
#     print("Hello world")
#     time.sleep(2)
# @timer
# def display():
#     print('displaying something')
#     time.sleep(4)
     
# hello()
# display()






# Problem 2:
# import time
# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         print('time taken by ',func.__name__,time.time()-start,'sec')
#     return wrapper
# @timer
# def hello():
#     print("Hello world")
#     time.sleep(2)
# @timer
# def square(num):
#     time.sleep(1)
#     print(num**2)
# hello()
# square(2)


# Problem 3:
#hum log ek aisa function bnaeynge ki wo check karega ki ye input valid hai ya nhi
# we are making sanity check program
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(*args) == data_type:
                func(*args)
            else:
                raise TypeError('Ye dataype nai chalega')
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)
@sanity_check(str)
def greet(name):
    print('hello',name)

greet('Aditya')
square(4)
square(4)





