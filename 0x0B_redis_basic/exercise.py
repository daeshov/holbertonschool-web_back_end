#!/usr/bin/env python3

"""class cache
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


class Cache:
    def __init__(self):
        # Initialize a Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        if isinstance(data, (int, float)):
            self._redis.set(random_key, str(data))
        else:
            self._redis.set(random_key, data)
        # Return the generated key
        return random_key

    def get(self, key: str, fn: Callable = None):
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        return self.get(key, fn=int)

    # Decorator to count method calls
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            count_key = f"calls:{key}"
            self._redis.incr(count_key)
            return method(self, *args, **kwargs)
        return wrapper
    
    @count_calls
    def get(self, key: str, fn: Callable = None):
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data
