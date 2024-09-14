import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://www.globo.com/'

    homepage = requests.get(url)
    soup = BeautifulSoup(homepage.text, 'html.parser')

    links = soup.find_all('a')
    tgt_class1 = 'post__title'
    tgt_class2 = 'post-multicontent__link--title__text'

    news = {}
    for link in links:
        if(link.h2 != None and link.h2.get('class') != None):
            if tgt_class1 in link.h2.get('class'):
                news[link.h2.text] = link.get('href')
            if tgt_class2 in link.h2.get('class'):
                news[link.h2.text] = link.get('href')
    return news

teste = get_news()
print(list(teste))