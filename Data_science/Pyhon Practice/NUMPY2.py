import numpy as np
# import time
# a = [i for i in range(10000000)]
# b = [i for i in range(10000000,20000000)]
# c = []
# start = time.time()
# for i in range(len(a)):
#     c.append(a[i] + b[i])
# print(time.time()-start)

# start = time.time()
# a = np.arange(10000000)
# b = np.arange(10000000,20000000)
# c = a + b
# print(time.time()-start)

# import sys
# print(sys.getsizeof(a))
# a = np.arange(10000000 ,dtype = np.int64)
# print(sys.getsizeof(a))



# a = np.arange(12).reshape(4,3)
# print(a)
# b = np.arange(3).reshape(3)
# print(b)
# print("Broadcasting")
# print(a + b)

import math
actual = np.random.randint(0,2,25)
predicted = np.random.randint(25)
def BCA(actual,predicat):
    epsilon = 1e-15
    predicat = np.clip(predicat,epsilon,1-epsilon)
    loss = -(actual * np.log(predicat) +(1 - actual) * np.log(1-predicat))
    return loss

print(BCA(actual,predicted))



import numpy as np

# actual should be 0 or 1
actual = np.random.randint(0, 2, 25)

# predicted should be between 0 and 1
predicted = np.random.rand(25)

def BCA(actual, predicat):
    epsilon = 1e-15  # to avoid log(0)
    predicat = np.clip(predicat, epsilon, 1 - epsilon)
    
    loss = -(actual * np.log(predicat) + (1 - actual) * np.log(1 - predicat))
    return loss

print(BCA(actual, predicted))

