from datasources.news import get_all_news

job = get_all_news.queue('https://mosmetro.ru/press/news/')


if __name__ == '__main__':
    job
