class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text1)+1)] for j in range(len(text2)+1)]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
                    
        
        
        
        
        
        
        # dp = dict()
        # def solve(i,j):
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if i < 0 or j < 0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         ans = 1 + solve(i-1,j-1)
        #     else:
        #         ans = max(solve(i,j-1), solve(i-1,j))
        #     dp[(i,j)] = ans
        #     return ans
        # return solve(len(text1)-1,len(text2)-1)
                
        
        
        