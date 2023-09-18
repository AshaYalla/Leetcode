class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i,j,dis in roads:
            graph[i].append((j,dis))
            graph[j].append((i,dis))
        
        ways = [0]*n
        dis = [float('inf')] * n
        
        queue = [(0,0)]
        dis[0] = 0
        ways[0] = 1
        
        while(queue):
            diss,node = heappop(queue)
            for nei,ndis in graph[node]:
                if diss + ndis < dis[nei]:
                    ways[nei] = ways[node]
                    dis[nei] =  diss + ndis
                    heappush(queue,(dis[nei],nei))
                    
                elif diss + ndis == dis[nei]:
                    ways[nei] +=ways[node]
        return ways[n-1] % int(10**9 + 7)

                    
                    
                
                
            
        