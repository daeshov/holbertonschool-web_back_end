#!/usr/bin/env python3
""" task 2 Create a class LIFOCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ creating LIFOCache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ adding an item to cache and implenting LIFO """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_item = self.insertion_order.pop()
                del self.cache_data[last_item]
                print(f"DISCARD: {last_item}")

            self.cache_data[key] = item
            self.insertion_order.append(key)

    def get(self, key):
        """ returns item by key """
        if key is not None:
            return self.cache_data.get(key, None)
