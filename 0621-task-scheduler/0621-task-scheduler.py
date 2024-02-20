
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
#         https://leetcode.com/problems/task-scheduler/discuss/2781024/easy-python-method-with-explanation

        if n == 0: return len(tasks)
        counter = collections.Counter(tasks)
        maxCount = 0
        maxValue = max(counter.values())
        for cha, val in counter.items():
            if val == maxValue:
                maxCount += 1
        return max((n + 1) * (maxValue - 1) + maxCount ,len(tasks))
    
    
    
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
                    
                    
                
        
            
            