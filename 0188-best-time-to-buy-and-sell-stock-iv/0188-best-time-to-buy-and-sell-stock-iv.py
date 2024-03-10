# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
#         dp = [[[-1 for _ in range(k + 1)] for _ in range(3)] for _ in range(len(prices) + 1)]
#         def solve(i, buy, cap):
#             if i >= len(prices) or cap <= 0:
#                 return 0
#             if dp[i][buy][k] != -1:
#                 return dp[i][buy][k]

#             if buy:
#                 dp[i][buy][k] = max(- prices[i] + solve(i+1,0,cap), solve(i+1,1,cap))
#             else:
#                 dp[i][buy][k] = max( prices[i] + solve(i+1,1,cap -1), solve(i+1,0,cap))
            
#             return dp[i][buy][k]
#         return solve(0,1,k)
    
class Solution:
    def recursion_with_memoization(self, p, ind, can_buy, k, dp):
        if ind >= len(p) or k <= 0:
            return 0

        if dp[ind][can_buy][k] != -1:
            return dp[ind][can_buy][k]

        if can_buy:
            dp[ind][can_buy][k] = max(-p[ind] + self.recursion_with_memoization(p, ind + 1, not can_buy, k, dp), self.recursion_with_memoization(p, ind + 1, can_buy, k, dp))
        else:
            dp[ind][can_buy][k] = max(p[ind] + self.recursion_with_memoization(p, ind + 1, not can_buy, k - 1, dp), self.recursion_with_memoization(p, ind + 1, can_buy, k, dp))

        return dp[ind][can_buy][k]

    def maxProfit(self, k, prices):
        dp = [[[-1 for _ in range(k + 1)] for _ in range(3)] for _ in range(len(prices) + 1)]
        return self.recursion_with_memoization(prices, 0, True, k, dp)

    

