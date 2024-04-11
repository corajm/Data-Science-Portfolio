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

import pandas as pd
import time
import random
import numpy as np
import pickle

#ama_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./AMA RAW 2/Ama-TagsMore-weekly1523.csv", encoding='latin-1')
NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_WEEKLY1523.csv")
missing = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./SG_missing.csv",)

titles = list(missing.get("title"))

titles_all = list(NYT_bestsellers.get("title"))
authors_all = list(NYT_bestsellers.get("author"))


def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles_all)
unique_authors = unique_list(authors_all)
lower_titles = []
for title in unique_titles:
    l_title = title.lower()
    lower_titles.append(l_title)

print(len(lower_titles))
titles_and_authors_dict = dict(zip(lower_titles, unique_authors))
print(len(titles_and_authors_dict))

print(titles_and_authors_dict["the sun and the star"])

missing_authors = []
for title in titles:
    if titles_and_authors_dict[title]:
        author = titles_and_authors_dict[title]
        missing_authors.append(author)
    else:
        continue


print(missing_authors)
print(len(missing_authors))
