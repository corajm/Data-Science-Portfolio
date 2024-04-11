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

goodreads_links = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/goodreads_links_weekly1523_CSV.csv")
#print(NYT_bestsellers)

urls = ["https://www.goodreads.com/en/book/show/34219841"]

#### PT 4 SCRAPING

# List of Authors and Quotes

titles_and_tags = {}

# List of URLs

# # List for Randomizing our request rate
# rate = [i/10 for i in range(10)]

# Iterating through the URLS
for url in urls:

    titles = []

    tags = []

    # Accessing the Webpage
    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")

    # Adding the authors and quotes to their lists
    titles.extend([i.text for i in soup.find_all(class_='Text Text__title1')])
    print(titles)

    tags.extend([i.text for i in soup.find_all(class_='Button Button--tag-inline Button--small')])

    #for i in soup.find_all(class_='Button Button--tag-inline Button--small'):
        #if [i.text] == ['...more']:
            #break
        #else:
            #tags.extend([i.text])

    for key in titles:
        titles_and_tags[key] = tags

    # Checking to see if we hit our required number of quotes then breaking the loop
    #if len(titles_and_tags) >= 10:
        #break

     # Randomizing our request rate
    #time.sleep(random.randint(0,10))

#print(len(titles_and_tags))

titles_and_tags_table = pd.Series(titles_and_tags)
#print(titles_and_tags_table )

titles_and_tags_table.to_csv(r'NYT_MG_WEEKLY_1523_TAGSmissing_CSV_04.csv')