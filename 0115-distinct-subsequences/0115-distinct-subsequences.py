class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp = dict()
        # def solve(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if j < 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if s[i] == t[j]:
        #         ans = solve(i-1,j-1) + solve(i-1,j)
        #     else:
        #         ans = solve(i-1,j)
        #     dp[(i,j)] = ans
        #     return ans
        # return solve(len(s)-1 , len(t) - 1)
        sl = len(s)
        tl = len(t)
        dp = [[0 for i in range(tl+1)] for j in range(sl+1)]
        
        for i in range(sl+1):
            dp[i][0] = 1
   
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
   

  