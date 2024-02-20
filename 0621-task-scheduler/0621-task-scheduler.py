
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0 
        t = Counter(tasks)
        heap = [-i for i in t.values()]
        heapq.heapify(heap)
        q = []
        
        while(heap or q):
            time+=1
            if heap:
                count = heapq.heappop(heap)
                count+=1
                if count:
                    q.append((count, time+n))
            if q and q[0][1] == time:
                ncount = q.pop(0)[0]
                heapq.heappush(heap, ncount)
        return time
                    
                    
                
        
            
            