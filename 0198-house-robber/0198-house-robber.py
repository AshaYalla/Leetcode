class Solution:
    def rob(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        dictt = {}
        def solve(i):
            if i >= n:
                return 0
            if i in dictt:
                return dictt[i]
            c1 = nums[i] + solve(i+2)
            c2 = solve(i+1)
            summ = max(c1,c2)
            dictt[i] = summ
            return summ
        return solve(0)
        
            
            