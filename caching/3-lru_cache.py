#!/usr/bin/env python3
""" task 3 Create a class LRUCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ creating LRUCache class """
    def __init__(self):
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """ adding an item to cache and implenting LRU """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used = self.insertion_order.pop()
                del self.cache_data[least_used]
                print(f"DISCARD: {least_used}")
            self.cache_data[key] = item

    def get(self, key):
        """ returns item by key """
        if key is not None:
            self.insertion_order.append(key)
            return self.cache_data.get(key, None)
