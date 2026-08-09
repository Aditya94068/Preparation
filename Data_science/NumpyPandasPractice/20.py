import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)

result = arr.flatten()
print(result)
result = arr.ravel()
print(result)
result =arr.reshape([1,12])
print(result,arr.dtype)