from enum import Enum

from kadal.utils import camel2snake


class MediaType(Enum):
    ANIME = "ANIME"
    MANGA = "MANGA"


class MediaFormat(Enum):
    TV = "TV"
    TV_SHORT = "TV_SHORT"
    MOVIE = "MOVIE"
    SPECIAL = "SPECIAL"
    OVA = "OVA"
    ONA = "ONA"
    MUSIC = "MUSIC"
    MANGA = "MANGA"
    NOVEL = "NOVEL"
    ONE_SHOT = "ONE_SHOT"


class MediaStatus(Enum):
    FINISHED = "FINISHED"
    RELEASING = "RELEASING"
    NOT_YET_RELEASED = "NOT_YET_RELEASED"
    CANCELLED = "CANCELLED"


class Media:
    def __init__(self, json, *, page=False):
        d = json if page else json['data']['Media']
        if d.get('type'):
            d['type'] = MediaType(d['type'])
        if d.get('status'):
            d['status'] = MediaStatus(d['status'])
        if d.get('format'):
            d['format'] = MediaFormat(d['format'])
        if d.get('coverImage'):
            d['coverImage'] = d['coverImage']['large']
        for k, v in d.items():
            setattr(self, camel2snake(k), v)
