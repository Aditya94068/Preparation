import numpy as np
# arr1 = np.array([1,2])
# arr2 = np.array([3,4])
# result = np.array(np.meshgrid(arr1 , arr2)).T.reshape(-1,2)
# print(result)

# arr1 = np.array([1,2,5])
# arr2 = np.array([3,4,5])
# arr3 = np.array([6,7])
# result = np.array(np.meshgrid(arr1,arr2,arr3)).T.reshape(-1,3)
# print(result)
# print(result.shape)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,6,7])
# arr3 = np.array([6,8,4])
# arr4 = np.array([5,6])
# result  = np.array(np.meshgrid(arr1,arr2,arr3,arr4)).T.reshape(-1,4)
# print(result)
# print(result.shape)


arr1 = np.array([1,3])
arr2 = np.array([4,7])
arr3 = np.array([6,4])
arr4 = np.array([5,6])
result  = np.array(np   .meshgrid(arr1,arr2,arr3,arr4)).T.reshape(-1,4)
print(result)
print(result.shape)