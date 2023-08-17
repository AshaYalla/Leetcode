class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        def solve(i):
            if dp[i] != 0:
                return dp[i]
            if i == 0:
                return 1
            if i < 0:
                return 0
            res = solve(i-1) + solve(i-2)
            dp[i] = res
            return res
        return solve(n)
        