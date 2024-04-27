class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdictt = defaultdict(list)
        coldictt = defaultdict(list)
        boxdictt = defaultdict(list)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                ele = board[r][c]
                if ele != '.':
                    if ele in rowdictt[r]:
                        return False
                    rowdictt[r].append(ele)
                    if ele in coldictt[c]:
                        return False
                    coldictt[c].append(ele)
                    if ele in boxdictt[(r//3, c//3)]:
                        return False
                    boxdictt[(r//3, c//3)].append(ele)
        return True
                    
                    
            
