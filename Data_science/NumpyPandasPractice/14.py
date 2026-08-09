import numpy as np
arr = np.array( [[[1,2,3],[4,5,6],[4,5,6]]])
print(arr)
print(arr.shape)
result = np.squeeze(arr)
print(result)
print(result.shape)
