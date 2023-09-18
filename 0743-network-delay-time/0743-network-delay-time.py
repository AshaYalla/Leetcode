class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #dijkstra
        graph = defaultdict(list)
        for u,v, dist in times:
            graph[u].append((v,dist))
        
        dis = [float('inf')] * (n+1)
        
        dis[0] = 0
        dis[k] = 0
    
        
        queue = [(0,k)]
        
        while(queue):
            dist, node = heapq.heappop(queue)
            
            for nei,ndis in graph[node]:
                if dist + ndis < dis[nei]:
                    dis[nei] = dist+ndis
                    heapq.heappush(queue,(dis[nei], nei))
        
        for i in dis:
            if i == float('inf'):
                return -1
        return max(dis)
    
       
        
        #bellmanford
        # dist = [float('inf')]*(n+1)
        # dist[0] = 0
        # dist[k] = 0
        # for i in range(n-1):
        #     for x,y,dis in times:
        #         if dist[x]!= float('inf') and dist[x]  + dis < dist[y]:
        #             dist[y] = dist[x]  + dis 
        # for i in dist:
        #     if i == float('inf'):
        #         return -1
        # return max(dist)
    
    
      
        