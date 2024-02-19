class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        que = []
        res = 0
        visited = set()
        
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    que.append((r,c,0))
                    
    
        while(que):

            i,j,level = que.pop(0)
            if (i,j) not in visited:
                visited.add((i,j))


            for ni,nj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<= i+ni <= len(rooms)-1 and 0<= j+nj <=len(rooms[0])-1 and rooms[i+ni][j+nj] == 2147483647 :
                    que.append((i+ni, j+nj,level+1))
                    rooms[i+ni][ j+nj] = level+1
                        

        
        