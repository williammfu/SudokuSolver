'''
Main program for sudoku solver
'''
import sys, time
sys.path.append("./src/")
from src import reader, solver

if len(sys.argv) == 2:
    
    filename = sys.argv[1]
    frmat = filename[-4:]

    sudoku = []
    if frmat == ".png":
        sudoku = reader.read_image(filename)
    elif frmat == ".txt":
        sudoku = reader.read_sudoku(filename)
    else:
        print("Format not found")
        sys.exit()

    print("Solving sudoku. . .")
    
    start = time.time()
    if solver.backtracking(sudoku):
        print("Solved!")
    else:
        print("Puzzle can't be solved.")
    fin = time.time()

    reader.write_sudoku(sudoku, filename)
    print(fin-start)

else:

    print("Invalid input")
    print("Use command: python main.py <filename>")
    sys.exit()
