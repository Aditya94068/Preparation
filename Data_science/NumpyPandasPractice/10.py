import numpy as np
arr1 = np.array([[0,3,1,0],[5,6,8,0],[0,3,0,5],[0,0,4,2]])
result = np.count_nonzero(arr1,axis=1)
print(result)