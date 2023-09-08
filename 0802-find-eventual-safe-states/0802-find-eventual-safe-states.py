class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
            
        visited = set()
        path = set()
        safe = set()
        
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
            safe.add(course)        
            return True
        
        for i in range(len(graph)):
            if i not in visited:
                dfs(i)
        return sorted(list(safe))
        