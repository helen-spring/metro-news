import datetime

import bs4
import requests

from datasources.date_format import get_date


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
    for link in links:
        result = requests.get(f'{url}{link}')
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        title = soup.select('h1.pagetitle__content-title')
        pub_date = soup.select('div.pagetitle__content-date')
        post_data = []
        if len(pub_date) > 0:
            date_str = pub_date[0].getText()
            date_formatted = get_date(date_str)
            post_data.append(title[0].getText())
            post_data.append(date_formatted)
            for image in images:
                post_data.append(image.attrs['src'])
            now = datetime.datetime.now()
            post_data.append(now.strftime("%d-%m-%Y %H:%M"))
        news_list.append(post_data)
    return news_list
