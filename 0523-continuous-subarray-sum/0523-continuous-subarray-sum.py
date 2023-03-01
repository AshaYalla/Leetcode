class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dictt = defaultdict(int)
        
        dictt[0] = -1
        
        summ = 0
        
        for i,j in enumerate(nums):
            summ+=j
            rem = summ % k
            
            if rem in dictt:
                if abs(dictt[rem] - i) > 1:
                    return True
            else:
                dictt[rem] = i
        return False
    
        