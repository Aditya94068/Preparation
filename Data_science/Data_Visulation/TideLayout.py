import matplotlib.pyplot as plt
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
Sachin = [0,90,546,657,879,9786,2000,5400,6500,600]

# plt.plot(years, kohli, label="Virat Kohli")
# plt.plot(years, sehwag, label="Virender Sehwag")


plt.plot(years,kohli,color = "red",linewidth = 3, linestyle = '--',label = "KOHLI")
plt.plot(years,sehwag,color = 'blue',linewidth=4,linestyle = '-.',label = "SEHWAG")
plt.plot(years,Sachin,color ='yellow',linewidth = 5,linestyle ='-.',label = "SACHIN")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.tight_layout()
plt.title("Performance Comparison")
plt.show()