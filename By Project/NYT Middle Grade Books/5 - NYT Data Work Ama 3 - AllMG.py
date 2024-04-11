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
bestsellers_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/WEEKLY MG/Amazon/Ama-TagsMore-weekly1523 for biglist.csv", encoding = "ISO-8859-1")

bestseller_titles = list(bestsellers_pd.get("title"))
bs_page = list(bestsellers_pd.get("pages"))
bs_publisher = list(bestsellers_pd.get("publisher"))
bs_categories_listoflists = list(bestsellers_pd.get("categories"))
categories_listoflists = list(tags_pd.get("categories"))
raw_titles = list(tags_pd.get("title"))
page = list(tags_pd.get("pages"))
publisher = list(tags_pd.get("publisher"))


def clean_categories(raw_cats):
    ''' cleans category list of lists into 3 seperate lists of cats for a book'''
    allcats =[]
    cats_unclean = []
    for catlist in raw_cats:
        cats_unclean_bybook = []
        newlist = catlist.split('"')
        for cat in newlist:
            if cat[0:2] == "['":
                morecatlist = cat.split("'")
                for item in morecatlist:
                    cats_unclean_bybook.append(item)
            else:
                cats_unclean_bybook.append(cat)
        cats_unclean.append(cats_unclean_bybook)
    #print(cats_unclean)

    for bybook in cats_unclean:
        allcats_bybook = []
        for item in bybook:
            if item != "[":
                if item != "]":
                    if item != ",":
                        if item != "":
                            item2 = item.strip(",")
                            item3 = item2.strip(" ")
                            item4 = item3.strip("'")
                            allcats_bybook.append(item4)
        allcats.append(allcats_bybook)
    #print(allcats)

    allcats_cleaner = []
    for list in allcats:
        bybook = []
        for item in list:
            if item != "":
                bybook.append(item)
        allcats_cleaner.append(bybook)
    #print(allcats_cleaner)

    cat1 = []
    cat2 = []
    cat3 = []
    for list in allcats_cleaner:
        try:
            cat1.append(list[0])
        except IndexError:
            cat1.append("")
        try:
            cat2.append(list[1])
        except IndexError:
            cat2.append("")
        try:
            cat3.append(list[2])
        except IndexError:
            cat3.append("")

    return cat1, cat2, cat3

cat_1 = clean_categories(categories_listoflists)[0]
cat_2 = clean_categories(categories_listoflists)[1]
cat_3 = clean_categories(categories_listoflists)[2]

bs_cat_1 = clean_categories(bs_categories_listoflists)[0]
bs_cat_2 = clean_categories(bs_categories_listoflists)[1]
bs_cat_3 = clean_categories(bs_categories_listoflists)[2]


titles = []
for itemt in raw_titles:
    new = itemt.strip()
    titles.append(new)

bs_titles = []
for itemtt in bestseller_titles:
    new2 = itemtt.strip()
    bs_titles.append(new2)

x = len(titles)
y = len(bs_titles)

is_bestseller_0 = [0]*x
is_bestseller_1 = [1]*y
full_titles = titles + bs_titles
full_pages = page + bs_page
full_publishers = publisher + bs_publisher
full_c1 = cat_1 + bs_cat_1
full_c2 = cat_2 + bs_cat_2
full_c3 = cat_3 + bs_cat_3
is_bestseller = is_bestseller_0 + is_bestseller_1

Ama_withcats = pd.DataFrame({"title": full_titles, "pages": full_pages, "publisher":full_publishers, "category 1": full_c1, "category 2": full_c2, "category 3": full_c3 , "is bestseller": is_bestseller})

Ama_withcats.to_csv(r'All_MG_Extended.csv')



