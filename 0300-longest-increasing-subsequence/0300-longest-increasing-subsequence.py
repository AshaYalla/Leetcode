class Solution:
    
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binarySearch(key,ans):
            left=0
            right=len(ans)
            while left<right:
                mid=(left+right)>>1
                if ans[mid]<key:
                    left=mid+1
                else:
                    right=mid
            return left
        
        n=len(nums)
        ans=[nums[0]]
        c=1
        for i in range(1,n):
            if nums[i]>ans[-1]:
                ans.append(nums[i])
                c+=1
            else:
                ind=binarySearch(nums[i],ans)
                ans[ind]=nums[i]
        return c
        
        
        
#         dp = [1 for i in range(len(nums))]
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], 1 + dp[j])
#         return max(dp)
                    
                    
#         dp = {}
#         def solve(i, prev):
#             if (i,prev) in dp:
#                 return dp[(i,prev)]
#             if i == len(nums):
#                 return 0
#             if  nums[i] > prev:
#                 dp[(i,prev)] = max(solve(i+1,prev), 1 +  solve(i+1,nums[i]))
#                 return dp[(i,prev)]
#             else:
#                 dp[(i,prev)] = solve(i+1,prev)
#                 return dp[(i,prev)]
#             dp[(i,prev)]
#         return solve(0,float('-inf'))
        
           
                    
                    
                
                
    

                
                
        