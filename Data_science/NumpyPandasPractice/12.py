import numpy as np
arr = np.array([1,2,3,4,5,6])
print("Initial array : " , arr)
result = np.flip(arr)
print("Method one : ",result)

res1 = arr[::-1]
print("Method two :",res1)

res2= np.flipud(arr)
print("Method three : ",res2)
