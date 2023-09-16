class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        
        for i,j,price in flights:
            graph[i].append((j,price))
            
        queue = [(0,src,0)]  
            
        stops = [float('inf') for i in range(n)]
        
        while(queue):
            fprice,node,num = heapq.heappop(queue)
            if num > stops[node] or num > k+1:
                continue;
            stops[node] = num
            if node== dst:
                return fprice
            for nei, nprice in graph[node]:
                heapq.heappush(queue,(fprice + nprice,nei,num+1))
        return -1