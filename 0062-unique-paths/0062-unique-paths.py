class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #tabulation space optimization
        prev  = [0 for j in range(n)]
        
        for i in range(m):
            curr  = [0 for j in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up = prev[j]
                    down = curr[j-1]
                    curr[j] = up + down
            prev = curr
        return curr[-1]
        
        #tabulation
        # dp  = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             dp[i][j] = 1
        #         else:
        #             up = dp[i-1][j]
        #             down = dp[i][j-1]
        #             dp[i][j] = up + down
        # return dp[m-1][n-1]
        
        #recursion
        # def solve(r,c):
        #     if r == 0 and c == 0:
        #         return 1
        #     if r < 0 or c < 0:
        #         return 0
        #     return solve(r-1,c) + solve(r,c-1)
        # return solve(m-1,n-1)
                