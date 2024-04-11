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

recent = date(2023, 5, 28)
dates = [recent]
old =recent
stop = date(2015, 8, 23)

for i in range(1,1000):
    new = old - timedelta(days=7)
    if new != stop:
        dates.append(new)
        old = new
    else:
        break

dates_strings = []
for date in dates:
    dates_strings.append((date).strftime("%Y/%m/%d"))

# List of Authors and Quotes
titles = []

author = []

publisher = []

date_fromweb = []

# List of URLs
urls = [
    f"https://www.nytimes.com/books/best-sellers/{i}/childrens-middle-grade-hardcover/"
    for i in dates_strings]


# # List for Randomizing our request rate
# rate = [i/10 for i in range(10)]

# Iterating through the URLS
for url in urls:

    # Accessing the Webpage
    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")

    # Adding the authors and quotes to their lists
    titles.extend([i.text for i in soup.find_all(class_='css-5pe77f')])

    author.extend([i.text for i in soup.find_all(class_='css-hjukut')])

    publisher.extend([i.text for i in soup.find_all(class_='css-heg334')])

    date_fromweb.extend([i.text for i in soup.find_all(class_='css-6068ga')])

    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(titles) >= 4500:
        break

#     # Randomizing our request rate
#     time.sleep(random.choice(rate))

#print(titles)
#print(date)
#print(len(titles))
#print(len(author))
#print(len(publisher))



def extend_dates(data_list):
    '''get a list of dates the same length as the other lists'''
    list_of_dates = []
    for item in data_list:
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
        list_of_dates.append(item)
    return list_of_dates

final_dates = extend_dates(date_fromweb)
#print(len(final_dates))

def ranks_list(data_list):
    '''get a list of dates the same length as the other lists'''
    ranks = []
    onetoten = list(range(1,11))
    for item in data_list:
        ranks = ranks + onetoten
    return ranks

rank = ranks_list(date_fromweb)
#print(rank)
#print(len(rank))


#### PT 3 COMPILE

nyt_monthly_mg_stats_table = pd.DataFrame({"rank": rank, "title": titles, "author": author, "publisher": publisher, "date": final_dates})
print(nyt_monthly_mg_stats_table)

#### PT 4 EXPORT

nyt_monthly_mg_stats_table.to_csv(r'NYT_MG_WEEKLY_1523_CSV.csv')

