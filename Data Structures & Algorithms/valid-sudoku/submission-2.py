class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # (Row / 3) * 3 + (col/3)
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rowSet:
                    return False
                else:
                    rowSet.add(board[i][j])
        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in colSet:
                    return False
                else:
                    colSet.add(board[j][i])
        for i in range(9):
            squareSet = set()
            for x in range(3):
                for y in range(3):
                    row = (i//3) * 3 + x
                    col = (i%3) * 3 + y
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in squareSet:
                        return False
                    else:
                        squareSet.add(board[row][col])
        return True