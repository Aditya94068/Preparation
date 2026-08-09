import numpy as np
#Creating 1d array with zero values
# array_1d = np.zeros(5)
# print(array_1d)

# Creating 2d array with zero valuesf
# array_2d = np.zeros((5,6))
# print(array_2d)


# array_2d  = np.zeros((2,4),dtype = int)
# print(array_2d)

array_column_major= np.zeros((3,4))
print(array_column_major.flatten(order = 'F'))