class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        
        for i in range(n):
            for j in range(amount+1):
                if j < coins[i]:
                    continue
                else:
                    dp[j] = dp[j-coins[i]] + dp[j]
        return dp[-1]
        
        
                
                
                
                
                
                
                
#         dp = {}
#         def solve(i,rem):
#             if (i,rem) in dp:
#                 return dp[(i,rem)]
#             if rem < 0:
#                 return 0
#             if rem == 0:
#                 return 1
#             if i < 0:
#                 if rem == 0:
#                     return 1
#                 else:
#                     return 0
            
#             ans = solve(i,rem-coins[i]) + solve(i-1,rem)
#             dp[(i,rem)] = ans
#             return ans
#         return solve(n-1,amount)
        