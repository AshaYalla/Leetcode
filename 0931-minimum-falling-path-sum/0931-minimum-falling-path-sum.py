class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = c = len(matrix)
        
        dp = [[ 0 for i in range(r)] for j in range(c)]
        
        dp[0] = matrix[0]
        
        for i in range(1,r):
            for j in range(c):
                
                if j-1 >= 0:
                    first = dp[i-1][j-1]
                else:
                    first = inf
                if j+1 < r:
                    last = dp[i-1][j+1]
                else:
                    last = inf
                
                dp[i][j] = matrix[i][j] + min(dp[i-1][j], first, last)
        print(dp)
        return min(dp[-1])
        
        
        
        
        
        
        
#         def solve(x,y):
#             if x == r:
#                 return 0
#             if y <0 or y >r-1:
#                 #there's no such box exisiting, so ill return infinity instead of 0
#                 #so the min value is of remaining existing boxes

#                 return inf
#             if (x,y) in dp:
#                 return dp[(x,y)]
#             first = solve(x+1,y-1)
#             sec =  solve(x+1,y)
#             third = solve(x+1,y+1)
            
#             dp[(x,y)] = matrix[x][y] + min(first,sec,third)
#             return dp[(x,y)]
        
#         minn = inf

#         #iterate through all the elements in the first row
#         for i in range(r):
#             dp = defaultdict()
#             minn = min(minn, solve(0,i))
#         return minn