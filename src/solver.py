'''
General scheme to solve
a sudoku puzzle from text file or
image file and write its output
'''
from backtrack import *
from sudoku import *
from solver import *
from reader import *
import time

def solve(input_file, output_file, username):
    '''
    General scheme to solve
    a sudoku puzzle from a given 
    input file (in txt or jpg/png)
    and prints its solution
    '''

    sudoku = None
    config_tesseract(username)

    # Image input
    if input_file[-4:] == ".png" or input_file[-4:] == ".jpg":
        sudoku = read_image(input_file)
    # Text input
    elif input_file[-4:] == ".txt":
        sudoku = read_sudoku(input_file)
    # Other file format (not supported)
    else:
        print("Input file format not supported")
        return

    print("Solving sudoku. . .")

    start = time.time()

    # Starting backtracking algorithm
    # to solve the sudoku
    define_mrv_queue(sudoku)
    if backtracking_mrv(sudoku):
        print("Solved!")
    else:
        print("Puzzle can't be solved.")

    fin = time.time()

    # Output
    write_sudoku(sudoku, output_file)
    print("\nSolved in {:.4f} s".format(fin-start))

def invalid_solve():

    print("Invalid input!!")
    print("Use command: python main.py <input file> <output file> <username>")
