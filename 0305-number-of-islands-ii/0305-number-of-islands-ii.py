class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        matrix = [[0 for i in range(n)]for j in range(m)]
        def find(x):
            if x!= parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
    
        
        rank = [0]*(m*n)
        parent = [i for i in range(m*n)]
        
        nei = [[1,0],[0,1],[-1,0],[0,-1]]
        res = []
        ans = 0
        
        for i,j in positions:
            if matrix[i][j] == 1:
                res.append(res[-1])
                continue
            matrix[i][j] = 1
            point = (i) * n +j
            
            
            sparents = []
            
        
            for x,y in nei:
                par = find(point)
                if x+i >= 0 and x+i < m and y+j >= 0 and y+j < n and matrix[x+i][y+j] == 1:
                    npoint = (x+i) * n + y+j
                    npar = find(npoint)
                    sparents.append(npar)
                    if par == npar:
                        continue
                    if rank[par] > rank[npar]:
                        parent[npar] = par
                        
                    elif rank[npar] > rank[par]:
                        parent[par] = npar
                    else:
                        parent[par] = npar
                        rank[npar] +=1
   
          
            if len(sparents) == 0:
                ans+=1
            else:

                ans = ans - len(set(sparents)) + 1
                
            res.append(ans)
        return res
                    