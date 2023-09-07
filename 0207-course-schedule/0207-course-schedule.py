class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
            
        visited = set()
        path = set()
        
        def dfs(course):
            for nei in graph[course]:
                if nei in path:
                    return False
                    
                if nei not in visited:
                    visited.add(nei)
                    path.add(nei)
                    if not dfs(nei):
                        return False
                    path.remove(nei)
            return True
            
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
                
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         graph = {i:[] for i in range(numCourses)}
#         visited = []
#         indegree = {i:0 for i in range(numCourses)}

#         for x, y in prerequisites:
#             graph[x].append(y)
#             indegree[y]+=1
#         print(graph,indegree)
#         queue = [i for i in indegree if indegree[i] == 0]
#         if queue == []: 
#             return False
        
#         while queue:
#             temp = queue.pop(0)
#             visited.append(temp)
#             for i in graph[temp]:
#                 if i not in visited:
#                     indegree[i]-=1
#                 if indegree[i] == 0:
#                     queue.append(i)
#         print((visited))
#         if len(visited) == numCourses:
#             return True
#         else:
#             return False