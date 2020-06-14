'''
Sudoku Solver
'''
from itertools import product
import heapq
import numpy as np
import reader

CELLS = set(range(1,10))
INDICES = set(range(9))
GRIDS = [slice(0,3), slice(3,6), slice(6,9)]
UNVISITED = []

class Unvis:

    def __init__(self, i, j, values):
        self.i = i
        self.j = j
        self.values = values
    
    def __lt__(self, value):
        return len(self.values) < len(value.values)

    def __repr__(self):
        return str(self.i) + " " + str(self.j) + " " + str(len(self.values))


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

def is_duplicate(row):
    ''' Returns True if a duplicate exists '''
    cells = set()
    for cell in row:
        if cell in cells:
            return True
        elif cell is not None:
            cells.add(cell)

    return False

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

def backtracking_mrv(sudoku):
    ''' 
    Backtracking algorithm in solving sudoku 
    with Minimum Remaining Value (MRV) heuristics
    '''

    if not UNVISITED:
        return True

    least = UNVISITED.pop(0)
    i, j = least.i, least.j
    poss = least.values

    for cell in poss:
        if is_valid(sudoku, i, j, cell):
            sudoku[i,j] = cell
            if backtracking(sudoku):
                return True
            sudoku[i,j] = None
    
    UNVISITED.push(least)
    UNVISITED.sort()
    return False

def find_possible(sudoku, row, col):
    ''' Returns a set of posible answer to a cell '''
    pos = list(CELLS.copy())

    for i in INDICES:
        if sudoku[row,i] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[row, i])
        if sudoku[i,col] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[i, col])
    
    for s in get_grid(sudoku, row, col):
        if s is not None and s in pos:
            pos.remove(s)

    return pos

def define_mrv_queue(sudoku):
    ''' Creates a list of minimum remaining value '''

    for i, j in product(INDICES, INDICES):
        
        if not sudoku[i,j]:
            possible = find_possible(sudoku, i, j)
            UNVISITED.append(Unvis(i, j, possible))
    
    UNVISITED.sort()

if __name__ == "__main__":
    import time
    filename = "tc1.txt"
    a = reader.read_sudoku(filename)
    b = reader.read_sudoku(filename)
    st = time.time()
    # print(b.pop(0))
    # rec(a,b)
    # print(a)
    backtracking(a)
    mid = time.time()
    # define_mrv_queue(b)
    # backtracking_mrv(b)
    fin = time.time()
    print(b)
    print("{:.6f} {:.6f}".format(mid-st, fin-mid))
    # reader.write_sudoku(a, filename)
