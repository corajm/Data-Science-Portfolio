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

NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_AMALINKS_WEEKLY1523.csv")
#print(NYT_bestsellers)

#### PT 2 FORMAT TITLES AND AUTHORS

titles = list(NYT_bestsellers.get("title"))
authors = list(NYT_bestsellers.get("author"))

def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles)
unique_authors = unique_list(authors)

count_t = []
count_a = []

for title in unique_titles:
    how_many = titles.count(title)
    count_t.append(how_many)

for author in unique_authors:
    how_many = authors.count(author)
    count_a.append(how_many)

titles_and_counts_dict = dict(zip(unique_titles, count_t))
titles_and_counts = pd.Series(titles_and_counts_dict)
#print(titles_and_counts)

authors_and_counts_dict = dict(zip(unique_authors, count_a))
authors_and_counts = pd.Series(authors_and_counts_dict)

#titles_and_counts.to_csv(r'counts-titles-PBweekly0823.csv')
authors_and_counts.to_csv(r'counts-authors-weekly1523.csv')
