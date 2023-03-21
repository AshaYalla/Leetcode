class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()
        self.freq = {}
        self.lfu = 1

    def get(self, key: int) -> int:
        if(key in self.cache):
            cur = self.cache[key]
            self.cache[key] += 1
            value = self.freq[cur][key] 
            self.freq[cur].pop(key)
            if cur+1 not in self.freq:
                self.freq[cur+1] = collections.OrderedDict()
            self.freq[cur+1][key] = value
            if len(self.freq[cur]) == 0 and self.lfu == cur:
                self.lfu+=1
            return value
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            cur = self.cache[key]
            self.cache[key] += 1
            self.freq[cur].pop(key)
            if cur+1 not in self.freq:
                self.freq[cur+1] = collections.OrderedDict()
            self.freq[cur+1][key] = value
            if len(self.freq[cur]) == 0 and self.lfu == cur:
                self.lfu+=1
        else:
            if len(self.cache) >= self.cap:
                popkey = self.freq[self.lfu].popitem(last = False)
                self.cache.pop(popkey[0])

            self.cache[key] = 1
            if 1 not in self.freq:
                self.freq[1] = collections.OrderedDict()
            self.freq[1][key] = value
            self.lfu = 1