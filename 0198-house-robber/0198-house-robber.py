class Solution:
    def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         @cache
#         def solve(i):
#             if i >= n:
#                 return 0
#             maxx = max(solve(i+2) + nums[i] , solve(i+1))
#             return maxx
#         return solve(0)
        
        
#         if(n == 1):
#             return nums[0]
        
#         dp = [0] * (n)
#         dp[0] = nums[0]
#         dp[1] = max(nums[1],nums[0])
#         for i in range(2,n):
#             dp[i] = max(dp[i-2] + nums[i], dp[i-1])
#         return dp[n-1]
    
        prev = nums[0]
        prev2 = 0
        
        for i in range(1,len(nums)):
            cur = prev2 + nums[i]
            ans = max(cur,prev)
            prev2 = prev
            prev = ans
            
        return prev
            
        
        
        
        
        
        # summ = 0
        # n = len(nums)
        # dictt = {}
        # def solve(i):
        #     if i >= n:
        #         return 0
        #     if i in dictt:
        #         return dictt[i]
        #     c1 = nums[i] + solve(i+2)
        #     c2 = solve(i+1)
        #     summ = max(c1,c2)
        #     dictt[i] = summ
        #     return summ
        # return solve(0)
        