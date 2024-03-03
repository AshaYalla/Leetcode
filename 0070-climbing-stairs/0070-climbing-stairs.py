class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        first_prev = 2
        sec_prev = 1
        ans = 3
        
        for i in range(3, n+1):
            ans = sec_prev + first_prev
            sec_prev = first_prev
            first_prev = ans
            
        return ans
    

        for i in range(2,n+1):
            ans = prev + cur
            prev = cur
            cur = ans
            
        return ans
        
        
        
        
        
#         dp = [-1] * n
#         def solve(x):
#             if x == n:
#                 return 1
#             if x > n:
#                 return 0
#             if dp[x] != -1:
#                 return dp[x]
            
#             l = solve(x+1)
#             r = solve(x+2)
#             dp[x] = l+r
#             return l+r
            
            
#         return solve(0)
        

        
        
        
        
        
        
        
        
        
        
        




