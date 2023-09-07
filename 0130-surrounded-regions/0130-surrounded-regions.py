class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        queue = []
        m = len(board)
        n = len(board[0])
        nei = [(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(len(board)):
            if board[i][0] == "O":
                visited.add((i,0))
                queue.append((i,0))
            if board[i][n-1] == "O":
                visited.add((i,n-1))
                queue.append((i,n-1))
                
        for j in range(len(board[0])):
            if board[0][j] == "O":
                visited.add((0,j))
                queue.append((0,j))
            if board[m-1][j] == "O":
                visited.add((m-1,j))
                queue.append((m-1,j))
                
        while(queue):
            r, c = queue.pop(0)
            for i,j in nei:
                if r+i >=0 and r+i <m and c+j >=0 and c+j < n and (r+i,c+j) not in visited and board[r+i][c+j] == "O":
                    visited.add((r+i,c+j))
                    queue.append((r+i,c+j))
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
        return board
                    
                    
                
                
                
                
                
        