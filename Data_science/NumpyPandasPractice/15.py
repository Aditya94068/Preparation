import numpy as np
arr=np.array ([[2,8,9,4],
       [9,4,9,4],
       [4,5,9,7],
       [2,9,4,3]])
result = repr(arr).count("9, 4")
print(result)