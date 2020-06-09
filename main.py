'''
Main program for sudoku solver
'''
import sys, time
sys.path.append("./src/")
from src import reader, solver

if len(sys.argv) == 2:
    
    filename = sys.argv[1]
    sudoku = reader.read_sudoku(filename)

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
