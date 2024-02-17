class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        
        while True:
            tortoise  = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise!= hare:
            tortoise  = nums[tortoise]
            hare = nums[hare]
        return hare
            
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
        return -1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         tortoise = hare = nums[0]
        
#         while True:
#             tortoise  = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break
#         tortoise = nums[0]
#         while tortoise!= hare:
#             tortoise  = nums[tortoise]
#             hare = nums[hare]
#         return hare
            

    
    
    
    
            
        