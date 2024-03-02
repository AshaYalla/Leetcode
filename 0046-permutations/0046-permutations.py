class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(path, nums):
            if not nums:
                ans.append(path)
                return
            for i in nums:
                solve(path+nums[i], nums[:i]+ nums[i+1:])
            
        solve([], nums)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         ans = []
#         check = [True]*len(nums)
#         def solve(i,path,check):
#             if i == n:
#                 ans.append(path[:])
#                 return
#             for j in range(len(nums)):
#                 if check[j] == True:
#                     check[j] = False
#                     path.append(nums[j])
#                     solve(i+1,path,check)
#                     path.pop()
#                     check[j] = True
#         solve(0,[],check)
#         return ans
    
    
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def solve(i,path):
            if i == n:
                ans.append(path[:])
                return
            for j in nums:
                if j not in path:
                    path.append(j)
                    solve(i+1,path)
                    path.pop()
        solve(0,[])
        return ans
    
    
    
    # class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     def solve(ind,target):
    #         if target==0:
    #             ans.append(op[:])
    #             return 
    #         for i in range(ind,len(candidates)):
    #             if i>ind and candidates[i]==candidates[i-1]:
    #                 continue
    #             if candidates[i]>target:
    #                 break
    #             op.append(candidates[i])
    #             solve(i+1,target-candidates[i])
    #             op.pop()
    #     candidates.sort()
    #     ans=[]
    #     op=[]
    #     solve(0,target)
    #     return ans