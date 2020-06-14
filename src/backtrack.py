'''
Sudoku solver module
using the backtracking algorithm
'''
from itertools import product
from src.sudoku import *

INDICES = set(range(9))
CELLS = set(range(1,10))
UNFILLED = [] # Queue to store unfilled cells

class Unfill:

    def __init__(self, i, j, values):
        ''' Constructor '''
        self.i = i
        self.j = j
        self.values = values
    
    def __lt__(self, value):
        ''' Operator overload (<) '''
        return len(self.values) < len(value.values)

    def __repr__(self):
        ''' Prints the unfilled '''
        return "(" + str(self.i) + "," + str(self.j) + ")" + str(len(self.values))

def backtracking(sudoku):
    ''' Backtracking algorithm in solving sudoku '''

    # Find empty cell
    i, j = empty_cells(sudoku)

    # This block acts as the base
    # of this recursive function
    # Recurrence stops when all cells are filled
    if (i,j) == (9,9):
        return True

    # Fills cell(i,j) with values 1..9
    for cell in CELLS:
        if is_valid(sudoku, i, j, cell):
            sudoku[i,j] = cell
            
            # Backtrack recursively
            if backtracking(sudoku):
                return True

            # Empties cell(i,j)
            sudoku[i,j] = None
    
    # All values 1..9 are invalid
    return False

def backtracking_mrv(sudoku):
    ''' 
    Backtracking algorithm in solving sudoku 
    with Minimum Remaining Value (MRV) heuristics
    '''

    # This block acts as the base
    # of this recursive function
    # Recurrence stops when all cells are filled
    if not UNFILLED:
        return True

    # Takes the cell with the least
    # remaining values
    least = UNFILLED.pop(0)
    i, j = least.i, least.j
    poss = least.values # Possible values for cell(i,j)

    # Checks every possible values
    for cell in poss:
        if is_valid(sudoku, i, j, cell):
            sudoku[i,j] = cell
            
            # Backtracking recursively
            if backtracking(sudoku):
                return True
            
            # Empties cell(i,j)
            sudoku[i,j] = None
    
    # If all possible values are invalid
    # put it back to the queue
    UNFILLED.push(least)
    UNFILLED.sort()
    return False

def define_mrv_queue(sudoku):
    ''' Creates a list of minimum remaining value '''

    for i, j in product(INDICES, INDICES):

        # Found an empty cell        
        if not sudoku[i,j]:
            possible = find_possible(sudoku, i, j)
            UNFILLED.append(Unfill(i, j, possible))
    
    # Sorts the list based on the
    # number of remaning values ascendingly
    UNFILLED.sort()

