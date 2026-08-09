# import pandas as pd
# import numpy as np
# subs = pd.read_csv(r'D:\Data_science\Pyhon Practice\subs.csv').squeeze()
# print(subs)

# runs = pd.read_csv(r'D:\Data_science\Pyhon Practice\kohli_ipl.csv',index_col='match_no').squeeze()
# print(runs)

# movies = pd.read_csv(r'D:\Data_science\Pyhon Practice\bollywood.csv',index_col='movie').squeeze()
# print(movies) 
# print(movies.size)
# print(movies.dtype)
# print(movies.name)
# print(movies.is_unique)
# # print(movies.index)
# print(movies.values)

# print(subs.head())
# print(subs.tail())
# print(runs.head(10))
# print(runs.tail())


# print(movies.sample())
# print(movies.sample(5))
# print(movies.sample(10))


# print(movies.value_counts())

# print(runs.sort_values())
# print(runs.sort_values(ascending=False))
# print(runs.sort_values(ascending=False).head())
# print(runs.sort_values(ascending=False).head(1))
# print(runs.sort_values(ascending=False).head(1).values)
# print(runs.sort_values(ascending=False).head(1).values[0])



import pandas as pd
import numpy as np
# country = ['india','bangladesh','USA','russia','china','srilanka','france','UK','spain','germany','finland'];
# print(pd.Series(country))

# code = np.array([13,34,54,64,75,76,86,24,13,3,5])
# print(pd.Series(runs))

# # print(pd.Series(country,index=runs))
# record = pd.Series(country,index=code,name='country code')
# print(record)


# names = ["Aman", "Riya", "Rahul", "Sneha", "Karan"]
# ages = [20, 21, 19, 22, 20]
# marks = [78, 85, 67, 90, 72]
# cities = ["Nashik", "Pune", "Mumbai", "Delhi", "Bangalore"]

# print(pd.Series([names,ages , marks]))

# print(pd.Series(ages),'\n',pd.Series(marks),'\n',pd.Series(names))

# detail= pd.Series(names,index = ages,name='Student detail')
# print(detail)




# marks = {
#     'maths' : 67,
#     'english' : 57,
#     'Science' : 89,
#     'Hindi' : 100,
#     'score' :{
#         'aman' : 44,
#         'aditya' : 55,
#         'rohit' :89
#     }
# }
# print(pd.Series(marks))



# code = np.array([13,34,54,64,75,76,86,24,183,3,5])
# print(code.size)
# print(code.dtype)
# print(record.name)

# print(pd.Series(code).is_unique)
# print(pd.Series(names).is_unique)
# print(record.index)
# print(record.values)




subs = pd.read_csv(r'D:\Data_science\Pyhon Practice\subs.csv').squeeze()
# print(subs)
movies = pd.read_csv(r'D:\Data_science\Pyhon Practice\bollywood.csv',index_col='movie').squeeze()
# print(movies)

runs = pd.read_csv(r'D:\Data_science\Pyhon Practice\kohli_ipl.csv',index_col='match_no').squeeze()
# print(runs)

# print(runs.head(10))
# print(runs.tail(50))

# print(movies.sample(10))
# print(subs.sample(18).values)


# print(movies.value_counts().head(1))
# print(runs.sort_values(ascending=False,inplace=True))
# print(runs.sort_values(ascending=False).head(1).values[0])

# movies.sort_index(inplace=True)
# print(movies.sort_index(ascending=False,inplace=True))
# print(movies.sort_index(ascending=False))

# print(runs.count())
# print(movies.count())
# print(subs.count())
# print(runs.sum())

# print(subs.mean())
# print(runs.mean())
# print(movies.value_counts().mean())
# print(subs.median())
# print(runs.median())
# print(movies.value_counts().median())
# print(movies.mode())
# print(runs.mode())
# print(subs.mode())

# print(subs.var())
# print(runs.var())
# print(movies.value_counts().var())
# print(subs.std())

# print(runs.min())
# print(subs.min())
# print(runs.max())
# print(subs.max())

# print(runs.describe())

# print(movies.describe())
# print(subs.describe())

# print(movies[1:100:1])
# print(runs[1:10:1])

# print(runs[[1,4,5,7,9]])
# print(movies[[1,3,6,2,7]])

# print(movies['Company (film)'])


# marks = pd.Series(np.array([13,34,54,64,75,76,86,24,13,3,5]))
# print(marks)
# marks[2:6] = [100,200,300,400]
# print(marks)
# marks[[1,5,6,3,2]] = [10,20,30,40,50]
# print(marks)


# for i in movies:
#     print(i)
# for i in movies.index:
#     print(i)

# for i in movies.values:
#     print(i)

# print(runs[runs>50])
# print(runs[runs>50].size)
# print(subs[subs>200].size)

# num_count = movies.value_counts()
# print(num_count[num_count>20].size)


# import matplotlib.pyplot as plt
# subs.plot()
# plt.show()
# movies.value_counts().head(20).plot(kind='pie')
# plt.show()