#User function Template for python3
from collections import defaultdict
class Solution:
    def shortestPath(self, n, m, edges):
        graph = defaultdict(list)
        
        for u,v,d in edges:
            graph[u].append((v,d))
            graph[v].append((u,d))
            
        distance = [float('inf')]* (n+1)
        parent = [0] * (n+1)
        
        parent[1] = 1
        distance[1] = 0
        
        sett = {(0,1)}

        while(sett):
            dis,node = sett.pop()
            for k in graph[node]:
                nei = k[0]
                ndis = k[1]
                

                if dis+ndis < distance[nei]:
                    if (distance[nei], nei) in sett:
                        sett.remove((distance[nei], nei))
                    distance[nei] = dis+ndis
                    parent[nei] = node
                    sett.add((distance[nei], nei))
                    

        ans = []
        node = n

        if distance[n] == float('inf'):
            return [-1]
                    
        while(parent[node] != node):
            ans.append(node)
            
            node = parent[node]
            
        ans.append(1)
            

        return ans[::-1]
        
        
        
                    
                
            
        
        
        


            
            
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        edges = []
        for i in range(m):
            node1, node2, weight = list(map(int, input().split()))
            edges.append([node1, node2, weight])
        obj = Solution()
        ans = obj.shortestPath(n, m, edges)
        for e in ans:
            print(e, end = ' ')
        print()
# } Driver Code Ends