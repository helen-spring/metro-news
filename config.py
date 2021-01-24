import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = ''
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
