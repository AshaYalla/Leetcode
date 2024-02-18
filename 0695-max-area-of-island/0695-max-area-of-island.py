class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        que = []
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == -1:
                    continue
                
                if grid[r][c] == 1:
                    que.append((r,c))
                    area = 0
                    
                    while(que):
                        
                        i,j = que.pop(0)
                        if grid[i][j] != -1:
                            grid[i][j] = -1
                            area+=1

                            for ni,nj in [(1,0),(0,1),(-1,0),(0,-1)]:
                                if 0<= i+ni <= len(grid)-1 and 0<= j+nj <=len(grid[0])-1 and grid[i+ni][j+nj] == 1:
                                    que.append((i+ni, j+nj))
                    res = max(res,area)
        return res
        

        
#         visited = set()
#         queue = []
#         m , n = len(grid), len(grid[0])
#         directions = [(-1,0),(1,0),(0,1),(0,-1)]
#         sum = 0
        
#         def bfs(start):
#             answer = 0
#             queue.append(start)
#             while queue:
#                 qi,qj = queue.pop(0)
#                 if((qi,qj) not in visited and grid[qi][qj] == 1 ):
#                     answer+=1
#                     visited.add(start)
#                 for ii,jj in directions:
#                     if(0<=qi+ii<m and 0<=qj+jj<n and (qi+ii,qj+jj) not in visited and grid[qi+ii][qj+jj] == 1):
#                         answer+=1
#                         queue.append((qi+ii,qj+jj))
#                         visited.add((qi+ii,qj+jj))
#             return answer
#         for i in range(m):
#             for j in range(n):
#                 if((i,j) not in visited and grid[i][j] == 1 ):
#                     sum = max(sum, bfs((i,j)))
#         return sum
    
                
        
        
        