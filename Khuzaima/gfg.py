import requests
from bs4 import BeautifulSoup as bs

import pandas as pd

from random import randint
from time import sleep


# URL = 'https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv'
URL = 'https://www.geeksforgeeks.org/page/'

names = []
numbers = []
n = 0

for page in range(1, 10):
    # pls note that the total number of
    # pages in the website is more than 5000 so i'm only taking the
    # first 10 as this is just an example

    print(f"scrapping page: {page}")

    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})

    for i in range(4, 19):
        n = n+1
        print (n)
        names.append(titles[i].text.strip())
        numbers.append(n)
        '''if page > 1:
            print(f"{(i - 3) + page * 15}" + titles[i].text)
        else:
            print(f"{i - 3}" + titles[i].text)'''

    sleep(randint(3, 15))

print("done")

df = pd.DataFrame({"Numbers":numbers, "Topics":names})
# print(df.type())
print(df.to_string())
