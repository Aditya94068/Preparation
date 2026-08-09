import numpy as np

#method one(==)
# an_array = np.array([[1,2],[3,4],[2,5]])
# another_array=np.array([[1,2],[3,4],[4,5]])
# compare = an_array == another_array
# result = compare.all()
# print(result)

#method two(np.array_equal)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2],[3,4]])
if np.array_equal(arr1,arr2):
    print(True)
else:
    print(False)

