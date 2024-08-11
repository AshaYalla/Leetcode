
                
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) -1 
        
        while(l <r):
            mid = (l+ r) //2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
            
            
        
        