import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np

URL = "https://www.worldatlas.com/citypops.htm"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

list_of_cities = soup.find(id = "container")

cities = list_of_cities.find_all("tr")

#set up array where we store city
city1 = []

for city in cities:
    # set up temporary array
    properties = []

    city_properties = city.find_all("td")

    for properti in city_properties:

        properties.append(properti.text)

    city1.append(properties)

del city1[0]

#create arrays
name = []
rank = []
country = []
population = []

#store in there
for city2 in city1:
    name1 = city2[1]
    name.append(name1)
    rank1 = city2[0]
    rank.append(rank1)
    country1 = city2[2]
    country.append(country1)
    population1 = city2[3]
    population.append(population1)

results = open("ScrapingResults.txt", "w")

table = pd.DataFrame({
    "Rank": rank,
    "City: ": name,
    "Country": country,
    "Population": population
})

results.write(tabulate(table, headers="keys"))
