class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
#         rl = len(grid)
#         cl = len(grid[0])
#         visited = set()
#         iland = 0
#         queue = []
#         for i in range(rl):
#             for j in range(cl):
#                 if grid[i][j] == '1' and (i,j) not in visited:
#                     iland +=1
#                     queue = [(i,j)]
#                     visited.add((i,j))
                
#                 while(queue):
#                     r,c = queue.pop()
#                     nei = [(1,0),(0,1),(-1,0),(0,-1)]
#                     for a,b in nei:
#                         if r+a < rl and r+a >= 0 and c+b < cl and c+b >=0 and grid[r+a][c+b] == '1' and (r+a,c+b) not in visited:
#                             queue.append((r+a,c+b))
#                             visited.add((r+a,c+b))
                            
#         return iland
       
        rl = len(grid)
        cl = len(grid[0])
        visited = set()
        
        def dfs(r,c):
            
            
            nei = [(1,0),(0,1),(-1,0),(0,-1)]
            
            for i,j in nei:
                if r+i < rl and r+i >= 0 and c+j < cl and c+j >=0 and grid[r+i][c+j] == '1' and (r+i,c+j) not in visited:
                    visited.add((r+i,c+j))
                    dfs(r+i,c+j)
        iland = 0
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == '1' and (i,j) not in visited:

                    visited.add((i,j))
                    iland +=1
                    dfs(i,j)
        return iland
    
                    
                    
        