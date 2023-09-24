class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        if m*n == 1:
            return 1
        
        parent = [i for i in range(m*n)]
        size = [ 1 for i in range(m*n)]
        def find(x):
            if x!=parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        maxx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x,y in nei:
                        if x+i >=0 and x+i < m and y+j >=0 and y+j < n and grid[x+i][y+j] == 1:
                            par = find(i*n+j)
                            npar = find((x+i)*n +(y+j))
                            
                            if par == npar:
                                continue
                            if size[par] > size[npar]:
                                parent[npar] = par
                                size[par]+=size[npar]
                                maxx = max(size[par], maxx)
                            else:
                                parent[par] = npar
                                size[npar]+=size[par]
                                maxx = max(size[npar], maxx)
      
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    sett = set()
                    iland = 0
                    for x,y in nei:
                        if x+i >=0 and x+i < m and y+j >=0 and y+j < n and grid[x+i][y+j] == 1:
                            par = find(i*n+j)
                            npar = find((x+i)*n +(y+j))
                            sett.add(npar)
                    for k in sett:
                        iland +=size[k]
                    maxx = max(maxx,iland+1)
                            

        return maxx
                    
                                
                                
                                
                    
        