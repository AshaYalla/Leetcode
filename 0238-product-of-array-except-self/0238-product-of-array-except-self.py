class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        print(ans)
        prev = 1
        for j in range(len(nums) - 2, -1,-1):
            print(prev)
            prev = nums[j+1] * prev
            ans[j] = ans[j] * prev
        return ans
            
            
            
        