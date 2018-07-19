from kadal.utils import camel2snake
from collections import namedtuple


UserStats = namedtuple("UserStats", "watched_time chapters_read")


class User:
    def __init__(self, json):
        d = json['data']['User']
        d['stats'] = UserStats(d['stats']['watchedTime'], d['stats']['chaptersRead'])
        if d.get('avatar'):
            d['avatar'] = d['avatar']['large']
        for k, v in d.items():
            setattr(self, camel2snake(k), v)
