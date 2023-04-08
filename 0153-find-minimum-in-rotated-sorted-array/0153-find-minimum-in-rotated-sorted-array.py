
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=len(nums)-1
        while start<=end:
            if nums[start] <= nums[end]:
                return nums[start]
            mid=start+(end-start)//2
            nextt=(mid+1)%n
            prevv=(mid+n-1)%n
            if nums[mid]<=nums[nextt] and nums[mid]<=nums[prevv]:
                return nums[mid]
            elif nums[mid] >= nums[start]:
                start=mid+1
            else:
                end=mid-1 