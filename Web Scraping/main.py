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

Links_csv = pd.read_csv(r"/Users/coramcanulty/Desktop/Stor 320/URL.list.csv")
urls = list(Links_csv.get("URL.list"))

# List of Authors and Quotes
kickstart = []
obid =[]

# # List for Randomizing our request rate
# rate = [i/10 for i in range(10)]

# Iterating through the URLS
co = 1
for url in urls:
    print(co)
    print(url)
    objectid = url[36:41]

    # Accessing the Webpage

    page = requests.get("https://boardgamegeek.com/boardgame/174430/gloomhaven/credits")

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
    iteratethro =  data["item"]["wiki"]
    print(iteratethro)
    TruOFa = "kickstarter" in iteratethro


    mechlist = []
    for i in iteratethro:
        mechin = i["name"]
        print(mechin)
        mechlist.append(mechin)

    kickstart.append(mechlist)
    obid.append(objectid)

    co = co+1

    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(mechs) >= 20:
        break

#     # Randomizing our request rate
#     time.sleep(random.choice(rate))

print(len(mechs))
print(len(obid))


mech_export = pd.DataFrame({"mechanics2": mechs, "objectid":obid})
mech_export.to_csv(r'MoreMechs.csv')