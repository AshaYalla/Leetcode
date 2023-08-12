class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        dictt = {}
        def solve(r,c):
            if (r,c) in dictt:
                return dictt[(r,c)]
            if r == 0 and c == 0:
                if obstacleGrid[r][c] == 0:
                    return 1
                else:
                    return 0
            if r < 0 or c < 0:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            dictt[(r,c)] = solve(r-1,c) + solve(r,c-1)
            return dictt[(r,c)]
        return solve(m-1,n-1)