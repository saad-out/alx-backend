#!/usr/bin/env python3
"""
This module implements a LRU caching algorithm.
"""
from base_caching import BaseCaching


def get_lru_item(lru_dict):
    """
    Get the least recently used item from a dictionary of items.

    Args:
        lru_dict (dict): Dictionary of items to evaluate.

    Returns:
        The key of the least recently used item.
    """
    lru = None
    for key, rank in lru_dict.items():
        if lru is None:
            lru = key
        else:
            lru = key if rank < lru_dict[lru] else lru
    return lru


class LRUCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        super().__init__()
        self.lru_track = dict()
        self.RANK = 0

    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache.

        Args:
            key (str): Key to insert into the cache.
            item (str): Value to insert into the cache.

        Returns:
            Nothing.
        """
        if (key is None) or (item is None):
            return

        key_not_found = key not in self.cache_data
        full_cache = len(self.cache_data) >= self.MAX_ITEMS
        if key_not_found and full_cache:
            lru_key = get_lru_item(self.lru_track)
            try:
                del self.lru_track[lru_key]
                del self.cache_data[lru_key]
            except KeyError:
                raise Exception("Erro while discarding LRU item.")
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.lru_track[key] = self.RANK
        self.RANK += 1

    def get(self, key):
        """
        Retrieves a key-value pair from the cache.

        Args:
            key (str): Key to retrieve from the cache.

        Returns:
            Value in cache linked to key, or None if key not found.
        """
        if key in self.lru_track:
            self.lru_track[key] = self.RANK
            self.RANK += 1
        return self.cache_data.get(key)
