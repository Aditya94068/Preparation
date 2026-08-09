L = [1,22,13,7,9,11,10]
s = 16
for i in range(0,len(L)):
    Subarrary = []
    for j in range(i,len(L)):
        Subarrary.append(L[j])
        if(sum(Subarrary) == s):
            print(Subarrary)

