class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        seen = set()
        seen.add(0)
            
        def dfs(node):
            summ = 0
            childapple = 0
            for c in graph[node]:
                if c not in seen:
                    seen.add(c)
                    childapple += dfs(c)
            if(childapple):
                summ = childapple + 1
                    
            if summ == 0 and hasApple[node] == True:
                
                return 1
                    
            return summ
        bleh = dfs(0)
        if bleh == 0:
            return 0
        return (bleh - 1) * 2
        
                    