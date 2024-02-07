class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxx = nums[0]
        
        if nums[0] == 0 and len(nums) == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        
        for i in nums[1:]:
            maxx -=1
            if maxx < 0:
                return False
            
            if i > maxx:
                maxx = i
            
        return True
            
        