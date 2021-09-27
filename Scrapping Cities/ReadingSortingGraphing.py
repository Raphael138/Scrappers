import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#opening file
file = open("ScrapingResults.txt")

#creating storage array
log_population = []
log_rank = []
total = []
top5 = []
i = 0

#reading file and getting info into arrays
for line in file:
    if i >1:
        line = line.split()
        population = line.pop(-1)
        population = population.split(",")
        population = int("".join(population))
        if i<9:
            top5.append(int(population))
        total.append(int(population))
        log_population.append(math.log10(int(population)))
        log_rank.append(math.log10(int(line[1])))


    i+=1

#closing file
file.close()

#print ratio of top 5
ratio = sum(top5)/ sum(total)
print("Ratio of top 5%: "+str(round(ratio*100, 2))+"%.")
#graphing
plt.figure()
plt.scatter(log_rank, log_population)
m, b = np.polyfit(log_population, log_rank, 1)
x = np.linspace(min(log_population), max(log_population), 10)
y = m*x+b
label = "slope: "+ str(round(m, 3))
plt.plot(y, x, label = label)
plt.xlabel("Log of Population")
plt.ylabel("Log of Rank")
plt.legend()
plt.show()

print("asda")
