class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                ans = 1 + solve(i-1,j-1)
            else:
                ans = max(solve(i,j-1), solve(i-1,j))
            dp[(i,j)] = ans
            return ans
        return solve(len(text1)-1,len(text2)-1)
                
        
        
        