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

tags_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./Ama-TagsRawMore-weekly1523.csv")
#print(tags_01_pd)

publishers_unclean = list(tags_pd.get("publisher"))

publishers = []
for item in publishers_unclean:
    stritem = str(item)
    newitem = stritem.split(";", 1)
    item2 = newitem[0]
    newnewitem = item2.split("(", 1)
    publishers.append(newnewitem[0])

print(publishers)

unique_pubs = list(set(publishers))
count = []
for pub in unique_pubs:
    how_many = publishers.count(pub)
    count.append(how_many)
print(count)

pubs_and_counts_dict = dict(zip(unique_pubs, count))
pubs_and_counts = pd.Series(pubs_and_counts_dict)
pubs_and_counts.to_csv(r'Ama-PubCount-weekly1523.csv')



