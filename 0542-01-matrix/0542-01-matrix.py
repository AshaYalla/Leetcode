class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        queue = []
        seen = set()
        nei = [(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    seen.add((i,j))
        while(queue):
            r,c,dis = queue.pop(0)
            for nr,nc in nei:
                if r+nr >=0 and r+nr < m and c+nc >=0 and c+nc < n and (r+nr, c+nc) not in seen:
                    seen.add((r+nr, c+nc))
                    queue.append((r+nr,c+nc,dis+1))
                    mat[r+nr][c+nc] = dis+1
        return mat
                
            
                
                
        