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
import json
import re



#### PT 2 SCRAPING

urls = [
    f"https://boardgamegeek.com/boardgamefamily/8374/crowdfunding-kickstarter/linkeditems/boardgamefamily?pageid={i}"
    for i in 1:626]

# List of Authors and Quotes
name = []
obid =[]

# # List for Randomizing our request rate
# rate = [i/10 for i in range(10)]

# Iterating through the URLS
co = 1
for url in urls:
    print(co)
    print(url)

    # Accessing the Webpage

    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content, "html.parser")
    #print(soup)
    test2 = soup.find_all("div")
    #print(test2)
    script = soup.find_all('script')[2].text
    #print(script)
    loc = script.find("GEEK.geekitemPreload")
    start = loc + len("GEEK.geekitemPreload = ")
    end = script.find("GEEK.geekitemSettings") -3
    info = script[start:end]

    data = json.loads(info)
    iteratethro =  data["item"]["links"]["boardgame"]
    #print(iteratethro)

    for i in iteratethro:
        namei = (i["name"])
        obidi = (i["objectid"])
        name.append(namei)
        obid.append(obidi)


    co = co+1

    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(name) >= 25:
        break

#     # Randomizing our request rate
#     time.sleep(random.choice(rate))

print(len(name))
print(len(obid))


kick_export = pd.DataFrame({"name": kickstart, "objectid":obid})
kick_export.to_csv(r'GamesWithKick.csv')