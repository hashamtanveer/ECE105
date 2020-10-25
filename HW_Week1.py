#!/usr/bin/env python
# coding: utf-8

# In[3]:




# ECE 105: Programming for Engineers II (Spring, 2020)
# HW : DNA Word Search
# Student name:  Hasham Tanveer 
# Email ID:         ht369              


import numpy as np



def find(word):
    if checkRows(word) or checkCols(word) or checkDiag(word) or checkDiagRev(word):
        return True
    else:
        return False


def checkRows(word):
    found = False
    for row in range(board.shape[0]) :
        row_array = board[row,:]
        row_string = ''.join(row_array)
        row_string_r = row_string[::-1]
        if word in row_string or word in row_string_r:
            found = True
    return found

def checkCols(word):
    found = False
    for col in range(board.shape[1]) :
        col_array = board[:,col]
        col_string = ''.join(col_array)
        col_string_r = col_string[::-1]
        if word in col_string or word in col_string_r:
            found = True
    return found

def checkDiag(word):
    found = False
    for diag in range(np.negative(board.shape[0])+1, board.shape[1]) :
        diag_array = board.diagonal(diag)
        diag_string = ''.join(diag_array)
        diag_string_r = diag_string[::-1]
        if word in diag_string or word in diag_string_r:
            found = True
    return found

def checkDiagRev(word):
    
    found = False
    board_rev=np.fliplr(board)
    for diagr in range(np.negative(board_rev.shape[0])+1, board_rev.shape[1]) :
    
        diagr_array = board_rev.diagonal(diagr)
        diagr_string = ''.join(diagr_array)
        diagr_string_r = diagr_string[::-1]
        
        if word in diagr_string or word in diagr_string_r:
            found = True
    return found


if __name__ == '__main__':   # check if run this script as the main file
    # If run this Python script file as the main file, then do following tests
    # else (e.g. when import this script into another file), the following 
    #   code will be skipped.
    
    # --- Example test setup 1: for testing the whole function "find"
    board = np.array([['A','A','A','T'],
                      ['A','G','G','C'],
                      ['A','T','G','C'],
                      ['A','A','T','A'],
                      ['A','T','A','A']])
    word = 'ACCT' # Expect True, ACCT is at the last column, read upward
    # word = 'CTT'  # Expect True, CTT is at anti diag, SouthWest direction
    # word = 'ATTA'  # Expect True, ATTA is at diag, SouthEast direction
    # word = 'AAA' # Expect True, found in many directions and locations
    # word = 'TTTA' # Expect False, not anywhere
    # word = 'TTTAGCTA' # Expect False, not anywhere, also too long
    
    print('=== Test case starts ===========================================')
    result = find(word) 
    print(board)
    print('*** Target word:', word, '\tResult:', result)
    print('=== Test case ends ===========================================')

    





# In[ ]:




