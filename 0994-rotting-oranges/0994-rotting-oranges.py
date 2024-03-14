class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        res = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    que.append((r,c,0))
                    
    
        while(que):

            i,j,level = que.pop(0)
            if grid[i][j] != -1:
                grid[i][j] = -1


            for ni,nj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<= i+ni <= len(grid)-1 and 0<= j+nj <=len(grid[0])-1 and grid[i+ni][j+nj] == 1:
                    que.append((i+ni, j+nj,level+1))
                    grid[i+ni][ j+nj] = -1
            res = max(res,level)
                        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return res
        