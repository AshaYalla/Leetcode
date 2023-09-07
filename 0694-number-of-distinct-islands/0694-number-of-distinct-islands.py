class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rl = len(grid)
        cl = len(grid[0])
        visited = set()
        pattern = []
        
        def dfs(r,c):
            nei = [(1,0),(0,1),(-1,0),(0,-1)]
            for i,j in nei:
                if r+i < rl and r+i >= 0 and c+j < cl and c+j >=0 and grid[r+i][c+j] == 1 and (r+i,c+j) not in visited:
                    visited.add((r+i,c+j))
                    island.append(dfs(r+i,c+j))
            return (r-x,c-y)       
             
        
        ans = 0
        
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1 and (i,j) not in visited:

                    visited.add((i,j))
                    island = []
                    x,y = i,j
                    dfs(i,j)

                    if island not in pattern:
                        pattern.append(island)
                        ans +=1
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         visited = set()
#         ipattern = []
#         queue = collections.deque()
#         ans = 0
#         r = len(grid)
#         c = len(grid[0])
#         nei = [(0,1),(1,0),(-1,0),(0,-1)]
#         for i in range(r):
#             for j in range(c):
#                 if grid[i][j] == 1 and (i,j) not in visited:
#                     queue.append((i,j))
#                     visited.add((i,j))
#                     island = []
#                     while(queue):
#                         x,y = queue.popleft()
#                         for mx,my in nei:
#                             if x+mx >=0 and y+my >= 0 and x+mx < r and y+my < c and grid[x+mx][y+my] == 1 and (x+mx,y+my) not in visited:
#                                 island.append((mx+x-i,my+y-j))
#                                 queue.append((x+mx,y+my))
#                                 visited.add((x+mx,y+my))
#                     print(island)
                               
#                     if island not in ipattern:
#                         ipattern.append(island)
#                         ans+=1
#         return ans
                                
                                
                        
                        
                    
    
        