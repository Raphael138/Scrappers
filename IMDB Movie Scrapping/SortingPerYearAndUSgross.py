import pandas as pd
from tabulate import tabulate

#open the results
file = open("ScrappingResults.txt")

#set up check
i = 1

# #set up lists
years = []
title = []
us_gross = []

#iterate through each line
for line in file:
    if i>2 and i!=6522:
        #the line as a list
        line = line.split()

        #the year
        year = line.pop(-2)
        years.append(int(year))

        #the us gross
        us_gross1 = line.pop(-1)
        us_gross1 = us_gross1.split("$")
        us_gross1 = us_gross1[1].split("M")
        us_gross1 = float(us_gross1[0])
        us_gross.append(us_gross1)

        #get the title
        del line[0]
        title.append(" ".join(line))
    i+=1

#closing file
file.close()

#setting up 2D array called movie
movies = [title,years,us_gross]

#setting up 2D array for each 5 years
movie_80s = []
movie_85s = []
movie_90s = []
movie_95s = []
movie_00s = []
movie_05s = []
movie_10s = []
movie_15s = []

#sorting per year
for j in range(0, len(title)):
    #between 1980 and 1984
    if movies[1][j]>1979 and movies[1][j]<1985:
        movie_80s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 1985 and 1989
    elif movies[1][j]>1984 and movies[1][j]<1990:
        movie_85s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 1990 and 1994
    elif movies[1][j]>1989 and movies[1][j]<1995:
        movie_90s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 1995 and 1999
    elif movies[1][j]>1994 and movies[1][j]<2000:
        movie_95s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 2000 and 2004
    elif movies[1][j]>1999 and movies[1][j]<2005:
        movie_00s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 2005 and 2009
    elif movies[1][j]>2004 and movies[1][j]<2010:
        movie_05s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 2010 and 2014
    elif movies[1][j]>2009 and movies[1][j]<2015:
        movie_10s.append([movies[0][j], movies[1][j], movies[2][j]])
    #between 2015 and 2019
    elif movies[1][j]>2014 and movies[1][j]<2020:
        movie_15s.append([movies[0][j], movies[1][j], movies[2][j]])

movie_80s.sort(key=lambda x: x[2], reverse= True)
movie_85s.sort(key=lambda x: x[2], reverse= True)
movie_90s.sort(key=lambda x: x[2], reverse= True)
movie_95s.sort(key=lambda x: x[2], reverse= True)
movie_00s.sort(key=lambda x: x[2], reverse= True)
movie_05s.sort(key=lambda x: x[2], reverse= True)
movie_10s.sort(key=lambda x: x[2], reverse= True)
movie_15s.sort(key=lambda x: x[2], reverse= True)

movies_per_period = [movie_80s[0:50], movie_85s[0:50], movie_90s[0:50], movie_95s[0:50], movie_00s[0:50], movie_05s[0:50], movie_10s[0:50], movie_15s[0:50]]

for h in range(0, 8):

    #creating file for each time period
    name = "SortedForTheYear"+str(1980+(h*5))+".txt"
    sorted_results = open(name,"w")

    #get titles because list is formated weirdly
    title_2 = []
    year_2 = []
    us_gross_2 = []
    for u in range(0,50):
        title_2.append(movies_per_period[h][u][0])
        year_2.append(movies_per_period[h][u][1])
        us_gross_2.append(movies_per_period[h][u][2])

    table = pd.DataFrame({
        "Title": title_2,
        "Year": year_2,
        "US gross": us_gross_2
    })

    sorted_results.write(tabulate(table, headers="keys"))
    sorted_results.close()
