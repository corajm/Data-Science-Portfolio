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

ama_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./AMA RAW 2/Ama-TagsMore-weekly1523.csv", encoding='latin-1')
sg_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/SG-TagsRaw-weekly1523.csv")

titles_sg_unclean = list(sg_pd.get("titles"))
titles_ama_unclean = list(ama_pd.get("title"))

print(len(titles_ama_unclean))
print(len(titles_sg_unclean))

print(titles_ama_unclean)
titles_ama = []
for item in titles_ama_unclean:
    stritem = str(item)
    newitem = stritem.split("(", 1)
    item2 = newitem[0]
    lowercaseitem = item2.lower()
    stripitem = lowercaseitem.strip("  ")
    stripitem2 = stripitem.strip("ê")
    titles_ama.append(stripitem2)
print(titles_ama)

print(titles_sg_unclean)
titles_sg = []
for item in titles_sg_unclean:
    stritem = str(item)
    newitem = stritem.split("\n", 1)
    item2 = newitem[0]
    lowercaseitem = item2.lower()
    titles_sg.append(lowercaseitem)
print(titles_sg)

t_ama_set = set(titles_ama)
t_sg_set = set(titles_sg)

missing = t_ama_set.difference(t_sg_set)
missing_list = list(missing)

print(len(missing_list))
print(missing_list)

missing_list_pd = pd.DataFrame(missing_list)
missing_list_pd.to_csv(r'SG_missing.csv')





