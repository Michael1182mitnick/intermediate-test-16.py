# Implement a Least Recently Used (LRU) cache with a fixed capacity.

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()  # Initialize an OrderedDict to store the cache
        self.capacity = capacity    # Fixed capacity of the cache

    def get(self, key):
        if key not in self.cache:
            return -1  # Key not found in the cache
        else:
            # Move the accessed key to the end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]  # Return the value of the key

    def put(self, key, value):
        if key in self.cache:
            # Update the key's value and move it to the end (most recently used)
            self.cache.move_to_end(key)
        self.cache[key] = value  # Insert or update the value of the key
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (first item in OrderedDict)
            self.cache.popitem(last=False)


# Example usage
lru_cache = LRUCache(3)  # Create an LRU cache with capacity 3

lru_cache.put(1, 1)
lru_cache.put(2, 2)
lru_cache.put(3, 3)

# Output: 1 (key 1 is accessed, so it becomes most recently used)
print(lru_cache.get(1))

lru_cache.put(4, 4)  # Adding key 4 will evict key 2 (least recently used)

print(lru_cache.get(2))  # Output: -1 (key 2 has been evicted)

# Output: 3 (key 3 is accessed, so it becomes most recently used)
print(lru_cache.get(3))

lru_cache.put(5, 5)  # Adding key 5 will evict key 1 (least recently used)

print(lru_cache.get(1))  # Output: -1 (key 1 has been evicted)
print(lru_cache.get(4))  # Output: 4
print(lru_cache.get(5))  # Output: 5
