import numpy as np
#trim zeros from the left and right sider
arr1 = np.array([0,0,0,0,2,0,0,3,0,4,5,6,7,0,3,3,5,6,0,0,0])
result = np.trim_zeros(arr1,'f')
print(result)
result = np.trim_zeros(arr1,'b')
print(result)

result = np.trim_zeros(arr1,'fb')
print(result)

result = np.trim_zeros(arr1,'bf')

print(result)




#trim zeros from the middle 
non_zeros = arr1[arr1!=0]
print(non_zeros)