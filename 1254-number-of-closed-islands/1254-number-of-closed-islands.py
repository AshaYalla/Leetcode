class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = []
        directions =[(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(grid),len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]== 0 and (i,j) not in visited):
                    boundaryflag = True
                    queue.append((i,j))
                    while(queue):
                        ti,tj = queue.pop(0)
                        visited.add((ti,tj))
                        if ti in (0,m-1) or tj in (0,n-1):
                            boundaryflag = False
                        for ni,nj in directions:
                            if(0<=ti+ni<m and 0<=tj+nj<n and grid[ti+ni][tj+nj] == 0 and (ti+ni,tj+nj) not in visited):
                                queue.append((ti+ni,tj+nj))
                                visited.add((ti+ni,tj+nj))
                    if boundaryflag:
                        answer+=1
        return answer
                        
                        
                    