class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                if nums[low] <= target and nums[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid

        if nums[low] == target:
            return low
        else:
            return -1