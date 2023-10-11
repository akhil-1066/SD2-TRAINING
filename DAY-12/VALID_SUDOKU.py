class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(i,j):
            t=[]
            row=(i//3)*3
            col=(j//3)*3
            for x in board[row:row+3]:
                for y in x[col:col+3]:
                    t.append(y)
            if board[i].count(board[i][j])>1 or board1[j].count(board[i][j])>1 or t.count(board[i][j])>1:
                return False
            return True
        board1=list(zip(*board))
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if not is_valid(i,j):
                        return False
        return True
