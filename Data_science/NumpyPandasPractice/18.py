import numpy as np
'''
Syntax to add border in numpy array
np.pad(a,pad_width="Value",mode = 'constant',constant_values = 9)
'''
arr = np.ones([2,2])
print(arr)

result = np.pad(arr,pad_width=2,mode = 'constant',constant_values = 0)
print(result)


arr = np.array([[1,2,3],[5,6,7]])
print(arr)
result = np.pad(arr,pad_width = 1,mode = 'constant',constant_values = 4)
print(result)