#!/usr/bin/python3

"""
BaseCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
   """
   BasicCache defines an intro to use cache

   To use:
   >>> my_cache = BasicCache()
   >>> my_cache.print_cache()
   Current cache:
   """

   def put(self, key, item):
       """
       Modify cache data

       Args:
           key: Key of the dict
           item: Value of the key
       """
       if key is not None and item is not None:
           self.cache_data[key] = item

   def get(self, key):
       """
       Modify cache data

       Args:
           key: Key of the dict

       Return:
           Value associated with the key, or None if the key is not in the cache
       """
       return self.cache_data.get(key)
   