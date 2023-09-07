class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]
        
        def dfs(node):
            for nei in graph[node]:
                if color[nei] ==  color[node]:
                        return False
                if color[nei] == -1:
                    color[nei] = not color[node]
                    if not dfs(nei) :
                        return False
            return True
        
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = True
                if not dfs(i):
                    return False
        return True

        
        
        
#         queue = [0]
        
#         for i in range(len(graph)):
#             if color[i] == -1:
#                 queue.append(i)
#                 color[i] = True

#                 while(queue):
#                     node = queue.pop(0)
                        
#                     for nei in graph[node]:
#                         if color[nei] ==  color[node]:
#                                 return False
#                         if color[nei] == -1:
#                             color[nei] = not color[node]
#                             queue.append(nei)
#         return True

            
