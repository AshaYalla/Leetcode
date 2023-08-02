class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
                    
                    
#         dp = {}
#         def solve(i, prev):
#             if (i,prev) in dp:
#                 return dp[(i,prev)]
#             if i == len(nums):
#                 return 0
#             if  nums[i] > prev:
#                 dp[(i,prev)] = max(solve(i+1,prev), 1 +  solve(i+1,nums[i]))
#                 return dp[(i,prev)]
#             else:
#                 dp[(i,prev)] = solve(i+1,prev)
#                 return dp[(i,prev)]
#             dp[(i,prev)]
#         return solve(0,float('-inf'))
        
           
                    
                    
                
                
    

                
                
        