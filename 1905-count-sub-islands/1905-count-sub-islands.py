class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        r = len(grid2)
        c = len(grid2[0])
        nei = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = 0       
        for i in range(r):
            for j in range(c):
                if grid2[i][j] == 1:
                    qu = [(i,j)]
                    flag = True
                    while(qu):
                        x,y = qu.pop()
                        if grid1[x][y] == 0:
                            flag = False
                        for ni,nj in nei:
                            if 0<= x+ni < r and 0 <= y+nj <c and grid2[x+ni][y+nj] == 1:
                                
                                qu.append((x+ni,y+nj))
                        grid2[x][y] = 0
                    if flag:
                        ans+=1
                    
                
        return ans
    
                                
                        
                
        