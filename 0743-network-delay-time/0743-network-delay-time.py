class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')]*(n+1)
        dist[0] = 0
        dist[k] = 0
        for i in range(n-1):
            for x,y,dis in times:
                if dist[x]!= float('inf') and dist[x]  + dis < dist[y]:
                    dist[y] = dist[x]  + dis 
        for i in dist:
            if i == float('inf'):
                return -1
        return max(dist)
    
    
      
        