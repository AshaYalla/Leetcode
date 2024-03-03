class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def solve(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if dp[x] != -1:
                return dp[x]
            
            l = solve(x+1)
            r = solve(x+2)
            dp[x] = l+r
            return l+r
            
            
        return solve(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
#         prev = 1
#         cur = 1
#         ans = 1
        
#         for i in range(2,n+1):
#             ans = prev + cur
#             prev = cur
#             cur = ans
            
#         return ans
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
        