class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(grid,i):
            if i > n+1:
                return
            
            if len(grid) == k:
                ans.append(grid[:])
                return
            grid.append(i)
            solve(grid,i+1)
            grid.pop()
            solve(grid,i+1)
        solve([],1)
        return ans
        