#!/usr/bin/env python3
"""Cache Class"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional, Any


class Cache:
    """The Cache Class"""
    def __init__(self) -> None:
        """Init method that stores an instance of the Redis Client"""
        # store instance of Redis Client as a private variable
        self._redis = redis.Redis()
        # flush the instance using flushdb
        self._redis.flushdb()

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

    def get(self, key: str, fn: Optional[Callable]) -> Any:
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
