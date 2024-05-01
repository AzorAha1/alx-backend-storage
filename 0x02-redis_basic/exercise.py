#!/usr/bin/env python3
"""this is a class"""
import redis
import uuid
from typing import Union
from typing import Callable
from typing import Optional


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

    def get(self, key: str, fn: Optional[Callable]) -> str:
        """_summary_

        Args:
            key (str): _description_
            fn (Callable[[str], str]): _description_

        Returns:
            str: _description_
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """_summary_

        Args:
            key (str): _description_

        Returns:
            str: _description_
        """
        value = self._redis.get(key)
        return self.get(key=key, fn=value.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """_summary_

        Args:
            key (int): _description_

        Returns:
            int: _description_
        """
        return self.get(key, int)

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
