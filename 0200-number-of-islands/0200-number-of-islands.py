class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        nei = [(-1,0),(1,0),(0,-1),(0,1),]
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1" and (i,j) not in visited:
                    ans+=1
                    queue = [(i,j)]
                    visited.add((i,j))
                    while(queue):
                        a,b =  queue.pop()
                        
                        for l,m in nei:
                            if (a+l >=0 and a+l <len(grid)) and (b+m >=0 and b+m <len(grid[0])) :
                                if (grid[a+l][b+m] == "1" ) and (a+l,b+m) not in visited:
                                    queue.append((a+l,b+m))    
                                    visited.add((a+l,b+m))
                                
        return ans

        