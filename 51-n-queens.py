from pprint import pprint
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        mainboard = [[True]*n]*n
        row = 5
        def queen_line_of_sight(x, y, i, j):
            return x == i or y == j or (i - x) == (j - y) or (i - x) == (y - j)
            
        def mark_unavailable(board, x, y):
            for i, line in enumerate(board):
                for j, _ in enumerate(line):
                    if queen_line_of_sight(i, j, x, y):
                        board[i][j] = False
                    
        def fill_next_queen(board):
            for i, line in enumerate(board):
                for j, allowed in enumerate(board):
                    if allowed:
                        board[i][j] = False
                        


Solution().solveNQueens(5)
        