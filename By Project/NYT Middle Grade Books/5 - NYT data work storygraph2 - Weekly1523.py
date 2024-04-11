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

attributes_df = pd.read_csv(r"/Users/coramcanulty/Desktop/Stacy NYT python proj./csv/SG-TagsRaw-weekly1523.csv")
#print(counts_pd)

desc_list = list(attributes_df['other descriptors'])
titles_list = list(attributes_df['titles'])

descriptors_by_book = []

for descs in desc_list:
    book = []
    newlist = descs.split(',')
    for tag in newlist:
        book.append(tag)
    descriptors_by_book.append(book)

def clean(list_of_desc):
    book2 = []
    for book in list_of_desc:
        if len(book) == 5:
            book2.append(book)
        if len(book) != 5:
            book2.append(["None"])
    book3 = []
    for book in book2:
        book_clean = []
        if book == "None":
            continue
        for item in book:
            clean1 = item.replace('"', '')
            clean2 = clean1.replace("'", "")
            clean3 = clean2.replace("[","")
            clean4 = clean3.replace("]","")
            clean5 = clean4.strip(" ")
            book_clean.append(clean5)
        book3.append(book_clean)
    return book3

clean_desclist = clean(descriptors_by_book)
#print(clean_desclist)

def PlotorChar(list_of_desc):
    Mix = []
    Character = []
    Plot = []
    for book in list_of_desc:
        if book == ["None"]:
            Mix.append("NA")
            Character.append("NA")
            Plot.append("NA")
            continue
        if book != ["None"]:
            ploc = book[0]
            #print(ploc)
            try:
                Amix_where = ploc.index("A mix")
                Amix_numstart = Amix_where + 7
                Amix_numend = Amix_numstart + 3
                Mix.append(ploc[Amix_numstart:Amix_numend])
            except ValueError:
                Mix.append("NA")
            try:
                Char_where = ploc.index("Char")
                Char_numstart = Char_where + 11
                Char_numend = Char_numstart + 3
                Character.append(ploc[Char_numstart:Char_numend])
            except ValueError:
                Character.append("NA")
            try:
                Plo_where = ploc.index("Plot")
                Plo_numstart = Plo_where + 6
                Plo_numend = Plo_numstart + 3
                Plot.append(ploc[Plo_numstart:Plo_numend])
            except ValueError:
                Plot.append("NA")

    return Mix, Plot, Character

def CharDev(list_of_desc):
    StrongCharacterDevelopment = []
    for book in list_of_desc:
        if book == ["None"]:
            StrongCharacterDevelopment.append("NA")
            continue
        if book != ["None"]:
            chardev = book[1]
            try:
                strong_where = chardev.index("Yes")
                strong_numstart = strong_where + 5
                strong_numend = strong_numstart + 3
                StrongCharacterDevelopment.append(chardev[strong_numstart:strong_numend])
            except ValueError:
                StrongCharacterDevelopment.append("NA")
    return StrongCharacterDevelopment

def LovableChar(list_of_desc):
    Lovable = []
    for book in list_of_desc:
        if book == ["None"]:
            Lovable.append("NA")
            continue
        if book != ["None"]:
            lovesec = book[2]
            try:
                love_where = lovesec.index("Yes")
                love_numstart = love_where + 5
                love_numend = love_numstart + 3
                Lovable.append(lovesec[love_numstart:love_numend])
            except ValueError:
                Lovable.append("NA")
    return Lovable

def DiverseChar(list_of_desc):
    Diverse = []
    for book in list_of_desc:
        if book == ["None"]:
            Diverse.append("NA")
            continue
        if book != ["None"]:
            divsec = book[3]
            try:
                div_where = divsec.index("Yes")
                div_numstart = div_where + 5
                div_numend = div_numstart + 3
                Diverse.append(divsec[div_numstart:div_numend])
            except ValueError:
                Diverse.append("NA")
    return Diverse

def FlawChar(list_of_desc):
    Flaws = []
    for book in list_of_desc:
        if book == ["None"]:
            Flaws.append("NA")
            continue
        if book != ["None"]:
            flawssec = book[4]
            try:
                flaws_where = flawssec.index("Yes")
                flaws_numstart = flaws_where + 5
                flaws_numend = flaws_numstart + 3
                Flaws.append(flawssec[flaws_numstart:flaws_numend])
            except ValueError:
                Flaws.append("NA")
    return Flaws

Mix1 = PlotorChar(clean_desclist)[0]
Plot1 = PlotorChar(clean_desclist)[1]
Char1 = PlotorChar(clean_desclist)[2]
CharacterDevelopment = CharDev(clean_desclist)
LovableCharecter = LovableChar(clean_desclist)
DiverseCharecter = DiverseChar(clean_desclist)
FlawCharacter = FlawChar(clean_desclist)

SG_Numbers = pd.DataFrame({"titles": titles_list, "Plot Driven": Plot1, "Character Driven": Char1, "Mix of Plot and Character": Mix1,"Strong Character Development": CharacterDevelopment, "Lovable Characters": LovableCharecter, "Diverse Characters": DiverseCharecter, "Flaws Of Characters Important": FlawCharacter })

SG_Numbers.to_csv(r'SG-Numbers_weekly1523_01.csv')

