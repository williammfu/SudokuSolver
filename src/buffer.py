def increment(i,j):
    ''' Increment position  '''
    m, n = i, j
    n += 1
    if n > 8:
        n = 0
        m += 1
    return m, n

def is_duplicate(row):
    ''' Returns True if a duplicate exists '''
    cells = set()
    for cell in row:
        if cell in cells:
            return True
        elif cell is not None:
            cells.add(cell)

    return False

def accept(sudoku):
    ''' Returns True if a duplicate in Sudoku exists '''
    # Check row
    for row in sudoku:
        if is_duplicate(np.array(row).flatten()):
            return False

    # Check column
    columns = sudoku.transpose()
    for column in columns:
        if is_duplicate(np.array(column).flatten()):
            return False
    
    # Check grid
    INDICES = CELLS + {0} - {9}
    for i,j in product(INDICES, INDICES):
        if is_duplicate(get_grid(sudoku, i, j)):
            return False

    return True

def find_possible(sudoku, row, col):
    ''' Returns a set of posible answer to a cell '''
    pos = CELLS.copy()

    for i in CELLS:
        if sudoku[row,i] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[row,i])
        if sudoku[i,col] is not None and sudoku[row, i] in pos:
            pos.remove(sudoku[i, col])
    
    for s in get_grid(sudoku, row, col):
        if s is not None and s in pos:
            pos.remove(s)

    return pos

