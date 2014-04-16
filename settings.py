from os import environ as env

REDIS_HOST = env.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(env.get('REDIS_PORT', 6379))
REDIS_DB = int(env.get('REDIS_DB', 0))
REDIS_PASS = env.get('REDIS_PASS', None)

PASSWORD = env.get('PASSWORD', 'password')
SECRET_KEY = env.get('SECRET_KEY', 'UeYYonX1w9jSGAaCwu3hy9tp2le1dSxrNHodn0HXpH3CzvxZCoBvnJUgNZI9mGJi')
