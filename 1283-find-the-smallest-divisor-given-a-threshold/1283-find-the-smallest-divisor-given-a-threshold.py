class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(divisor) -> bool:
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return right
#         if(len(nums) == 1): 
#             carry = 0
#             if(nums[0] % threshold != 0):
#                 carry = 1
#             return (nums[0] // threshold + carry)
            
        
#         left = 1
#         right = sum(nums) - 1
#         ans = 0
        
#         while(left <= right):
#             mid = (left + right) // 2
#             sumi = 0
#             for i in nums:
#                 sumi += i//mid
#                 if(i%mid != 0):
#                     sumi+=1
#             if(sumi <= threshold):
#                 ans = mid
#                 right = mid - 1
                
                
#             else:
#                 left = mid + 1
                
#         return ans
                
            
        