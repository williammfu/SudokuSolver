'''
I/O Module for a
sudoku puzzle instance
'''
import numpy as np
import cv2
import pytesseract
UNAME = "ASUS"
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\{}\AppData\Local\Tesseract-OCR\tesseract.exe".format(UNAME)

TEST_DIR = "../test/"
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

def thresholding(image):
    ''' Thresholding an image after reducing its noise '''
    blur = cv2.GaussianBlur(image,(5,5),0)
    return cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

def make_grid(i, j):
    ''' Returns the slice of an image '''

    # Offsets, to avoid the lines
    n_offset = 3 if i == 3 or i == 0 or i == 2 else 1
    w_offset = -3 if j == 5 else 3 if j == 0 else 1
    s_offset = 2 if i !=5 and i != 2 else -1
    e_offset = 1 if j != 5 and j != 8 else -4

    # Slicing
    n = i*32 + n_offset # North
    w = j*32 + w_offset # West
    s = (i+1)*32 + s_offset # South
    e = (j+1)*32 + e_offset # East

    return n, s, w, e


def read_image(image_name):
    ''' Reads an image of a sudoku instance '''
    
    # Directory in test
    full_path = TEST_DIR + image_name 
    img = cv2.imread(full_path, 0)
    tr = thresholding(img)

    sudoku = []
    config = r"--oem 3 --psm 6 outputbase digits" # Tesseract config to read digits only

    for i in range(9):
        row = []
        for j in range(9):
            n, s, w, e = make_grid(i, j)
            r = tr[ n : s, w : e ]
            digit = pytesseract.image_to_string(r, config=config).replace(".","").replace("-","").replace("\n","")
            if digit == "":
                row.append(None)
            else:
                row.append(int(digit) % 10)
        sudoku.append(row)
    
    return np.matrix(sudoku)

if  __name__ == "__main__":

    f, g = 'image4.png', "tc1.txt"
    a = read_image(f)
    b = read_sudoku(g)
    print(a)
    print(b)
