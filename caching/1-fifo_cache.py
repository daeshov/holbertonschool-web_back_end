#!/usr/bin/env python3
""" task 1 Create a class FIFOCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ creating FIFOCache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ adding an item to cache and implenting FIFO """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                old_key = next(iter(self.cache_data))
                del self.cache_data[old_key]
                print(f"DISCARD: {old_key}")

              self.cache_data[key] = item

    def get(self, key):
        """ returns item by key """
        if key is not None:
            return self.cache_data.get(key, None)
