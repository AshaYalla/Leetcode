class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for i in range(len(graph))]
        queue = [0]
        
        for i in range(len(graph)):
            if color[i] == -1:
                queue.append(i)
                color[i] = True

                while(queue):
                    node = queue.pop(0)
                        
                    for nei in graph[node]:
                        if color[nei] ==  color[node]:
                                return False
                        if color[nei] == -1:
                            color[nei] = not color[node]
                            queue.append(nei)
        return True

            
