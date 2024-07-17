#!/usr/bin/env python3
"""Cache Class"""
import redis
from uuid import uuid4
from typing import Union


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
