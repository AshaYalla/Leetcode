class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        summ = 0
        maxx = 0
        
        for i,j in enumerate(nums):
            summ+= j
            maxx = max(maxx,math.ceil(summ/(i+1)))
        return maxx
            
        