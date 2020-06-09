'''
Sudoku Solver
'''
from itertools import product
import heapq
import numpy as np
import reader

CELLS = set(range(1,10))
GRID_SET = {0, 3, 6}
GRIDS = [slice(0,3), slice(3,6), slice(6,9)]

def is_valid(sudoku, row, col, cell):
    ''' Returns True if S[row, col] cell value is valid '''

    s_row = np.array(sudoku[row]).flatten() # Rows
    s_col = np.array(sudoku[:,col]).flatten() # Columns
    s_grid = get_grid(sudoku, row, col) # Grid (3x3)

    return (
        np.count_nonzero(s_row == cell) == 0 and
        np.count_nonzero(s_col == cell) == 0 and
        np.count_nonzero(s_grid == cell) == 0
    )

def get_grid(sudoku, row, col):
    ''' Returns the grid from a cells '''
    return np.array(sudoku[GRIDS[row//3], GRIDS[col//3]]).flatten()

def empty_cells(sudoku):
    ''' Returns the i,j value of the empty cells '''
    for i in range(9):
        row = list(np.array(sudoku[i]).flatten())
        if None in row:
            return i, row.index(None)

    return 9, 9 

def backtracking(sudoku):
    ''' Backtracking algorithm in solving sudoku '''

    i, j = empty_cells(sudoku)

    if (i,j) == (9,9):
        return True

    for cell in CELLS:
        if is_valid(sudoku, i, j, cell):
            sudoku[i,j] = cell
            if backtracking(sudoku):
                return True
            sudoku[i,j] = None
    
    return False

if __name__ == "__main__":
    import time
    st = time.time()
    filename = "tc1.txt"
    a = reader.read_sudoku(filename)
    print(backtracking(a))
    fin = time.time()
    reader.write_sudoku(a, filename, (fin-st))
