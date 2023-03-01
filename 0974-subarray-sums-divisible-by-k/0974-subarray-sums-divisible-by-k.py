class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        dictt = defaultdict(int)
        dictt[0] = 1
        
        summ = 0
        res = 0
        
        for i in nums:
            summ+=i
            rem = summ % k
            
            res+=dictt[rem]
            dictt[rem]+=1
        return res
        