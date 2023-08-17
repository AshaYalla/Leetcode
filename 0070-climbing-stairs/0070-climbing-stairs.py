class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        cur = 1
        ans = 1
        
        for i in range(2,n+1):
            ans = prev + cur
            prev = cur
            cur = ans
            
        return ans
#         dp = [0]*(n+1)
#         dp[0] = dp[1] = 1
        
#         for i in range(2,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[n]



        
        
        # def solve(i):
        #     if dp[i] != 0:
        #         return dp[i]
        #     if i == 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     res = solve(i-1) + solve(i-2)
        #     dp[i] = res
        #     return res
        # return solve(n)
        