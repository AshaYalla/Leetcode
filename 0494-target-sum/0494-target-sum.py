# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)

                
#         dp = [[0 for i in range(target+1)] for j in range(n+1)]
        
#         for i in range(n+1):
#             dp[i][0] = 1
        
#         for i in range(1,n+1):
#             for j in range(0,target+1):
#                 if j < nums[i-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
#         return dp[-1][-1]
        
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        dp = [[0] * (2 * total + 1) for _ in range(len(nums))]
        dp[0][nums[0] + total] = 1
        dp[0][-nums[0] + total] += 1
        
        for i in range(1, len(nums)):
            for summ in range(-total, total + 1):
                if dp[i - 1][summ + total] > 0:
                    dp[i][summ + nums[i] + total] += dp[i - 1][summ + total]
                    dp[i][summ - nums[i] + total] += dp[i - 1][summ + total]
        
        return 0 if abs(S) > total else dp[len(nums) - 1][S + total]
        
        
        
        
#         def solve(i,summ):
            
#             if i == len(nums):
#                 if summ == target:
#                     return 1
#                 else:
#                     return 0
            
            
#             neg = solve(i+1,summ -nums[i])
#             pos = solve(i+1, summ + nums[i])
            
#             return neg + pos
            
            
#         return solve(0, 0)
            
        
        
        
        
        
        
        

#         nums.sort()
#         n = len(nums)

#         dp = dict()
#         mod=10**9+7

        #recursion
#         def recursion(i,k):
#             if i == n:
#                 if k == 0:
#                     return 1
#                 else:
#                     return 0
#             if (i,k) in dp:
#                 return dp[(i,k)]

#             summ =  recursion(i+1,k + nums[i]) + recursion(i+1,k-nums[i])
#             dp[(i,k)] = summ 
#             return summ
#         return recursion(0,target) %mod
        
        #tabulation
    
#         dp = [[0 for i in range(target+1)] for j in range(n+1)]
        
#         for i in range(n+1):
#             dp[i][0] = 1
        
#         for i in range(1,n+1):
#             for j in range(0,target+1):
#                 if j < nums[i-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
#         return dp[-1][-1]
        
#         #tabulation Optimized
        
#         prev = [0 for i in range(sum+1)] 
        
#         for i in range(n+1):
#             prev[0] = 1
        
#         for i in range(1,n+1):
#             curr = [0 for i in range(sum+1)] 
#             for j in range(0,sum+1):
#                 if j < arr[i-1]:
#                     curr[j] = prev[j]
#                 else:
#                     curr[j] = prev[j] + prev[j-arr[i-1]]
#             prev = curr
#         return prev[-1]%1000000007
    

        