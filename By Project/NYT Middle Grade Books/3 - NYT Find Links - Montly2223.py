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

NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_MG_WEEKLY_1523_CSV.csv")
#print(NYT_bestsellers)

#### PT 2 FORMAT TITLES AND AUTHORS

titles = list(NYT_bestsellers.get("title"))
authors = list(NYT_bestsellers.get("author"))
titles_and_authors_dict = dict(zip(titles, authors))

def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles)
unique_authors = unique_list(authors)
titles_and_authors = pd.Series(titles_and_authors_dict)

#print(titles)
#print(unique_authors)
#print(unique_titles)
#print(titles_and_authors)
#print(len(titles_and_authors))
#print(len(unique_titles))
#print(len(titles))
#print(titles_and_authors)
#print(titles_and_authors.loc["WISH"])

titles_and_authors_list = []
for item in unique_titles:
    titles_and_authors_list.append(str(item) + " " + str(titles_and_authors.loc[item]))

search_list = [f"{i} goodreads" for i in titles_and_authors_list]
#print(search_list)

#### PT 3 GOODREADS LINKS

goodreads_links = []
for x in search_list:
    search = x
    url = 'https://www.google.com/search'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': search}

    content = requests.get(url, headers=headers, params=parameters).text
    soup = bs(content, 'html.parser')

    search = soup.find(id="search")
    first_link = search.find('a')

    goodreads_links.append(first_link['href'])

#print(goodreads_links)
print(len(goodreads_links))

#goodreads_export = pd.DataFrame({"links": goodreads_links})
#print(goodreads_export)

#goodreads_export.to_csv(r'goodreads_links_weekly1523_CSV.csv')
