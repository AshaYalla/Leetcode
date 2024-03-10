class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        profit = 0
        def solve(i, buy, cap):
            if (i,buy) in dp:
                return dp[(i,buy)]
            if i == len(prices) or cap == 0:
                return 0
            if buy:
                profit = max(- prices[i] + solve(i+1,0,cap), solve(i+1,1,cap))
            else:
                profit = max( prices[i] + solve(i+1,1,cap -1), solve(i+1,0,cap))
            dp[(i,buy)] = profit
            return profit
        return solve(0,1,2)
    def maxProfit(self, prices: List[int]) -> int:
        empty = 0
        oneBought = oneSold = twoBought = twoSold = -float('inf')        
        for price in prices:
            prevOneBought, prevOneSold, prevTwoBought = oneBought, oneSold, twoBought
            oneBought = max(empty - price, prevOneBought)
            oneSold = max(prevOneBought + price, prevOneSold)
            twoBought = max(prevOneSold - price, prevTwoBought)
            twoSold = max(prevTwoBought + price, twoSold)
        return max(empty, oneSold, twoSold)