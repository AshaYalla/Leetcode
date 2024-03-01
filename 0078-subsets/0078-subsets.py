class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         ans = []
#         def solve(i,path):
#             ans.append(path[:])
            
#             for j in range(i,n):
#                 path.append(nums[j])
#                 solve(j+1,path)
#                 path.pop()
            
#         solve(0,[])
#         return ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        
        def solve(x,path):
            if x == len(nums):
                ans.append(path[:])
                return 
            
            
            path.append(nums[x])
            solve(x+1,path)
            path.pop()
            solve(x+1,path)
            return
        solve(0,[])
        return ans
            
    

        
#         ans = []
        
#         def solve(x,path):
#             if x == len(nums):
#                 ans.append(path[:])
#                 return 
            
            
#             path.append(nums[x])
#             solve(x+1,path)
#             path.pop()
#             solve(x+1,path)
#             return
#         solve(0,[])
#         return ans
            

        
        
#         n = len(nums)
#         ans = []
#         def sub(i,summ ):
#             if(i == n):
#                 ans.append(list(summ))
#                 return
            
#             summ.append(nums[i])
#             sub(i+1,summ )
#             summ.pop()
#             sub(i+1, summ)
            
#         sub(0,[])
#         ans.sort()
#         return ans
            
        