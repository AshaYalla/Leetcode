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


    def maxProfit(self, k, prices):
        
        dp = [[[-1 for _ in range(k + 1)] for _ in range(3)] for _ in range(len(prices) + 1)]
        
        def recursion_with_memoization(ind, can_buy, k):
            if ind >= len(prices) or k <= 0:
                return 0

            if dp[ind][can_buy][k] != -1:
                return dp[ind][can_buy][k]

            if can_buy:
                dp[ind][can_buy][k] = max(-prices[ind] + recursion_with_memoization(ind + 1, not can_buy, k), recursion_with_memoization(ind + 1, can_buy, k, ))
            else:
                dp[ind][can_buy][k] = max(prices[ind] + recursion_with_memoization(ind + 1, not can_buy, k - 1), recursion_with_memoization( ind + 1, can_buy, k))

            return dp[ind][can_buy][k]
        
        return recursion_with_memoization(0, True, k)

    

