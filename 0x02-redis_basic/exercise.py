#!/usr/bin/env python3
"""this is a class"""
from functools import wraps
import redis
import uuid
from typing import Union
from typing import Callable
from typing import Optional


def count_calls(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """_summary_

        Returns:
            _type_: _description_
        """
        
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        Callable: _description_
    """
    qualifiedname = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs = f'{qualifiedname}:inputs'
        outputs = f'{qualifiedname}:outputs'
        self._redis.rpush(inputs, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(result))
        return result
    return wrapper
    

class Cache:
    def __init__(self):
        """_summary_
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, float, int]:
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
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """_summary_

        Args:
            key (int): _description_

        Returns:
            int: _description_
        """
        return self.get(key, int)
