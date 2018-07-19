from kadal.utils import camel2snake


class User:
    def __init__(self, json):
        d = json['data']['User']
        if d.get('avatar'):
            d['avatar'] = d['avatar']['large']
        for k, v in d.items():
            setattr(self, camel2snake(k), v)
