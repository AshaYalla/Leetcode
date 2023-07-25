class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        profit = 0
        def solve(i, buy):
            if (i,buy) in dp:
                return dp[(i,buy)]
            if i == len(prices):
                return 0
            if buy:
                profit = max(- prices[i] + solve(i+1,0), solve(i+1,1))
            else:
                profit = max( prices[i] + solve(i+1,1), solve(i+1,0))
            dp[(i,buy)] = profit
            return profit
        return solve(0,1)
                
                
        