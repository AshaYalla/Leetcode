class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = - float('inf')
        cursum = 0
        for i in nums:
            cursum+=i
            if cursum > maxx:
                maxx = cursum
            if cursum <= 0:
                cursum = 0
        return maxx
            
        