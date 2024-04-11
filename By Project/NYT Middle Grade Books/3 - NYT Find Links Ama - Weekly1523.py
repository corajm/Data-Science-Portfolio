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

NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_WEEKLY1523.csv")
#print(NYT_bestsellers)

counts = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/counts-weekly1523.csv")
#print(counts_pd)

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

titles_and_authors_list = []
for item in unique_titles:
    if str(titles_and_authors.loc[item]) != "NaN":
        titles_and_authors_list.append(str(item) + " " + str(titles_and_authors.loc[item]))
    else:
        titles_and_authors_list.append(str(item))

search_item = []
for item in titles_and_authors_list:
    searchfor = item.replace(" ", "+")
    search_item.append(searchfor)

search_list = [f"https://www.amazon.com/s?k={i}" for i in search_item]

amazon_links = []
for x in search_list:

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    content = requests.get(x, headers= headers).text
    soup = bs(content, 'html.parser')
    #print(soup)

    search = soup.find(class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")
    if search == None:
        continue
    #print(search)
    first_link = search.find("a")
    #print(first_link)

    back_of_link = first_link['href']
    amazon_links.append("amazon.com"+back_of_link)
    #print(amazon_links)

    #time.sleep(random.choice(rate))

print(amazon_links)
print(len(unique_titles))
print(len(search_list))
print(len(amazon_links))

amazon_export = pd.DataFrame({"links": amazon_links})
amazon_export.to_csv(r'AmazonLinks_weekly1523.csv')
