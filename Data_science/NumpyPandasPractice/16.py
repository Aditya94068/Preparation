import numpy as np

x = np.array([1,2,3,4,5,1,2,3,1,1,2,3,1,1])
# print(np.bincount(x).argmax())

y = np.bincount(x)
maximum = max(y)
for i in range(len(y)):
    if(y[i] == maximum):
        print(i,end =" ")