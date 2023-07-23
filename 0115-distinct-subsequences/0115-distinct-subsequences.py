class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = dict()
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j < 0:
                return 1
            if i < 0:
                return 0
            if s[i] == t[j]:
                ans = solve(i-1,j-1) + solve(i-1,j)
            else:
                ans = solve(i-1,j)
            dp[(i,j)] = ans
            return ans
        return solve(len(s)-1 , len(t) - 1)
    
        
        