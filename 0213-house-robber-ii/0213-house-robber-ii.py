class Solution:
    def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         prev = nums[0]
#         prev2 = 0
        
#         for i in range(1,len(nums)-1):
#             cur = prev2 + nums[i]
#             ans = max(cur,prev)
#             prev2 = prev
#             prev = ans
            
#         max1 = prev
        
#         prev = nums[1]
#         prev2 = 0
        
#         for i in range(2,len(nums)):
#             cur = prev2 + nums[i]
#             ans = max(cur,prev)
#             prev2 = prev
#             prev = ans
            
#         max2 = prev
        
#         return max(max1,max2)
        
        
        summ = 0
        n = len(nums)
        dictt = {}
        if len(nums) == 1:
            return nums[0]
        def solve(i,n):
            if i >= n:
                return 0
            if i in dictt:
                return dictt[i]
            c1 = nums[i] + solve(i+2,n)
            c2 = solve(i+1,n)
            summ = max(c1,c2)
            dictt[i] = summ
            return summ
        first = solve(0,len(nums) -1)
        dictt = {}
        sec = solve(1, len(nums))
        return max(first, sec) 
        
        