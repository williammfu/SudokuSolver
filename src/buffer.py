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
    
    # Empty cells exist
    if None in sudoku:
        return False

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



