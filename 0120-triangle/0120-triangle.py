class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        a = len(triangle)
        b = len(triangle)
        dp = dict()
        def solve(i,j):
            if  i == 0:
                return triangle[0][0]
            if (i,j) in dp:
                return dp[(i,j)]
            if j > i or j < 0:
                return inf
            dp[(i,j)] = triangle[i][j] + min(solve(i-1,j), solve(i-1,j-1))
            return dp[(i,j)]
        
        minn = inf
        
        for j in range(b):
            minn = min(minn, solve(a-1,j))
        return minn
            
            
            
            
            
            # if i == m:
            #     return min(triangle[i][j], triangle[i][j+1] if j < n -1 else 0)
            # if j > i+1:
            #     return 0
            # triangle
            
            