
#### PT 1 IMPORTING EVERYTHING

import pip

if int(pip.__version__.split('.')[0]) > 9:
    from pip._internal import main
else:
    from pip import main
def install(package):
    main(['install', package])

install('BeautifulSoup4')
install("pandas")
install("requests")

from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep
import random
import pickle
import pandas as pd
import requests
import re
import random
from random import randint




Links_csv = pd.read_csv(r"/Users/coramcanulty/Desktop/AO3_Scrape_2/ao3links01.csv")
urls = list(Links_csv.get("links"))

#### USER AGENTS

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


#### FUNCTION

def ao3_scrape(start, stop):
    '''
    This function is used to scrape data. First we scrape links then scrape info from specific pages
    '''

    ###Now we have our links, we're going to go through this link of lists to scrape facts about the fics

    ## What we want to get
    objectid = []
    titles = []
    authors = []
    ratings = []
    warnings = []
    relationship_cats = []
    fandoms = []
    relationships = []
    characters = []
    freeforms = []
    languages = []
    series = []
    published = []
    completed = []
    status_date = []
    words = []
    chapters = []
    comments = []
    kudos = []
    bookmarks = []
    hits = []

    links = urls[start: stop]
    print(links)

    for url in links:

        user_agent = random.choice(user_agent_list)

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'User-Agent': user_agent,
        }

        page = requests.get(url, headers= headers)
        if page:
            print("yes")
        else:
            print("no")

        soup = bs(page.content)

        obid1 = url[34:]
        idx1 = obid1.index('/')
        objectidin = obid1[:idx1]
        objectid.append(objectidin)

        title = soup.find(class_="title heading")
        title2 = title.text.strip()
        titles.append(title2)

        author = soup.find(class_="byline heading")
        if author:
            author2 = author.text.strip()
            authors.append(author2)
        else:
            authors.append("NA")

        rating = soup.find_all(class_="rating tags")
        if rating:
            rating2 = rating[1].find_all(class_="tag")
            rating3 = rating2[0].text
            ratings.append(rating3)
        else:
            ratings.append("NA")

        warn = soup.find_all(class_="warning tags")
        if warn:
            warn2 = [i.text for i in warn[1].find_all(class_='tag')]
            warnings.append(warn2)
        else:
            warnings.append("NA")

        cat = soup.find_all(class_="category tags")
        if cat:
            cat2 = [i.text for i in cat[1].find_all(class_='tag')]
            relationship_cats.append(cat2)
        else:
            relationship_cats.append("NA")

        fan = soup.find_all(class_="fandom tags")
        if fan:
            fan2 = [i.text for i in fan[1].find_all(class_='tag')]
            fandoms.append(fan2)
        else:
            fandoms.append("NA")

        rel = soup.find_all(class_="relationship tags")
        if rel:
            rel2 = [i.text for i in rel[1].find_all(class_='tag')]
            relationships.append(rel2)
        else:
            relationships.append("NA")

        char = soup.find_all(class_="character tags")
        if char:
            char2 = [i.text for i in char[1].find_all(class_='tag')]
            characters.append(char2)
        else:
            characters.append("NA")

        ff = soup.find_all(class_="freeform tags")
        if ff:
            ff2 = [i.text for i in ff[1].find_all(class_='tag')]
            freeforms.append(ff2)
        else:
            freeforms.append("NA")

        lang = soup.find_all(class_="language")
        if lang:
            lang2 = lang[1].text.strip()
            languages.append(lang2)
        else:
            languages.append("NA")

        ser = soup.find_all(class_="series")
        if ser:
            series.append(1)
        else:
            series.append(0)

        pub = soup.find_all(class_="published")
        if pub:
            pub2 = pub[1].text
            published.append(pub2)
        else:
            published.append("NA")

        comp = soup.find_all(class_="status")
        if comp:
            comp2 = comp[0].text
            comp3 = comp2[:-1]
            completed.append(comp3)
        else:
            completed.append("Completed")

        stat = soup.find_all(class_="status")
        if stat:
            stat2 = stat[1].text
            status_date.append(stat2)
        else:
            status_date.append("NA")

        word = soup.find_all(class_="words")
        if word:
            word2 = word[1].text
            words.append(word2)
        else:
            words.append("NA")

        chap = soup.find_all(class_="chapters")
        if chap:
            chap2 = chap[1].text
            indxch = chap2.index("/")
            chap3 = chap2[:indxch]
            chapters.append(chap3)
        else:
            chapters.append("NA")

        com = soup.find_all(class_="comments")
        if com:
            com2 = com[2].text
            comments.append(com2)
        else:
            comments.append("NA")

        kud = soup.find_all(class_="kudos")
        if kud:
            kud2 = kud[1].text
            kudos.append(kud2)
        else:
            kudos.append("NA")

        bm = soup.find_all(class_="bookmarks")
        if bm:
            bm2 = bm[1].text
            bookmarks.append(bm2)
        else:
            bookmarks.append("NA")

        hit = soup.find_all(class_="hits")
        if hit:
            hit2 = hit[1].text
            hits.append(hit2)
        else:
            hits.append("NA")


    #print(titles)
    #print(authors)
    #print(ratings)
    #print(warnings)
    #print(relationship_cats)
    #print(fandoms)
    #print(relationships)
    #print(characters)
    #print(freeforms)
    #print(languages)
    #print(series)
    #print(published)
    #print(completed)
    #print(status_date)
    #print(words)
    #print(chapters)
    #print(comments)
    #print(kudos)
    #print(bookmarks)
    #print(hits)

    #print(len(links))
    #print(len(objectid))
    #print(len(titles))
    #print(len(authors))
    #print(len(ratings))
    #print(len(warnings))
    #print(len(relationship_cats))
    #print(len(fandoms))
    #print(len(relationships))
    #print(len(characters))
    #print(len(freeforms))
    #print(len(languages))
    #print(len(series))
    #print(len(published))
    #print(len(completed))
    #print(len(status_date))
    #print(len(words))
    #print(len(chapters))
    #print(len(comments))
    #print(len(kudos))
    #print(len(bookmarks))
    #print(len(hits))

    fanfic = pd.DataFrame(
        {"links": links, "objectid": objectid, "title": titles, "author": authors, "rating": ratings,
         "warnings": warnings, "relationship_cat": relationship_cats, "fandoms": fandoms, "relationships": relationships,
         "characters": characters, "freeforms": freeforms, "language": languages, "series": series, "published": published,
         "completed": completed, "status_date": status_date, "word_count": words, "chapters": chapters,
         "comments": comments, "kudos": kudos, "bookmarks": bookmarks, "hits": hits})

    sleep(randint(0, 5))

    return fanfic


missing2 = range(15000,18000)
for k in range(1,1000):
    missing = []
    for i in missing2:
        start = i -1
        stop = i
        try:
            fanfic = ao3_scrape(start,stop)
            fanfic.to_csv(rf'fics{i}.csv')
        except:
            missing.append(i)
            sleep(randint(0, 1))
    missing2 =[]
    for j in missing:
        start = j-1
        stop = j
        try:
            fanfic = ao3_scrape(start,stop)
            fanfic.to_csv(rf'fics{j}.csv')
        except:
            missing.append(j)
            sleep(randint(0, 1))










