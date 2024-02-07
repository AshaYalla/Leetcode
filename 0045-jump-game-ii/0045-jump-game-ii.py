class Solution:
    def jump(self, nums: List[int]) -> int:
        start , stop = 0 , 0 
        far = 0
        ans = 0
        
        for i in range(len(nums) -1 ):
            far = max(far, i+nums[i])
            
            if i == stop:
                ans+=1
                stop = far
        return ans
            
            
        