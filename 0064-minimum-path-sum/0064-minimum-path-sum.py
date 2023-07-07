class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        prev  = grid[0]
        m = len(grid)
        n = len(grid[0])
        
        for i in range(0,m):
            curr  = grid[i]
            for j in range(n):
                if i == 0 and j == 0:
                    up = 0
                    down = 0
                else:
                    up = 201
                    down = 201
                if i > 0: up = prev[j]
                if j > 0: down = curr[j-1]
                curr[j] += min(up , down)
            prev = curr
        return curr[-1]
        