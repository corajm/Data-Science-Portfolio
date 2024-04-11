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
install("unidecode")

from unidecode import unidecode
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

Links_csv = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./All_MG_missing_82.csv")
urls = list(Links_csv.get("missing links"))

titles = []
categories_bybook = []
pages = []
publishers_bybook = []

rate = [i/10 for i in range(10)]

user_agent_list = ['Mozilla/5.0 (Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.63',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.68',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (X11; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
 "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
 "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.3",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0",
 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"]

# Iterating through the URLS
y = 0
missing = []
for url in urls:

    print(url)

    categories = []
    pages_bad = []
    publishers = []

    user_agent = random.choice(user_agent_list)

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': user_agent,
    }

    # Accessing the Webpage
    page = requests.get(url, headers= headers)

    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")

    if soup:
        search = soup.find(class_="a-unordered-list a-nostyle a-vertical zg_hrsr")
        search2 = soup.find(class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")
        if search:
            if search2:
                titles.extend([i.text for i in soup.find(class_='a-size-extra-large')])
                # print(titles)

                categories.extend([i.text for i in search.find_all(class_='a-list-item')])
                #print(categories)

                pages_bad.extend([i.text for i in
                                  soup.find_all(class_='a-section a-spacing-none a-text-center rpi-attribute-value')])
                # print(pages_bad)

                publishers.extend([i.text for i in search2.find_all(class_='a-list-item')])
                # print(publishers)

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

                if 1+y != len(pages):
                    pages.append("NA")

                for pub in publishers:
                    if pub[0:10] == " Publisher":
                        just_pub = pub
                    else:
                        continue

                pub = just_pub.split("                                 ")
                publishers_bybook.append(pub[-1])
                # print(publishers_bybook)

                categories_bybook.append(clean_categories)
                print(y)
                y=y+1

                time.sleep(random.choice(rate))

            else:
                print("NA")
                missing.append(url)
        else:
            print("NA")
            missing.append(url)
    else:
        print("NA")
        missing.append(url)


    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(titles) >= 25:
        break

print(len(titles))
print(len(missing))
print(len(categories_bybook))
print(len(pages))
print(len(publishers_bybook))
#print(titles)

#### PT 3 COMPILE

missing_export = pd.DataFrame({"missing links": missing})
amazon_export = pd.DataFrame({"title": titles, "categories": categories_bybook, "pages": pages, "publisher": publishers_bybook})
amazon_export.to_csv(r'All_MG_Ama_83.csv')
missing_export.to_csv(r'All_MG_missing_83.csv')