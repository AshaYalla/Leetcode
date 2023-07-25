class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i < 0 and j < 0:
                return True
            if j < 0 and i >= 0 : 
                return False
            if i < 0 and j >= 0:
                for k in range(j+1):
                    if p[k] != '*':
                        return False
                return True
            
            if (s[i] == p[j]) or (p[j] == '?'):
                dp[(i,j)] = solve(i-1,j-1)
                return dp[(i,j)]
            if p[j] == '*':
                dp[(i,j)] = (solve(i-1,j) or solve(i,j-1))
                return dp[(i,j)]
            else:
                return False
        return solve(len(s) -1, len(p) - 1)
    
 
            
        