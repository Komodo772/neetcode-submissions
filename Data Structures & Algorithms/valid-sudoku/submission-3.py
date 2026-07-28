class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ##board = [[0] * 9 for i in range(9)]

        for row in board:
            dupecheck = set()
            for panel in row:
                if panel == ".":
                    continue
                if panel in dupecheck:
                    return False
                dupecheck.add(panel)
        
        for i in range(9):
            dupecheck = set()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in dupecheck:
                    return False
                dupecheck.add(row[i])

        for square in range(9):
            dupecheck = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in dupecheck:
                        
                        return False
                    dupecheck.add(board[row][col])
        return True
        