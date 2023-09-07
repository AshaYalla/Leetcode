class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        ipattern = []
        queue = collections.deque()
        ans = 0
        r = len(grid)
        c = len(grid[0])
        nei = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    island = []
                    while(queue):
                        x,y = queue.popleft()
                        for mx,my in nei:
                            if x+mx >=0 and y+my >= 0 and x+mx < r and y+my < c and grid[x+mx][y+my] == 1 and (x+mx,y+my) not in visited:
                                island.append((mx+x-i,my+y-j))
                                queue.append((x+mx,y+my))
                                visited.add((x+mx,y+my))
                    print(island)
                               
                    if island not in ipattern:
                        ipattern.append(island)
                        ans+=1
        return ans
                                
                                
                        
                        
                    
    
        