class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visited = set()
        pathvis = set()
        res = [0]* len(graph)
        
        def dfs(i):
            
            if i in pathvis:
                return False
            if i in visited:
                return True
            visited.add(i)
            pathvis.add(i)
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            pathvis.remove(i)    
            res[i] = 1
            return True
        
        for i in range(len(graph)):
            dfs(i)
        ans = []
        print(res)
        for i in range(len(res)):
            if res[i] == 1:
                ans.append(i)
        return ans
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(graph)
#         indegree = [0] * n
        
#         for i in range(n):
#             for node in graph[i]:
#                 indegree[i]+=1
                
#         q = deque()
#         for i in range(n):
#             if indegree[i] == 0:
#                 q.append(i)
                
#         safe = []
#         print(q)
        
#         while(q):
#             node = q.popleft()
#             safe.append(node)
#             for nei in graph[node]:
#                 indegree[nei] -=1
#                 if indegree[nei] ==0:
#                     q.append(nei)
                    
#         return sorted(safe)
                    
                    
            
        
            
        
        
        
        
        
        
        
        
        
            
#         visited = set()
#         path = set()
#         safe = set()
        
#         def dfs(course):
#             for nei in graph[course]:
#                 if nei in path:
#                     return False
                    
#                 if nei not in visited:
#                     visited.add(nei)
#                     path.add(nei)
#                     if not dfs(nei):
#                         return False
#                     path.remove(nei)
#             safe.add(course)        
#             return True
        
#         for i in range(len(graph)):
#             if i not in visited:
#                 dfs(i)
#         return sorted(list(safe))
        