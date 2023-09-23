class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0]*n
        
        def findp(x):
            if x == parent[x]:
                return x
            parent[x] = findp(parent[x])
            return parent[x]
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                
                if isConnected[i][j] == 1 and i!=j:
                    pi = findp(i)
                    pj = findp(j)
                    if pi!= pj:
                        if rank[pi] == rank[pj]:
                            rank[pi]+=1
                            parent[pj] = pi
                        elif rank[pi] > rank[pj]:
                            parent[pj] = pi
                        else:
                            parent[pi] = pj
        count = 0
        for i in range(len(parent)):
            if i== parent[i]:
                count+=1
        return count
                        

                    
        
    


# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         adj = defaultdict(set)
#         for i in range(len(isConnected)):
#             for j in range(len(isConnected[0])):
#                 if isConnected[i][j] == 1 and i!=j:
#                     adj[i].add(j)
#                     adj[j].add(i)
                    
#         def dfs(node):
#             for j in adj[node]:
#                 if j not in visited:
#                     visited.add(j)
#                     dfs(j)
                    
 
#         visited = set()
#         prov = 0
        
#         for i in adj:
#             if i not in visited:
#                 visited.add(i)
#                 prov+=1
#                 dfs(i)
#         return len(isConnected) - len(visited) + prov

            
        
        
        
        
#         adj = defaultdict(set)
#         for i in range(len(isConnected)):
#             for j in range(len(isConnected[0])):
#                 if isConnected[i][j] == 1 and i!=j:
#                     adj[i].add(j)
#                     adj[j].add(i)
                    
#         queue = []    
#         visited = set()
#         prov = 0
        
#         for i in adj:
#             if i not in visited:
#                 visited.add(i)
#                 queue.append(i)
#                 prov+=1
#             while(queue):
#                 node = queue.pop()
#                 for j in adj[node]:
#                     if j not in visited:
#                         visited.add(j)
#                         queue.append(j)
                        
#         return len(isConnected) - len(visited) + prov