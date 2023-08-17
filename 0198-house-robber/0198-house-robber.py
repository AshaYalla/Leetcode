class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def solve(i):
            if i >= n:
                return 0
            maxx = max(solve(i+2) + nums[i] , solve(i+1))
            return maxx
        return solve(0)
        