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

NYT_bestsellers = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_MG_WEEKLY_1523_CSV.csv")
#print(NYT_bestsellers)

counts = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/counts_weekly1523_CSV.csv")
#print(counts_pd)

#### PT 2 FORMAT TITLES AND AUTHORS

titles = list(NYT_bestsellers.get("title"))
authors = list(NYT_bestsellers.get("author"))
titles_and_authors_dict = dict(zip(titles, authors))

def unique_list(list):
    '''get unique values from a list, still in order'''
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

unique_titles = unique_list(titles)
unique_authors = unique_list(authors)
titles_and_authors = pd.Series(titles_and_authors_dict)

def getIndexes(dfObj, value):
    listOfPos = []

    # isin() method will return a dataframe with
    # boolean values, True at the positions
    # where element exists
    result = dfObj.isin([value])

    # any() method will return
    # a boolean series
    seriesObj = result.any()

    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)

    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)

        #for row in rows:
            #listOfPos.append((row, col))

    # This list contains a list tuples with
    # the index of element in the dataframe
    return rows

multiweek_titles = []

for title in unique_titles:
    title_row = counts.iloc[getIndexes(counts,str(title))]
    title_row_value = (title_row.values[0])[1]
    if title_row_value >= 2:
        multiweek_titles.append(title)

#print(len(multiweek_titles))
#print(titles)
#print(unique_authors)
#print(unique_titles)
#print(titles_and_authors)
#print(len(titles_and_authors))
#print(len(unique_titles))
#print(len(titles))
#print(titles_and_authors)
#print(len(titles_and_authors))
#print(titles_and_authors.loc["WONDER"])

titles_and_authors_list = []
for item in multiweek_titles:
    if str(titles_and_authors.loc[item]) != "NaN":
        titles_and_authors_list.append(str(item) + " " + str(titles_and_authors.loc[item]))
    else:
        titles_and_authors_list.append(str(item))


#search_list = [f"{i} goodreads" for i in titles_and_authors_list]
#print(search_list)

rate = [i/10 for i in range(10)]

#### PT 3 GOODREADS LINKS

storygraph_links = []
for x in titles_and_authors_list:
    split_list = x.split(" ")
    #print((split_list))
    if len(split_list) >= 6:
        url = f'https://app.thestorygraph.com/browse?search_term={split_list[0]}%20{split_list[1]}%20{split_list[2]}%20{split_list[3]}%20{split_list[4]}%20{split_list[5]}'
    if len(split_list) == 5:
        url = f'https://app.thestorygraph.com/browse?search_term={split_list[0]}%20{split_list[1]}%20{split_list[2]}%20{split_list[3]}%20{split_list[4]}'
    if len(split_list) == 4:
        url = f'https://app.thestorygraph.com/browse?search_term={split_list[0]}%20{split_list[1]}%20{split_list[2]}%20{split_list[3]}'
    if len(split_list) == 3:
        url = f'https://app.thestorygraph.com/browse?search_term={split_list[0]}%20{split_list[1]}%20{split_list[2]}'
    if len(split_list) == 2:
        url = f'https://app.thestorygraph.com/browse?search_term={split_list[0]}%20{split_list[1]}'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }

    content = requests.get(url, headers=headers).text
    soup = bs(content, 'html.parser')
    #print(soup)

    search = soup.find(class_='book-cover')
    #print(search)
    #print("break")
    if search == None:
        continue
    else:
        first_link = search.find('a')
        #print(first_link)
        #print("skip")
        #print((first_link['href']))

        storygraph_links.append("https://app.thestorygraph.com/" + str(first_link['href']))

    time.sleep(random.choice(rate))


print(storygraph_links)
#print(len(goodreads_links))

storygraph_export = pd.DataFrame({"links": storygraph_links})
#print(goodreads_export)

storygraph_export.to_csv(r'storygraph_links_weekly1523_morethan one_CSV.csv')
