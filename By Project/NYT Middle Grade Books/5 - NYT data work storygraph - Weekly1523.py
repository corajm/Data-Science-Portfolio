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
#print(counts_list)

attributes_df = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./NYT_MG_WEEKLY_1523_TAGSstorygraph_CSV.csv")

desc_list = list(attributes_df['other descriptors'])

descriptors_by_book = []

for descs in desc_list:
    book = []
    newlist = descs.split(',')
    for tag in newlist:
        book.append(tag)
    descriptors_by_book.append(book)


descriptors_by_book_clean = []
for book in descriptors_by_book:
    book2 = []
    if len(book) == 5:
        if (book[0])[0:6] == "['A mi":
            book2.append("a mix of plot and character driven")
        elif (book[0])[0:6] == '["A mi':
            book2.append("a mix of plot and character driven")
        elif (book[0])[0:3] == "['C":
            book2.append("Character Driven")
        elif (book[0])[0:3] == '["C':
            book2.append("Character Driven")
        elif (book[0])[0:3] == "['P":
            book2.append("Plot Driven")
        elif (book[0])[0:3] == '["P':
            book2.append("Plot Driven")
        elif (book[0])[0:5] == "['N/A":
            book2.append("N/A")
        elif (book[0])[0:5] == '["N/A':
            book2.append("N/A")
        if (book[1])[0:5] == " 'It'":
            book2.append("Character Development is complicated")
        elif (book[1])[0:3] == ' "I':
            book2.append("Character Development is complicated")
        elif (book[1])[0:4] == " 'Ye":
            book2.append("Strong Character Development")
        elif (book[1])[0:4] == ' "Ye':
            book2.append("Strong Character Development")
        elif (book[1])[0:4] == " 'No":
            book2.append("Not strong character development")
        elif (book[1])[0:4] == ' "No':
            book2.append("Not strong character development")
        elif (book[1])[0:5] == " 'N/A":
            book2.append("N/A")
        elif (book[1])[0:5] == ' "N/A':
            book2.append("N/A")
        if (book[2])[0:6] == " 'It's":
            book2.append("It's Complicated (Lovable)")
        elif (book[2])[0:3] == ' "I':
            book2.append("It's Complicated (Lovable)")
        elif (book[2])[0:5] == " 'Yes":
            book2.append("Lovable Characters")
        elif (book[2])[0:5] == ' "Yes':
            book2.append("Lovable Characters")
        elif (book[2])[0:4] == " 'No":
            book2.append("NonLovable Characters")
        elif (book[2])[0:4] == ' "No':
            book2.append("NonLovable Characters")
        elif (book[2])[0:5] == " 'N/A":
            book2.append("N/A")
        elif (book[2])[0:5] == ' "N/A':
            book2.append("N/A")
        if (book[3])[0:6] == " 'It's":
            book2.append("It's Complicated (Diverse)")
        elif (book[3])[0:3] == ' "I':
            book2.append("It's Complicated (Diverse)")
        elif (book[3])[0:5] == " 'Yes":
            book2.append("Diverse Cast")
        elif (book[3])[0:5] == ' "Yes':
            book2.append("Diverse Cast")
        elif (book[3])[0:4] == " 'No":
            book2.append("Not Diverse Cast")
        elif (book[3])[0:4] == ' "No':
            book2.append("Not Diverse Cast")
        elif (book[3])[0:5] == " 'N/A":
            book2.append("N/A")
        elif (book[3])[0:5] == ' "N/A':
            book2.append("N/A")
        if (book[4])[0:6] == " 'It's":
            book2.append("It's Complicated (Flaws)")
        elif (book[4])[0:3] == ' "I':
            book2.append("It's Complicated (Flaws)")
        elif (book[4])[0:5] == " 'Yes":
            book2.append("Flaws of Character is Main Focus")
        elif (book[4])[0:5] == ' "Yes':
            book2.append("Flaws of Character is Main Focus")
        elif (book[4])[0:4] == " 'No":
            book2.append("Flaws of C not a Main Focus")
        elif (book[4])[0:4] == ' "No':
            book2.append("Flaws of C not a Main Focus")
        elif (book[4])[0:5] == " 'N/A":
            book2.append("N/A")
        elif (book[4])[0:5] == ' "N/A':
            book2.append("N/A")
    else:
        book2.append("NONE")
    if len(book2) != 5:
        book2 = ["NONE"]
    descriptors_by_book_clean.append(book2)

alldescriptors = []

for desc_list in descriptors_by_book_clean:
    for desc in desc_list:
        alldescriptors.append(desc)

unique_descriptors = list(set(alldescriptors))

descriptors_count = []

for desc in unique_descriptors:
    how_many = alldescriptors.count(desc)
    descriptors_count.append(how_many)

descriptors_and_counts_dict = dict(zip(unique_descriptors, descriptors_count))
descriptors_and_counts = pd.Series(descriptors_and_counts_dict)

#### PT 3 COUNT TAGS

genretags_list = list(attributes_df['genre tags'])
moodtags_list = list(attributes_df['mood tags'])
#print(tags_01_list)

allgenretags =[]
genretags_by_book = []

for taglist in genretags_list:
    book = []
    newlist = taglist.split("'")
    for tag in newlist:
        if tag != ", ":
            if tag != "[":
                if tag != "]":
                    allgenretags.append(tag)
                    book.append(tag)
    genretags_by_book.append(book)

allmoodtags =[]
moodtags_by_book = []

for taglist in moodtags_list:
    book = []
    newlist = taglist.split("'")
    for tag in newlist:
        if tag != ", ":
            if tag != "[":
                if tag != "]":
                    allmoodtags.append(tag)
                    book.append(tag)
    moodtags_by_book.append(book)
#print(len(alltags))

unique_genretags = list(set(allgenretags))
unique_moodtags = list(set(allmoodtags))

genrecount = []
moodcount = []

for tag in unique_genretags:
    how_many = allgenretags.count(tag)
    genrecount.append(how_many)

for tag in unique_moodtags:
    how_many = allmoodtags.count(tag)
    moodcount.append(how_many)

genretags_and_counts_dict = dict(zip(unique_genretags, genrecount))
genretags_and_counts = pd.Series(genretags_and_counts_dict)

moodtags_and_counts_dict = dict(zip(unique_moodtags, moodcount))
moodtags_and_counts = pd.Series(moodtags_and_counts_dict)
#print(tags_and_counts)

#genretags_and_counts.to_csv(r'genre_counts_storygraph_weekly1523_CSV.csv')
#moodtags_and_counts.to_csv(r'mood_counts_storygraph_weekly1523_CSV.csv')
#descriptors_and_counts.to_csv(r'descript_counts_storygraph_weekly1523_CSV.csv')

