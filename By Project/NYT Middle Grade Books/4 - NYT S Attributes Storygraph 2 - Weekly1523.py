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

storygraph_books = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./SGLink_missing_weekly1523.csv", encoding='latin-1')
#print(NYT_bestsellers)

links = list(storygraph_books.get("links"))


#### PT 4 SCRAPING

# List of Authors and Quotes

books = []
all_titles = []

# List of URLs

# # List for Randomizing our request rate
# rate = [i/10 for i in range(10)]

# Iterating through the URLS
for url in links:

    titles = []

    genretags = []

    moodtags = []

    pages = []

    descriptors = []

    # Accessing the Webpage
    page = requests.get(url)


    # Getting the webpage's content in pure html
    soup = bs(page.content, features="html.parser")

    # Adding the authors and quotes to their lists
    titles.extend([i.text for i in soup.find_all(class_='font-serif font-bold text-lg min-[520px]:text-2xl leading-6')])
    print(titles)

    pages.extend([i.text for i in soup.find_all(class_='text-xs min-[520px]:text-sm font-light text-darkestGrey dark:text-grey mt-1')])

    genretags.extend([i.text for i in soup.find_all(class_='inline-block text-xs sm:text-sm text-teal-700 dark:text-teal-200 mr-0.5 mt-1 border border-darkGrey dark:border-darkerGrey rounded-sm py-0.5 px-2')])

    moodtags.extend([i.text for i in soup.find_all(class_="inline-block text-xs sm:text-sm text-pink-500 dark:text-pink-200 mr-0.5 mt-1 border border-darkGrey dark:border-darkerGrey rounded-sm py-0.5 px-2")])

    descriptors.extend([i.text for i in soup.find_all(class_="review-response-summary")])

    #for i in soup.find_all(class_='Button Button--tag-inline Button--small'):
        #if [i.text] == ['...more']:
            #break
        #else:
            #tags.extend([i.text])

    clean_pages = []
    unique_genretags = list(set(genretags))
    unique_moodtags = list(set(moodtags))
    unique_descriptors = descriptors[0:5]
    for page in pages:
        clean_page = page[9:12]
        clean_pages.append(clean_page)

    for title in titles:
        all_titles.append(title)
        title = {"pages": clean_pages, "genre tags": unique_genretags, "mood tags": unique_moodtags, "other descriptors": unique_descriptors}

    books.append(title)


    # Checking to see if we hit our required number of quotes then breaking the loop
    #if len(titles_and_tags) >= 10:
        #break

     # Randomizing our request rate
    #time.sleep(random.randint(0,10))

print(books)

titles_and_tags_table = pd.DataFrame.from_dict(books)
print(titles_and_tags_table)
titles_and_tags_table["titles"] = all_titles

titles_and_tags_table.to_csv(r'SG-TagsRaw2-weekly1523.csv')