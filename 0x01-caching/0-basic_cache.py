#!/usr/bin/env python3
"""
This module implements a basic cache class BasicCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that implements the BaseCaching class
    """
    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache

        Arguments:
            key: key for the dictionary
            item: value to assign to the key

        Returns:
            Nothing
        """
        if (key is not None) and (item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a key-value pair from the cache

        Arguments:
            key: key to retrieve from the cache

        Returns:
            Value in cache linked to key, or None if key not found
        """
        return self.cache_data.get(key, None)
