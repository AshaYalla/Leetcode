class Solution:
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
            
        