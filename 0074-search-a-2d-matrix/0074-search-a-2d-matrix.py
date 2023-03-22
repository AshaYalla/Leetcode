class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0] ) -1
        
        while(r < len(matrix) and c >=0):
            mid = matrix[r][c]
            if target == mid:
                return True
            elif mid > target:
                c-=1
            else:
                r+=1
        return False
        