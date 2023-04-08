class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        r, c = len(grid)-1, len(grid[0]) -1 
        def dfs(i,j):
            if i < 0 or j < 0 or i > r or j > c:
                return 0
            if grid[i][j] == 1 or (i,j) in visited:
                return 1
            visited.add((i,j))
            return( min( dfs(i+1,j), dfs(i-1,j), dfs(i,j-1), dfs(i,j+1)))
            
        res = 0  
        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j] == 0 and (i,j) not in visited:
                    res+=dfs(i,j)
        return res
                    
                        
                    