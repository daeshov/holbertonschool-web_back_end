#!/usr/bin/python3
""" task 0 Create a class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ creating class """


def put(self, key, item):
    """ adding item to cache """
    if key is None or item is None:
        self.cache_data[key] = item


def get(self, key):
    """ returns value linked to key """
    if key is None:
        return None
    return self.cache_data.get(key, None)
