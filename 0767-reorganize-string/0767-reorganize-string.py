class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        prev = None
        maxheap = [[-j,i] for i,j in count.items()]
        heapq.heapify(maxheap)
        res = ""
        
        while(maxheap or prev):
            if(prev and not maxheap):
                return ""
            a,b = heapq.heappop(maxheap)
            res+=b
            a+=1
            if(prev):
                heapq.heappush(maxheap,prev)
                prev = None
            if a!=0:
                prev = [a,b]
        return res
            
        