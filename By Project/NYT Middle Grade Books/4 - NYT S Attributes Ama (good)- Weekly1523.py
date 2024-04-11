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

NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./1 - NYT Scrape w/NYT_AMALINKS_WEEKLY1523.csv")
#print(NYT_bestsellers)


#### PT 2 FORMAT TITLES AND AUTHORS

titles = list(NYT_bestsellers.get("title"))
links = list(NYT_bestsellers.get("amazon links"))
titles_and_links_dict = dict(zip(titles, links))

def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles)
unique_links = unique_list(links)

titles = []
categories_bybook = []
# List of Authors and Quotes

# List of URLs
urls = unique_links
print(len(urls))

# # List for Randomizing our request rate
rate = [i/10 for i in range(10)]

# Iterating through the URLS
for url in urls:
    print(url)

    categories = []

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    }

    # Accessing the Webpage
    page = requests.get(url, headers= headers)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")
    #print(soup)
    if soup:

        search = soup.find(class_="a-unordered-list a-nostyle a-vertical zg_hrsr")
        if search:

    # Adding the authors and quotes to their lists
            titles.extend([i.text for i in soup.find(class_='a-size-extra-large')])
            #print(titles)

            categories.extend([i.text for i in search.find_all(class_='a-list-item')])
            print(categories)

            clean_categories = []
            for category in categories:
                newcat = category[category.find('in'):]
                clean_categories.append(newcat)

            categories_bybook.append(clean_categories)

            time.sleep(random.choice(rate))

    #if len(titles) >= 30:
        #break






#print(len(titles))
#Amazon_Attributes = pd.DataFrame({"title": titles, "categories": categories_bybook})
#print(Amazon_Attributes)
#Amazon_Attributes.to_csv(r'Ama-TagsRaw-weekly1523-missing.csv')

