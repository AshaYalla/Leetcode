class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while(l<r):
            mid = (l+r) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        if nums[l] != target:
            return -1
        return l
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        left = 0
        right = len(nums) - 1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return -1
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