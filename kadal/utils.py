import re


def camel2snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower()
