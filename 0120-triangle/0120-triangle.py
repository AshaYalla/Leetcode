class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0] = triangle[0]
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
                else:
                    upper_left = triangle[i][j] + dp[i - 1][j - 1]
                    upper_right = triangle[i][j] + dp[i - 1][j]
                    dp[i][j] = min(upper_left, upper_right)

        return min(dp[n - 1])
        
        
        
        
        # dp = [[0 for i in range(j)] for j in range(1,len(triangle)+1)]

        
#         def dfs(i, j):
#             if i == len(triangle):
#                 return 0
#             if dp[i][j] != 0:
#                 return dp[i][j]

#             lower_left = triangle[i][j] + dfs(i + 1, j)
#             lower_right = triangle[i][j] + dfs(i + 1, j + 1)
#             dp[i][j]  = min(lower_left, lower_right)

#             return dp[i][j] 

#         return dfs(0, 0)
            
    