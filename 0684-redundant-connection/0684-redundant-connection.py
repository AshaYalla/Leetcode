class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * len(parent)
        
        
        def findparent(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(i,j):
            pi = findparent(i)
            pj = findparent(j)
            
            if pi == pj:
                return False
            
            if rank[pi] > rank[pj]:
                parent[pi] = pj
                rank[pj]+= rank[pi]
            else:
                parent[pj] = pi
                rank[pi]+= rank[pj]
            return True
                
        for i,j in edges:
            if not union(i,j):
                return [i,j]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         adj = defaultdict(list)
#         for i in edges:
#             adj[i[0]].append(i[1])
#             adj[i[1]].append(i[0])
            
#         visited = set()
#         visited.add(1)
        
#         def dfs(node,parent):
#             for i in adj[node]:
#                 if i in visited and i!=parent:
#                     return [node,i]
#                 if i not in visited:
#                     visited.add(i)
#                     dfs(i,node)
                    
#         return dfs(1,-1)
        
        
    

      