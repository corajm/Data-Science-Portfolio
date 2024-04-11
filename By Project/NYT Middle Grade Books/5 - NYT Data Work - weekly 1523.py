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

counts_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/countsANDtags_weekly1523_CSV_NOCOOKBOOKS.csv")
#print(counts_pd)

counts_list = list(counts_pd.iloc[:,1])
print(counts_list)

tags_01_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/countsANDtags_weekly1523_CSV_tags.csv")
#print(tags_01_pd)
#tags_02_pd = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/NYT_MG_WEEKLY_1523_TAGScapped_CSV_02.csv")
#print(tags_02_pd)

#### PT 2 COMBINING TAGS LIST

#titles_01_list = list(tags_01_pd.iloc[:,0])
#titles_02_list = list(tags_02_pd.iloc[:,0])
#titles_03_list = list(tags_03_pd.iloc[:,0])

#titles = list(set(titles_01_list) | set(titles_02_list))
#titles = list(set(titles_half) | set(titles_03_list))

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

        for row in rows:
            listOfPos.append((row, col))

    # This list contains a list tuples with
    # the index of element in the dataframe
    return row

#for item in titles:
    #if item not in tags_01_pd.values:
        #tags_01_pd.loc[len(tags_01_pd.index)] = tags_02_pd.iloc[getIndexes(tags_02_pd, item)]
#print(tags_01_pd)

#### PT 3 COUNT TAGS

tags_01_list = list(tags_01_pd.iloc[:,2])
#print(tags_01_list)

alltags =[]
tags_by_book = []

for taglist in tags_01_list:
    book = []
    newlist = taglist.split("'")
    for tag in newlist:
        if tag != ", ":
            if tag != "[":
                if tag != "]":
                    alltags.append(tag)
                    book.append(tag)
    tags_by_book.append(book)
#print(len(alltags))

unique_tags = list(set(alltags))

count = []

for tag in unique_tags:
    how_many = alltags.count(tag)
    count.append(how_many)

tags_and_counts_dict = dict(zip(unique_tags, count))
tags_and_counts = pd.Series(tags_and_counts_dict)
#print(tags_and_counts)

#tags_and_counts.to_csv(r'tag_counts_weekly1523_CSV_USE2.csv')

titles_01_list = list(tags_01_pd.iloc[:,0])

total_count = {}

for i in range(0,(len(tags_by_book))):
    for tag in tags_by_book[i]:
        if tag in total_count:
            d = {tag: total_count.get(tag) + tags_and_counts.loc[tag]*counts_pd.iloc[i,1]}
            total_count.update(d)
        else:
            total_count[tag] = tags_and_counts.loc[tag]*counts_pd.iloc[i,1]

#print(total_count)

total_count_series = pd.Series(total_count)
#print(total_count_series)

total_count_series.to_csv(r'total_tag_count_weekly1523_CSV_USE2.csv')
