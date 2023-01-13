class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi =  mx  = mn = nums[0]
        for i in range(1,len(nums)):
            if(nums[i] == 0):
                mx = mn = 1
            mx , mn = max(mx*nums[i], nums[i], mn*nums[i]),min(mx*nums[i], nums[i], mn*nums[i])
            
            maxi = max(maxi,mx)
        return maxi