class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in edges:
            adj[i[0]].append(i[1]) 

        def dfs(v):
            if v in path:
                return float("inf")
            if v in visited:
                return 0
            visited.add(v)
            path.add(v)
            cindex = ord(colors[v]) - ord('a')
            count[v][cindex] = 1
            
            for nei in adj[v]:
                if dfs(nei) == float("inf"):
                    return float("inf")
                for c in range(26):
                    count[v][c] = max(count[v][c], count[nei][c] + ( 1 if c == cindex else 0))

            path.remove(v)
            return max(count[v])

        
        n = len(colors)
        res = 0
        visited, path = set(), set()
        count = [[0] * 26 for i in range(n)]
        for i in range(n):
            res = max(res,dfs(i))
        if res == float("inf"):
            return -1
        else:
            return res