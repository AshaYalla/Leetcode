class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i) 
        color = {}
        def dfs(node,c):
            color[node] = c
            for k in graph[node]:
                if k in color:
                    if(color[k] == c):
                        return False
                else:
                    if not dfs(k, 1-c):
                        return False
            return True
        for node in range(1,n+1):
            if node not in color:
                if not dfs(node,1):
                    return False
        return True

