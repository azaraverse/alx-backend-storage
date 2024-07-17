#!/usr/bin/env python3
"""Cache Class"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator that takes a single argument and returns a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        A wrapped Callable function that increments the count for a key
        every time method is called and returns the value returned by the
        original method.
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Stores the history of inputs and outputs for a particular function
    """
    input_list_keys, output_list_keys = (
        method.__qualname__ + ":inputs",
        method.__qualname__ + ":outputs",
    )

    @wraps(method)
    def wrapper(self, *args):
        """
        A wrapped callable function for call_history that returns the inputs
        and ouputs of a function it decorates
        """
        self._redis.rpush(input_list_keys, str(args))
        exc = method(self, *args)
        self._redis.rpush(output_list_keys, exc)

        return exc
    return wrapper


class Cache:
    """The Cache Class"""
    def __init__(self) -> None:
        """Init method that stores an instance of the Redis Client"""
        # store instance of Redis Client as a private variable
        self._redis = redis.Redis()
        # flush the instance using flushdb
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument, generates a random uuid key and stores the
        data argument in Redis using the key generated.

        Args:
            data: data to store

        Returns:
            key (str): random generated key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Takes a key string argument and a callable argument and converts
        the key using the callable to a desired format.
        """
        data = self._redis.get(key)

        # if a conversion method is given, use it to format the data
        if fn:
            converted_data = fn(data)
            return converted_data
        # if the conversion format is explicitly int, use get_int
        if fn == int:
            return self.get_int(data=data)
        # if the conversion format is explicitly str, use get_str
        if fn == str:
            return self.get_str(data=data)
        # if no conversion format is given, return data as is
        return data

    def get_str(self, data: bytes) -> str:
        """Method that converts data in bytes to its string representation
        """
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """Method that converts data in bytes to an integer"""
        return int(data)
