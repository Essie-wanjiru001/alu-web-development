#!/usr/bin/python3
""" MRU cache """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU caching system """

    def __init__(self):
        """ Initialize MRU caching system """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If key exists, move it to the end of the list
        if key in self.cache_data:
            del self.cache_data[key]

        # If cache is at maximum capacity, remove the most recently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = list(self.cache_data.keys())[0]
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

        # Add the new item
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the list
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item

        return item


if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
