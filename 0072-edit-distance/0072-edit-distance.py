class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j < 0:
                return i + 1
            if i < 0:
                return j + 1
            if word1[i] != word2[j]:
                ans = min(1+ solve(i-1,j), 1+ solve(i,j-1), 1 + solve(i-1,j-1))
            else:
                ans =  solve(i-1,j-1)
            dp[(i,j)] = ans
            return ans
        return solve(len(word1)-1, len(word2) -1 )
                
            
        