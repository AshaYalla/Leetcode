class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        dp = dict()
        mod=10**9+7

        #recursion
        def recursion(i,k):
            if i == n:
                if k == 0:
                    return 1
                else:
                    return 0
            if (i,k) in dp:
                return dp[(i,k)]

            summ =  recursion(i+1,k + nums[i]) + recursion(i+1,k-nums[i])
            dp[(i,k)] = summ 
            return summ
        return recursion(0,target) %mod
        
#         #tabulation
    
#         dp = [[0 for i in range(sum+1)] for j in range(n+1)]
        
#         for i in range(n+1):
#             dp[i][0] = 1
        
#         for i in range(1,n+1):
#             for j in range(0,sum+1):
#                 if j < arr[i-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
#         return dp[-1][-1]%1000000007
        
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
    

        