import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(arr)

print([1,2,3,4,5] in arr.tolist())
print([24,54,65,75,6] in arr.tolist())
print([11,12,13,14,15] in arr.tolist())
print([100,200,300,400,500] in arr.tolist())

