import time
from datetime import timedelta

from redis import Redis
from rq import Queue

from datasources.news import get_all_news


def news_worker():
    redis_conn = Redis()
    queue = Queue(connection=redis_conn)
    job = queue.enqueue(
        timedelta(minutes=10),
        get_all_news,
        'https://mosmetro.ru/press/news/'
    )
    time.sleep(5)
    return job.result


if __name__ == '__main__':
    news = news_worker()
