class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left<right):
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return - 1
        return left