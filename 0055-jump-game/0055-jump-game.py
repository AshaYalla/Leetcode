class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]
        
        for i in range(len(nums)):
            if maxx < i:
                return False
            maxx = max(maxx, i+nums[i])
            
        return True
            