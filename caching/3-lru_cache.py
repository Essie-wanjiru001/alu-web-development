#!/usr/bin/python3
""" LRU cache """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching system """

    def __init__(self):
        """ Initialize LRU caching system """
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If key exists, move it to the end of the used_order list
        if key in self.cache_data:
            self.used_order.remove(key)
        self.used_order.append(key)

        # If cache is at maximum capacity, remove the least recently used item
        if len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.used_order.pop(0)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

        # Add the new item
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the used_order list
        self.used_order.remove(key)
        self.used_order.append(key)

        return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LRUCache()
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
