import datetime

import bs4
import requests

from datasources.date_format import get_date
from main import rq


@rq.job(timeout=600)
def get_all_news(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    images = soup.find_all('img', {'class': 'newslist__image'})
    news_link = soup.find_all('a', {'class': 'newslist__link'})
    links = []
    for i in news_link:
        link = i.attrs['href']
        link = link.strip('/press/news/')
        links.append(link)
    news_list = []
    i = 0
    for link in links:
        article = get_article(url, link)
        article.append(images[i].attrs['src'])
        news_list.append(article)
        i += 1
    return news_list


def get_article(url, link):
    result = requests.get(f'{url}{link}')
    soup = bs4.BeautifulSoup(result.text, "html.parser")
    title = soup.select('h1.pagetitle__content-title')
    pub_date = soup.select('div.pagetitle__content-date')
    article_data = []
    if len(pub_date) > 0:
        date_str = pub_date[0].getText()
        date_formatted = get_date(date_str)
        article_data.append(title[0].getText())
        article_data.append(date_formatted)
        now = datetime.datetime.now()
        article_data.append(now.strftime("%d-%m-%Y %H:%M"))
    return article_data
