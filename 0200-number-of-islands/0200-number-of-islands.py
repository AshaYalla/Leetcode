class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = []
        m , n = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        sum = 0
        
        def bfs(start):
            answer = 0
            queue.append(start)
            while queue:
                qi,qj = queue.pop(0)
                if((qi,qj) not in visited and grid[qi][qj] == "1" ):
                    answer+=1
                    visited.add(start)
                for ii,jj in directions:
                    if(0<=qi+ii<m and 0<=qj+jj<n and (qi+ii,qj+jj) not in visited and grid[qi+ii][qj+jj] == "1"):
                        queue.append((qi+ii,qj+jj))
                        visited.add((qi+ii,qj+jj))
            return answer
        for i in range(m):
            for j in range(n):
                if((i,j) not in visited and grid[i][j] == "1" ):
                    sum += bfs((i,j))
        return sum
    
                
        
        