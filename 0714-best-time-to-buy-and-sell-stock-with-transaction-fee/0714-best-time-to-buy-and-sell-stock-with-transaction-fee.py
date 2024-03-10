class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        dp = dict()
        profit = 0
        def solve(i, buy):
            if (i,buy) in dp:
                return dp[(i,buy)]
            if i >= len(prices):
                return 0
            if buy:
                dp[(i,buy)] = max(- prices[i] + solve(i+1,0), solve(i+1,1))
            else:
                dp[(i,buy)] = max( prices[i] - fee + solve(i+1,1), solve(i+1,0))
            return dp[(i,buy)]
        return solve(0,1)
        