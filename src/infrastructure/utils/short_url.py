import random
from string import ascii_letters, digits
from pydantic import HttpUrl


def create_short_url():
    url_length = 8
    symbols = ascii_letters + digits
    result = ''
    for _ in range(url_length):
        idx = random.randint(0, len(symbols) - 1)
        symbol = symbols[idx]
        result += symbol
    return result
