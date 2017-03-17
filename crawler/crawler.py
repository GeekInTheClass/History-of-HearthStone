from datetime import datetime
def timestamp():
    return str(datetime.now())[:10]

data_folder = 'data/'
data_format = '.json'
import json
from os import listdir
def load(reload=False):
    news = [ int(n[:-len(data_format)]) for n in listdir(data_folder) ]
    return (reload or not news) and -1 or max(news)

def save(name, data):
    if name.isdigit():
        with open(data_folder + name + data_format, 'w') as f:
            json.dump(data, f)


domain = 'http://kr.battle.net'
query = '/hearthstone/ko/blog/infinite?page='
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import bs4
def get(href):
    content = urlopen('http://' in href and href or domain + href).read()
    soup = bs(content, 'lxml')
    try:
        title = soup.find('div', {'class': 'article-header'}).find('h2').text
        date = soup.find('div', {'class': 'article-meta'}).find('span').text
        text = soup.find('div', {'class': 'article-content'}).text
        return {'title': title, 'date': date, 'text': text}
    except:
        return {'title': '', 'date': '', 'text':''}

def crawl(last=0):
    page = 0
    while True:
        content = urlopen(domain + query + str(page)).read()
        if not content: break
        soup = bs(content, 'lxml')
        news = soup.findAll("h3", { "class" : "article-title" })
        for n in news:
            href = n.find('a')['href']
            href = href[:href.rfind('/')]
            name = href[href.rfind('/') + 1:]
            if not name.isdigit(): continue
            if int(name) <= last: 
                print ('done. ' + str(last))
                break
            save(name, get(href))
        page+=1

if __name__ == '__main__':
    last = load()
    crawl(last=last)


