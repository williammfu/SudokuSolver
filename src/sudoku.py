'''
Sudoku Module:
Represents the constraints
inside a a 9x9 matrix
'''
import numpy as np

# Slicing object for 3x3 submatrix inside sudoku
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

    # Empty cells not found
    return 9, 9 

def find_possible(sudoku, row, col):
    ''' Returns a set of posible answer to a cell '''
    pos = list(range(1,10))

    for i in range(9):
        if sudoku[row,i] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[row, i])
        if sudoku[i,col] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[i, col])
    
    for s in get_grid(sudoku, row, col):
        if s is not None and s in pos:
            pos.remove(s)

    return pos
