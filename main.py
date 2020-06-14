'''
Main program for sudoku solver
'''
from sys import argv
import src.solver as solver

if len(argv) == 4:
    
   solver.solve(argv[1], argv[2], argv[3])

else:

    solver.invalid_solve()
