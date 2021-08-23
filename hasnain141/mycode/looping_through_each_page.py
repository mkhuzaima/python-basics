import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint

# url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
headers={"Accept-Language": "en-US, en; q=0.5"}
titles=[]
years=[]
time=[]
imdbScores=[]
metascore=[]

pages = np.arange(1,1001,50)
for page in pages:
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start=" + str(page) + "&ref_=adv_nxt", headers=headers)
    soup = BeautifulSoup(page.text,"html.parser")
    div=soup.find_all('div', class_='lister-item mode-advanced')
    sleep(randint(2,10))

    for container in div:
        # MOVIE TITLE
        name=container.h3.a.text
        titles.append(name)
        # print("\n")
        # MOVIE YEAR
        year = container.h3.find('span',class_='lister-item-year text-muted unbold').text
        years.append(year)
        # MOVIE DURATION
        runtime = container.find('span',class_='runtime').text if container.p.find('span', class_='runtime')else''
        time.append(runtime)
        # MOVIE IMDB
        imdb= float(container.strong.text)
        imdbScores.append(imdb)
        # MOVIE SCORE
        score=container.find('span',class_='metascore').text if container.find('span',class_='metascore') else '-'
        metascore.append(score)

movies= pd.DataFrame({
    'Name':titles, 
    'Year':years, 
    'Duration':time,
    'IMDB':imdbScores,
    'MetaScore':metascore
    })
movies.to_csv('Top 1000 Movies.csv')
# print(titles)
# print(years)
# print(time)
# print(imdbScores)
# print(metascore)
