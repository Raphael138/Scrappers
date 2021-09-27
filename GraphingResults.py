import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#initiate graph and common names for axis
fig = plt.figure()
for_common_name = fig.add_subplot(111)
for_common_name.set_xlabel("log of US gross")
for_common_name.set_ylabel("log of Rank")
for_common_name.spines["top"].set_color("None")
for_common_name.spines["bottom"].set_color("None")
for_common_name.spines["left"].set_color("None")
for_common_name.spines["right"].set_color("None")
for_common_name.tick_params(labelcolor = "w", bottom = False, left = False)


for j in range(0,8):
    name = "SortedForTheYear"+str(1980+j*5)+".txt"
    file = open(name)
    i = -1

    #intitiate two arrays: us_gross and rank
    log_us_gross = []
    log_rank = []
    total = []
    top5 = []

    for line in file:
        if i>0 and i<51:

            line = line.split()

            log_us_gross.append(math.log10(float(line[-1])))
            log_rank.append(math.log10(i))
            total.append(float(line[-1]))
            if i >0 and i<6:
                top5.append(float(line[-1]))
        i+=1

    ratio = sum(top5)/sum(total)
    print("Top 5 percentage :", round(ratio*100, 2),"%w")

    #graph results
    emplacement = j+1
    sub_plot = fig.add_subplot(3,3, emplacement)
    sub_plot.scatter(log_us_gross, log_rank)
    m, b = np.polyfit(log_us_gross, log_rank, 1)
    x = np.linspace(min(log_us_gross), max(log_us_gross),100)
    y = m*x+b
    sub_plot.plot(x, y, label = "slope:"+str(round(m, 2)))
    sub_plot.legend()


plt.show()