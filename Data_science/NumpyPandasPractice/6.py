import numpy as np
arry1 = np.arange(2)
# print("One Dimensional array :")
print(arry1)

arry2 = np.arange(12).reshape(6,2)
# print("Tow Dimensional array :")
print(arry2)

for i,j in np.nditer([arry1,arry2]):
    print("%d:%d" % (i,j))


# result = np.vstack([arry1,arry2])
# print(result)


# result = np.hstack([arry1,arry2])
# print(result)