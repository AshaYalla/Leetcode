class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if(key in self.cache):
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.cap:
                self.cache.popitem(last = False)
            self.cache[key] = value
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)