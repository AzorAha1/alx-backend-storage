#!/usr/bin/env python3
"""this is a class"""
import redis
import uuid
from typing import Union
from typing import Callable


class Cache:
    def __init__(self):
        """_summary_
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """_summary_
        Args:
            data (any): _description_

        Returns:
            str: _description_
        """
        randomkey = str(uuid.uuid4())
        self._redis.set(name=randomkey, value=data)
        return randomkey

    def get(self, key: str, fn: Callable[[str], str]) -> str:
        """_summary_

        Args:
            key (str): _description_
            fn (Callable[[str], str]): _description_

        Returns:
            str: _description_
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data)

    def get_str(self, key: str) -> str:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            str: _description_
        """
        value = self._redis.get(key)
        return self.get(key=key, fn=value.decode('utf-8'))

    def get_int(self, key: int) -> int:
        """_summary_

        Args:
            key (int): _description_

        Returns:
            int: _description_
        """
        return self.get(key, int)
