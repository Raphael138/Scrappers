from bs4 import BeautifulSoup
import pandas as pd
import os
import requests


def main():
    #initiate title, year, us_gross
    titles = []
    us_gross = []
    years = []
    actors = []
    ratings = []
    number_votes = []
    genres = []
        
    # For loops that loops through the pages of the IMDB webpages
    for page in range(1, 6636, 50):

        # find url
        URL = "https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&countries=us&sort=user_rating,desc&start="+str(page)+"&ref_=adv_nxt"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        # find list
        list_movies = soup.find(class_="lister-list")
        movies = list_movies.find_all("div", class_="lister-item mode-advanced")

        #iterate over each movie
        for movie in movies:

            #find title
            title = movie.h3.a.text
            titles.append(title)

            #find year and append everything if it has everything
            year = movie.find("span", class_="lister-item-year text-muted unbold").text.split("(")[-1].split(")")[0]
            years.append(int(year))

            #find intermediate for us gross
            inbetween = movie.find_all("span", attrs={"name": "nv"})
            number_votes.append(inbetween[0].text)
            us_gross.append(inbetween[1].text if len(inbetween)==2 else None)

            # Finding the genre for a movie
            genre = movie.find("span", class_="genre").text.strip()
            genres.append(genre)

            # Finding the rating for a movie
            rating = movie.find("strong").text
            ratings.append(float(rating))

            inbetween = movie.find_all("p")[2].find_all("a")[1:]
            actor = ""
            for a in inbetween:
                actor+=a.text+ ", "
            actors.append(actor[:-2])

    # Creating the dataframe for all the movies and adding them to the file
    df = pd.DataFrame({
        "Title":titles,
        "Year":years,
        "US Gross": us_gross,
        "Rating": ratings,
        "Number of Votes": number_votes,
        "Genre": genres,
        "Actors": actors
    })  
    os.remove("movies.csv")
    df.to_csv("movies.csv")  

    return 0

if __name__=="__main__":
    main()
