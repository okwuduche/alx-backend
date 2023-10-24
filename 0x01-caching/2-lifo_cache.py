#!/usr/bin/env python3
"""2. LIFO caching"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching
    and is a caching system"""
    def __init__(self) -> None:
        super().__init__()
        self.__last_in = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data.keys():
                if len(self.cache_data) == self.MAX_ITEMS:
                    last_key = self.__last_in.pop()
                    del self.cache_data[last_key]
                    print(f"DISCARD: {last_key}")
            else:
                del self.__last_in[self.__last_in.index(key)]
            self.__last_in.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
