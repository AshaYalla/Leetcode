class TimeMap:

    def __init__(self):
        self.dictt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictt[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

  

        if key not in self.dictt:
            return ""
        
        elif self.dictt[key][0][0] > timestamp:
            return ""

        elif self.dictt[key][-1][0] < timestamp:
            return self.dictt[key][-1][1]
        
        l = 0
        r = len(self.dictt[key]) - 1
        
        while(l<r):
            mid = (l+r) // 2
            if self.dictt[key][mid][0] >= timestamp:
                r = mid
            else:
                l = mid +1
        if self.dictt[key][l][0] == timestamp :

            return self.dictt[key][l][1] 
        
        else:
            return self.dictt[key][l-1][1]


                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)