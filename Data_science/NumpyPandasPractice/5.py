import numpy as np
arr = np.array([[1,5,3,4],[6,'a',5,5],[8,3,5,6],[5,6,'c','s']],dtype=object)
def is_numeric_row(row):
    return all(isinstance(i,(int,float)) for i in row)
numeric_row = np.array([row for row in arr if is_numeric_row(row)])
print(numeric_row)
