import re


def camel2snake(s) -> str:
    return re.sub(r"([A-Z])", r"_\1", s).lower()
