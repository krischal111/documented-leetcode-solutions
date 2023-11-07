import numpy as np

full_line = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def get_indices(i, j):
    h = i
    v = j
    b = (i//3)*3 + (j//3)
    return h, v, b

def box_index(i,j):
    return (i//3)*3 + (j//3)
    
def get_horizontal_sets(board):
    sets = []
    for line in board:
        sets.append(full_line-set(line))
    return sets

def get_vertical_sets(board):
    sets = []
    for line in np.transpose(board):
        sets.append(full_line - set(line))
    return sets

def get_box_sets(board):
    sets = [set(full_line) for _ in range(9)]
    for i in range(9):
        for j in range(9):
            sets[box_index(i,j)].discard(board[i][j])
    return sets

def intify(board):
    board = [
        int(f) if f != '.' else 0
        for minilist in board
        for f in minilist
    ]
    my_board = np.array(board).reshape((9,9))
    return my_board

def acceptify(board):
    board = [
        [
            str(numero) if numero != 0 else '.'
            for numero in line
        ]
        for line in board
    ]
    return board

def full(board):
    for line in board:
        if set(line) != full_line:
            return False
    else:
        return True

def not_full(board):
    return not full(board)

from pprint import pprint      
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        myboard = intify(board)
        original_board = myboard.copy()
        # print(myboard)
        hset = get_horizontal_sets(myboard)
        vset = get_vertical_sets(myboard)
        bset = get_box_sets(myboard)
        # pprint(hset)
        # pprint(vset)
        # pprint(bset)

        count = 81
        while not_full(myboard):
            for i in range(9):
                for j in range(9):
                    if myboard[i][j] != 0:
                        continue
                    b = box_index(i,j)
                    possible_numbers = hset[i].intersection(vset[j]).intersection(bset[b])
                    # print(i,j, possible_numbers)
                    if len(possible_numbers) == 1:
                        myboard[i][j] = numero = possible_numbers.pop()
                        hset[i].discard(numero)
                        vset[j].discard(numero)
                        bset[b].discard(numero)
            count -= 1
            if not count:
                break
        
        solved_board = acceptify(myboard)
        for i in range(9):
            for j in range(9):
                board[i][j] = solved_board[i][j]
        
        # print(original_board)
        # print(myboard)

if __name__ == '__main__':
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Solution().solveSudoku(board)
    solution = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    array = [[box_index(i,j) for j in range(9)] for i in range(9)]
    # print(np.array(array))
    solved = intify(solution)
    # print(solved)
        