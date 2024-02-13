class Solution:
    def jump(self, nums: List[int]) -> int:
        maxx = nums[0]
        cur_end = 0
        ans = 0
        
        for i in range(len(nums)-1):
            if maxx < i:
                return False
            maxx = max(maxx, i+nums[i])
            
            if i == cur_end:
                ans+=1
                cur_end = maxx
                
            
            
        return ans
                    