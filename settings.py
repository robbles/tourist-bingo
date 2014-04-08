from os import environ as env

REDIS_HOST = env.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(env.get('REDIS_PORT', 6379))
REDIS_DB = int(env.get('REDIS_DB', 10))
