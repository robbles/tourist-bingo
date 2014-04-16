from redis import StrictRedis
import random

import settings

redis = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB, password=settings.REDIS_PASS)

class ShuffledSet(object):
    def __init__(self, key):
        self.key = key

    def all(self):
        return redis.smembers(self.key)

    def subset(self, count):
        all_targets = list(self.all())
        random.shuffle(all_targets)
        return all_targets[:count]

    def add(self, text):
        redis.sadd(self.key, text)

    def remove(self, text):
        redis.srem(self.key, text)
