#!/usr/bin/env python3
"""Track url accessibility count"""
import requests
from functools import wraps
import redis
from typing import Callable


def cache(method: Callable) -> Callable:
    """
    Decorator to cache the result of a function call for 10 seconds
    and count accesses
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Decorator wrapper function
        """
        r = redis.Redis()
        # increment the access count for the url
        r.incr(f'count:{url}')

        # get the cached page content
        cached_page = r.get(url)
        if cached_page:
            return cached_page.decode('utf-8')

        # if not cached, get the original function
        result = method(url)

        # cache the result with a 10 sec expiration
        r.setex(url, 10, result)
        return result
    return wrapper


@cache
def get_page(url: str) -> str:
    """
    Using the requests module to obtain HTML content of a url

    Args:
        url (str): url to access

    Returns:
        The HTML content
    """
    resultponse = requests.get(url=url)
    return resultponse.text


if __name__ == '__main__':
    get_page('https://httpbin.org/delay/2')
