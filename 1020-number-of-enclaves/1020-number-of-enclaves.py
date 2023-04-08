class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r,c = len(grid)-1, len(grid[0])-1
        visited = set()
        nei = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0
        con = True
        for i in range(0,r):
            for j in range(0,c):
                queue =[(i,j)]
                ans = 0
                while(queue):
                    ti, tj = queue.pop()
                    if (ti,tj) not in visited  and ti >=0 and ti <=r and tj >=0 and tj <=c  and grid[ti][tj] == 1:
                        ans+=1
                        visited.add((ti,tj))
                        queue.extend([(ti+1,tj),(ti,tj+1),(ti-1,tj),(ti,tj-1)])
                        if ti  in (0,r) or tj  in(0,c):
                            con = False
                if con:
                    res+=ans
                con = True
                            
        return res
                    
                        
        