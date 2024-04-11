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
links = list(NYT_bestsellers.get("amazon links"))
titles_and_links_dict = dict(zip(titles, links))

def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles)
unique_links = unique_list(links)

titles = []
categories_bybook = []
pages = []
publishers_bybook = []

# List of Authors and Quotes

# List of URLs
urls = unique_links
print(len(urls))

# # List for Randomizing our request rate
rate = [i/10 for i in range(10)]

# Iterating through the URLS
for url in urls[290:]:
    #print(url)

    categories = []
    pages_bad = []
    publishers = []

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0",
    }

    # Accessing the Webpage
    page = requests.get(url, headers= headers)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")
    #print(soup)
    if soup:
        search = soup.find(class_="a-unordered-list a-nostyle a-vertical zg_hrsr")
        search2 = soup.find(class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
        if search:
            if search2:

    # Adding the authors and quotes to their lists
                titles.extend([i.text for i in soup.find(class_='a-size-extra-large')])
                #print(titles)

                categories.extend([i.text for i in search.find_all(class_='a-list-item')])
                print(categories)

                pages_bad.extend([i.text for i in soup.find_all(class_='a-section a-spacing-none a-text-center rpi-attribute-value')])
                #print(pages_bad)

                publishers.extend([i.text for i in search2.find_all(class_='a-list-item')])
                #print(publishers)

                clean_categories = []
                for category in categories:
                    newcat = category[category.find('in'):]
                    clean_categories.append(newcat)

                for num in pages_bad:
                    if num[-6:-1] == "pages":
                        pages.append(num)
                        break
                    else:
                        continue

                for pub in publishers:
                    if pub[0:10] == " Publisher":
                        just_pub = pub
                    else:
                        continue
                pub = just_pub.split("                                 ")
                publishers_bybook.append(pub[-1])
                #print(publishers_bybook)

                categories_bybook.append(clean_categories)

                time.sleep(random.choice(rate))

            else:
                print("NA")
        else:
            print("NA")
    else:
        print("NA")


    if len(titles) >= 30:
        break






print(len(titles))
print(len(categories_bybook))
print(len(pages))
#print(titles)
#print(pages)
print(len(publishers_bybook))
Amazon_Attributes2 = pd.DataFrame({"title": titles, "categories": categories_bybook, "pages": pages, "publisher": publishers_bybook})
#print(Amazon_Attributes)
Amazon_Attributes2.to_csv(r'Ama-TagsRawMore-weekly1523_11.csv')

