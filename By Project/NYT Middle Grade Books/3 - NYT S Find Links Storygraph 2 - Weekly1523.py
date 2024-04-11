#### PT 1 IMPORTING EVERYTHING

import pip

if int(pip.__version__.split('.')[0]) > 9:
    from pip._internal import main
else:
    from pip import main
def install(package):
    main(['install', package])

install('BeautifulSoup4')
install('openpyxl')
install('numpy')
install("pandas")
install("requests")
install("matplotlib")

from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import random
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import requests

storygraph_books = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./SG_MoreMissing.csv", encoding='latin-1')
#print(NYT_bestsellers)

titles = list(storygraph_books.get("title"))
authors = list(storygraph_books.get("author"))

title_and_author = dict(zip(titles, authors))

links = []

for title in titles:
    author = title_and_author[title]
    title_right = title.replace(" ", "%20")
    #author_right = author.replace(" ", "%20")
    link = "https://app.thestorygraph.com/browse?search_term="+title_right
    links.append(link)

print(links)

real_links = []

#### PT 4 SCRAPING

for url in links:

    content = requests.get(url).text
    soup = bs(content, 'html.parser')
    #print(soup)

    search = soup.find(class_="book-cover")
    if search == None:
        continue

    print(search)

    first_link = search.find("a")
    print("HERE")
    print(first_link)
    real_link = "https://app.thestorygraph.com"+first_link["href"]

    real_links.append(real_link)

    # Checking to see if we hit our required number of quotes then breaking the loop
    #if len(titles_and_tags) >= 10:
        #break

     # Randomizing our request rate
    #time.sleep(random.randint(0,10))


#missing_links = pd.DataFrame({"links": real_links})
#print(titles_and_tags_table)
#titles_and_tags_table["titles"] = all_titles

#missing_links.to_csv(r'SGLink_missing2_weekly1523.csv')