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
from datetime import date, timedelta

#### PT 2 SCRAPING

Links_csv = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./All Books 2015-2023 goodreads links.csv")
urls = list(Links_csv.get("links"))

# List of Authors and Quotes
titles = []

authors = []

goodreads_page_links = []

user_agent_list = [
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.1',
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.3"
]

# Iterating through the URLS
for url in urls:

    user_agent = random.choice(user_agent_list)

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': user_agent,
    }

    # Accessing the Webpage
    page = requests.get(url, headers= headers)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")

    search = soup.find_all(class_="bookTitle")
    #print(search)

    page_titles = []
    for i in search:
        title = i.find(role = "heading").text
        print(title)
        page_titles.append(title)
    #print(page_titles)
    #print(len(page_titles))
    titles.extend(page_titles)

    page_links = []
    for x in search:
        link = x["href"]
        real_link = "https://www.goodreads.com" + link
        print(real_link)
        page_links.append(real_link)
    #print(page_links)
    #print(len(page_links))
    goodreads_page_links.extend(page_links)


    search2 = soup.find_all(class_="authorName")
    #print(search2)

    page_authors = []
    for j in search2:
        if j.find(itemprop="name") == None:
            continue
        else:
            author = j.find(itemprop="name").text
            page_authors.append(author)
            print(author)
    #print(page_authors)
    #print(len(page_authors))
    authors.extend(page_authors)

    print(len(page_titles))
    print(len(page_authors))
    print(len(page_links))
    print(" ")


    # Checking to see if we hit our required number of quotes then breaking the loop
    #if len(titles) >= 4500:
        #break

print(len(titles))
print(len(authors))
print(len(goodreads_page_links))

#### PT 3 COMPILE

ALL_MG_1523 = pd.DataFrame({"titles": titles, "authors": authors, "goodreads links": goodreads_page_links})
#print(nyt_monthly_mg_stats_table)

#### PT 4 EXPORT

ALL_MG_1523.to_csv(r'ALL_MG_1523_02.csv')
