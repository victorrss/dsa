class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rows = set()
            cols = set()
            for j in range(len(board)):
                row = board[i][j]
                col = board[j][i]
                if row != ".":
                    if row in rows:
                        return False
                    else:
                        rows.add(row)
                if col != ".":
                    if col in cols:
                        return False
                    else:
                        cols.add(col)
        rows = [[0, 2], [0, 2], [0, 2], [3, 5], [3, 5], [3, 5], [6, 8], [6, 8], [6, 8]]
        cols = [[0, 2], [3, 5], [6, 8], [0, 2], [3, 5], [6, 8], [0, 2], [3, 5], [6, 8]]
        for b in range(9):
            rowStart = rows[b][0]
            rowEnd = rows[b][1]
            box = set()
            for i in range(rowStart, rowEnd + 1):
                colStart = cols[b][0]
                colEnd = cols[b][1]
                for j in range(colStart, colEnd + 1):
                    cell = board[i][j]

                    if cell != ".":
                        if cell in box:
                            return False
                        else:
                            box.add(cell)
        return True
