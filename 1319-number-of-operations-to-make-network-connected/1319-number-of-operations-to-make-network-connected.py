class Solution:

#     def dfs(self, node, adj, visit):
#         visit[node] = True
#         for neighbor in adj[node]:
#             if not visit[neighbor]:
#                 self.dfs(neighbor, adj, visit)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

#         adj = [[] for _ in range(n)]
#         for connection in connections:
#             adj[connection[0]].append(connection[1])
#             adj[connection[1]].append(connection[0])

#         number_of_connected_components = 0
#         visit = [False for _ in range(n)]
#         for i in range(n):
#             if not visit[i]:
#                 number_of_connected_components += 1
#                 self.dfs(i, adj, visit)

#         return number_of_connected_components - 1
        
        
        
        redundency = 0
        parent = [i for i in range(n)]
        def findp(x):
            if x!= parent[x]:
                parent[x] = findp(parent[x])
            return parent[x]
        
        for i,j in connections:
            pi = findp(i) 
            pj = findp(j)
            parent[pj] = pi
        
        count = 0
                
        for i in range(len(parent)) :
            if i == parent[i]:
                count+=1

        
        return count -1
                
                
                
        
        