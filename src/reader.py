'''
I/O Module for a
sudoku puzzle instance
'''
import numpy as np
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ASUS\AppData\Local\Tesseract-OCR\tesseract.exe"

TEST_DIR = "./test/"
OUT_DIR = "./out/"
DIGITS = {1,2,3,4,5,6,7,8,9}

def read_sudoku(filename):
    ''' Reads a sudoku instance '''
    
    filepath = TEST_DIR + filename
    parsed = []
    with open(filepath, "r") as f:
        parsed = [x.strip().split(" ") for x in f]
    
    mat = []
    for parse in parsed:
        row = [ None if cell == "#" else int(cell) for cell in parse ]
        mat.append(row)
    
    # print(np.matrix(mat))
    return np.matrix(mat)

def write_sudoku(sudoku, filename="result.txt"):
    ''' Prints sudoku to command line and a txt file '''

    mat = np.array(sudoku).tolist()
    cells = []
    
    # Prints Matrix in file
    output = OUT_DIR + filename
    with open(output, "w") as f:
        for i in range(9):
            for j in range(9):
                f.write(str(mat[i][j]) + " ")
                print(mat[i][j], end=" ")
                if mat[i][j] == 5:
                    cells.append((i+1,j+1))
            f.write("\n")
            print(" ")
        
        for cell in cells:
            f.write(str(cell) + "\n")
            print(cell, end=" ")

def read_image(image_name):
    ''' Reads an image of a sudoku instance '''
    
    # Directory in test
    full_path = TEST_DIR + image_name 
    img = cv2.imread(full_path)
    sudoku = []
    config = r"--oem 3 --psm 6 outputbase digits"

    for i in range(9):
        row = []
        for j in range(9):
            r = img[ (i*31) + 1: (i+1)*31 + 1, (j*31) + 1 : (j+1)*31 + 1]
            digit = pytesseract.image_to_string(r, config=config).replace(".","").replace("-","")
            if digit == "":
                row.append(None)
            else:
                row.append(int(digit) % 10)
        sudoku.append(row)
    
    return np.matrix(sudoku)

if  __name__ == "__main__":
    f, g = 'image2.png', "tc4.txt"
    a = read_image(f)
    b = read_sudoku(g)
    print(a)
    print(b)
