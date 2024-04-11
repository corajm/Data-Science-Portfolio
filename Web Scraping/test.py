#### PT 1 IMPORTING EVERYTHING

import pip

if int(pip.__version__.split('.')[0]) > 9:
    from pip._internal import main
else:
    from pip import main
def install(package):
    main(['install', package])

install('BeautifulSoup4')
install('numpy')
install("pandas")
install("requests")
install("matplotlib")
install("selenium")
install("webdriver-manager")


# set up selenium
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.chrome.service import Service
import json
import requests
import random
from random import randint
from time import sleep
# path to the chrdmedriver executable
chromedriver = "Projects/current projects/chromedriver"
# tell the os where the chromedriver is
#os.environ["webdriver.chrome.driver" ] = chromedriver
# setup Chrome headless
chrome_options = ChromeOptions()
chrome_options.add_argument('headless')

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


# the function for scraping game list pages
def gamelist_scrape(start, stop):
    '''
    This function is used to scrape data from the boardgame rank list pages.
    Each page has 100 games. The page loop will loop through page by page and row by row,
    to collect data from each game entry, then assign them to the gamelisttable.
    '''

    boardgame = []
    objectid = []
    pagelink = []

    # request each page.
    for page in range(start, stop):
        pagenum = str(page + 1)
        url = f"https://boardgamegeek.com/boardgamefamily/8374/crowdfunding-kickstarter/linkeditems/boardgamepublisher?pageid={pagenum}"


        my_user_agent = random.choice(user_agent_list)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--user-agent={my_user_agent}")

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        soup = bs(driver.page_source, "lxml")
        #test2 = soup.find_all("div")
        # print(test2)
        script = soup.find_all('linked-items-module')[0]
        script2 = script.find_all(class_="media")
        for i in range(0,25):
            game = script2[i]

            link1= game.find("a")
            linkstr = str(link1)
            idx1 = linkstr.index("<")
            idx2 = linkstr.index(">")
            res = linkstr[idx1 + 1: idx2]
            res2 = res[linkstr.index('"'):]
            res3 = res2[:res2.index('"')]
            link = "https://boardgamegeek.com"+res3

            x = res3.split("/")
            obid = x[2]

            titlex = game.find(class_="ng-binding").text
            title = titlex.lstrip()[:-7]

            boardgame.append(title)
            objectid.append(obid)
            pagelink.append(link)

            KickStarted = pd.DataFrame(
                {"boardgame": boardgame, "objectid": objectid, "link": pagelink})

        driver.quit()

        sleep(randint(0, 1))
        #if len(boardgame) >50:
            #break
        # time.sleep(1)
    return KickStarted

#KickStartedFull = gamelist_scrape(33,36)

#KickStartedFull.to_csv(r'GamesWithKick14.csv')

#for i in range(170,626):
    #KickStartedFull = gamelist_scrape(i,i+1)
    #KickStartedFull.to_csv(rf'GamesWithKick{i}.csv')

missing2 = range(305,626)
for j in range(1, 600):
    missing = []
    for i in missing2:
        try:
            KickStartedFull = gamelist_scrape(i, i + 1)
            KickStartedFull.to_csv(rf'GamesWithKick{i}.csv')
        except:
            missing.append(i)
    missing2 = []
    for i in missing:
        try:
            KickStartedFull = gamelist_scrape(i, i + 1)
            KickStartedFull.to_csv(rf'GamesWithKick{i}.csv')
        except:
            missing2.append(i)