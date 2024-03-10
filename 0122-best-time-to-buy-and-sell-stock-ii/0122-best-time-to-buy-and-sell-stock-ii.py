class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[-1 for i in range(2)] for i in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for ind in range(1, n):
            for buy in range(2):
                if buy:
                    profit = max(-prices[ind] + dp[ind-1][0], dp[ind-1][1])
                else:
                    profit = max(prices[ind] + dp[ind-1][1], dp[ind-1][0])
                dp[ind][buy] = profit

        return dp[n-1][0]
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = dict()
#         profit = 0
#         def solve(i, buy):
#             if (i,buy) in dp:
#                 return dp[(i,buy)]
#             if i == len(prices):
#                 return 0
#             if buy:
#                 profit = max(- prices[i] + solve(i+1,0), solve(i+1,1))
#             else:
#                 profit = max( prices[i] + solve(i+1,1), solve(i+1,0))
#             dp[(i,buy)] = profit
#             return profit
#         return solve(0,1)
                
                
        

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxprofit=0
#         for i in range(len(prices)-1):
#             if prices[i+1]>prices[i]:
#                 maxprofit+=prices[i+1]-prices[i]
#         return maxprofit