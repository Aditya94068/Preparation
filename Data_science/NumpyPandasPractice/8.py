import numpy as np
arr  = np.arange(3*5*6).reshape(3,5,6)
print(arr)
dig_arr = np.diagonal(arr,axis1 = 1,axis2= 2)
print("digonal elemengt :\n",dig_arr)