class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if target in nums:
                return [0,0]
            else:
                return[-1,-1]
        l,r = 0,len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                start = end = mid
                while(start-1 >= 0 and nums[start-1] == target):
                    start-=1
                while(end + 1 <= len(nums) -1 and nums[end+1] == target):
                    end+=1
                return[start,end]
            elif(nums[mid] > target):
                r = mid -1
            else:
                l = mid+1
        return [-1,-1]
    
                    
        