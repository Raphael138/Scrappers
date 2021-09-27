from bs4 import BeautifulSoup
import pandas as pd
import os
import requests
import threading

def thread_function(page, titles, authors, ratings, number_ratings ,scores, number_votes):

    # find url
    URL = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page="+str(page)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    # find list
    list_books = soup.find("table", class_="tableList js-dataTooltip")
    books = list_books.find_all("tr")

    #iterate over each movie
    for book in books:

        #find title
        inbetween = book.find_all("td")[2]
        title = inbetween.find("a", class_="bookTitle").text
        titles.append(title.strip())

        #find author
        author = inbetween.find("a", class_="authorName").text
        authors.append(author)

        #find ratings and number of ratings
        inbetween = book.find("span", class_="minirating").text.split()
        try:
            ratings.append(float(inbetween[0]))
        except:
            ratings.append(float(inbetween[3]))
        number_ratings.append(inbetween[-2])

        #find score and number of votes
        inbetween = book.find("span", class_="smallText uitext").find_all("a")
        scores.append(int(inbetween[0].text.split()[1].replace(",","")))
        number_votes.append(inbetween[1].text.split()[0])

def main():
    #initiate list of threads
    threads = []

    #initiate important variables
    titles = []
    authors = []
    ratings = []
    number_ratings = []
    scores = []
    number_votes = []
    
    # For loops that loops through the pages of the IMDB webpages
    for it1 in [1, 51]:
        for page in range(it1, it1+50):
            t = threading.Thread(target=thread_function, args=(page, titles, authors, ratings, number_ratings ,scores, number_votes,))
            t.daemon = True
            threads.append(t)

    for i,t in enumerate(threads):
        print(i+1)
        if not t.is_alive():
            t.start()

    for i in range(len(threads)):
            threads[i].join()

    # Creating the dataframe for all the movies and adding them to the file
    df = pd.DataFrame({
        "Title":titles,
        "Author":authors,
        "Rating": ratings,
        "Number of Rating": number_ratings,
        "Score": scores,
        "Number of Votes": number_votes,
    })  
    os.remove("books.csv")
    df.to_csv("books.csv")  

    return 0

if __name__=="__main__":
    main()
