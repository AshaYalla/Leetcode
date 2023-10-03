class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dictt = Counter(nums)
        ans = 0
        for i, x in dictt.items():
            if x >=2:
                ans+= (x-1) * (x) // 2
        return ans
            
            
            

        