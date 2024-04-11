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

tags_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/ALL MG 1523/All_MG_Amapages.csv", encoding = "ISO-8859-1")
#print(tags_01_pd)

categories_listoflists = list(tags_pd.get("categories"))

allcats =[]
cats_unclean = []
for catlist in categories_listoflists:
    newlist = catlist.split('"')
    for cat in newlist:
        if cat[0:2] == "['":
            morecatlist = cat.split("'")
            for item in morecatlist:
                cats_unclean.append(item)
        else:
            cats_unclean.append(cat)
print(cats_unclean)

for item in cats_unclean:
    if item != "[":
        if item != "]":
            if item != ",":
                item2 = item.strip(",")
                item3 = item2.strip(" ")
                item4 = item3.strip("'")
                allcats.append(item4)
print(allcats)

unique_cats = list(set(allcats))
count = []
for cat in unique_cats:
    how_many = allcats.count(cat)
    count.append(how_many)
print(count)

cats_and_counts_dict = dict(zip(unique_cats, count))
cats_and_counts = pd.Series(cats_and_counts_dict)
cats_and_counts.to_csv(r'Ama-CatCount-AllMG.csv')



