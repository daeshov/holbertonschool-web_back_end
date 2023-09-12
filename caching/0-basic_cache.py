#!/usr/bin/env python3
""" task 0 Create a class BasicCache that inherits from BaseCaching
and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ creating class """

    def put(self, key, item):
        """ adding an item to cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ returns item by key """
        if key is not None:
            return self.cache_data.get(key, None)
