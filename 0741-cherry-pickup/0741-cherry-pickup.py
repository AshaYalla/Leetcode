class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = dict()
        def solve(r1,r2,c1):
            if (r1,r2,c1) in dp:
                return dp[(r1,r2,c1)] 
            c2 = r1+c1-r2
            if r1 >= m  or r2 >= m or c1 >= n or c2 >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if (r1 == m-1 and c1 == n-1 ):
                return grid[r1][c1]
            if r1 == r2:
                summ =  grid[r1][c1]
            else:
                summ = grid[r1][c1] + grid[r2][c2]
            
            a1 = solve(r1+1,r2,c1)
            a2 = solve(r1+1,r2+1,c1)
            a3 = solve(r1,r2,c1+1)
            a4 = solve(r1,r2+1,c1+1)
            summ += max(a1,a2,a3,a4)
            dp[(r1,r2,c1)] = summ
            return summ
        return max(0, solve(0,0,0))
