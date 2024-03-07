class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
            
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]

        
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                    continue
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                
        return dp[-1][-1]
        
        
        
        dictt = {}
        def solve(r,c):
            if (r,c) in dictt:
                return dictt[(r,c)]
            if r == 0 and c == 0:
                if obstacleGrid[r][c] == 0:
                    return 1
                else:
                    return 0
            if r < 0 or c < 0:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            dictt[(r,c)] = solve(r-1,c) + solve(r,c-1)
            return dictt[(r,c)]
        return solve(m-1,n-1)
    