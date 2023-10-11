#!/usr/bin/env python3
"""class cache
"""
import redis
import uuid
from typing import Union


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
