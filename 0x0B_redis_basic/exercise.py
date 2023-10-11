#!/usr/bin/env python3
"""Cache Class: A class that provides caching functionality.
with method decorators."""

import redis
import uuid
from typing import Union, Callable

from functools import wraps


# Decorator to count method calls
def count_calls(method: Callable) -> Callable:
    """Decorate that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrap function for counting method calls."""
        count_key = method.__qualname__
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)

    return wrapper


@count_calls
def get(self, key: str, fn: Callable = None):
    """Get data from the cache and optionally apply a conversion function."""
    data = self._redis.get(key)
    if data is not None and fn is not None:
        return fn(data)
    return data


# Decorator to store input and output history
def call_history(method: Callable) -> Callable:
    """Decorate to store the history of inputs and outputs for a function."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrap function for storing input and output history."""
        qualified_name = method.__qualname__
        input_list_key = f"{qualified_name}:inputs"
        output_list_key = f"{qualified_name}:outputs"

        # Store input as a string
        input_str = str(args)
        self._redis.rpush(input_list_key, input_str)

        # Call the original method to retrieve the output
        output = method(self, *args, **kwargs)

        # Store the output as a string
        self._redis.rpush(output_list_key, str(output))

        return output

    return wrapper


def replay(method: Callable):
    """Display the history of calls of a particular function."""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    inputList = redis.lrange(inputs, 0, -1)
    outputList = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(inputList, outputList))
    for a, b in redis_zipped:
        attr, data = a.decode("utf-8"), b.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))


class Cache:
    """Cashe class."""

    def __init__(self):
        """Initialize the Cache class and Redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in the cache and return a key."""
        random_key = str(uuid.uuid4())
        # Store the data in Redis using the random key
        if isinstance(data, (int, float)):
            self._redis.set(random_key, str(data))
        else:
            self._redis.set(random_key, data)
        # Return the generated key
        return random_key

    def get(self, key: str, fn: Callable = None):
        """Get data from the cache and apply an optional
        conversion function."""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str):
        """Get data from the cache and convert it to a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """Get data from the cache and convert it to an integer."""
        return self.get(key, fn=int)
