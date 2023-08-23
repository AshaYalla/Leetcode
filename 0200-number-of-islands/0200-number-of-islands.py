class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        
        def dfs(r,c):
            grid[r][c]  = '0'
            nei = [(1,0),(0,1),(-1,0),(0,-1)]
            
            for i,j in nei:
                if r+i < rl and r+i >= 0 and c+j < cl and c+j >=0 and grid[r+i][c+j] == '1':
                    dfs(r+i,c+j)
            
        
        iland = 0
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == '1':
                    iland +=1
                    dfs(i,j)
        return iland
                    
        