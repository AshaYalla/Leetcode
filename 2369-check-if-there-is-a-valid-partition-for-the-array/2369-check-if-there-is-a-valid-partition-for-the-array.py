class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [-1] * len(nums)
        def solve(i):
 
            if i == len(nums):
                return True
            if dp[i] !=-1:
                return dp[i]
            
            ans = False
            if i+1 < len(nums)  and nums[i] == nums[i+1]:
                ans = ans or solve(i+2)
            if i+2 < len(nums) and nums[i] == nums[i+1] == nums[i+2]:
                ans = ans or solve(i+3)
                
            if i+2 < len(nums) and nums[i] == nums[i+1]-1 == nums[i+2]-2:
                ans = ans or solve(i+3)
            dp[i] = ans
            return ans
        return solve(0)
                
                
                
    