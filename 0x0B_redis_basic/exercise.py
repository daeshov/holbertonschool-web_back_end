#!/usr/bin/env python3

"""class cache
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps

# Decorator to count method calls
def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        count_key = method.__qualname__
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)
    return wrapper
    
@count_calls
def get(self, key: str, fn: Callable = None):
    data = self._redis.get(key)
    if data is not None and fn is not None:
        return fn(data)
    return data


 # Decorator to store input and output history
def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
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

@staticmethod
def replay(method: Callable):
    qualified_name = method.__qualname__
    input_list_key = f"{qualified_name}:inputs"
    output_list_key = f"{qualified_name}:outputs"
    
    inputs = Cache._redis.lrange(input_list_key, 0, -1)
    outputs = Cache._redis.lrange(output_list_key, 0, -1)
    
    print(f"{qualified_name} was called {len(inputs)} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{qualified_name}({input_str}) -> {output_str}")


class Cache:
    def __init__(self):
        # Initialize a Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

   