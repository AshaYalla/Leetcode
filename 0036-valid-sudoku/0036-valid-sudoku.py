class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(list)
        coldict = defaultdict(list)
        boxdict = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowdict[i]:
                    print("a")
                    return False
                rowdict[i].append(board[i][j])
                if board[i][j] in coldict[j]:
                    print("b")
                    return False
                coldict[j].append(board[i][j])
                if board[i][j] in boxdict[(i//3 , j//3)]:
                    print("c")
                    return False
                boxdict[(i//3 , j//3)].append(board[i][j])

        return True
                
        