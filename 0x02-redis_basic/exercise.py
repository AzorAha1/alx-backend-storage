#!/usr/bin/env python3
"""this is a class"""
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """_summary_
        Args:
            data (any): _description_

        Returns:
            str: _description_
        """
        randomkey = str(uuid.uuid4())
        self._redis.set(name=randomkey, value=data)
        return randomkey
