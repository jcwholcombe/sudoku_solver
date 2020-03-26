import numpy as np


"""board=([0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0])"""

board=([5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,7,9])




def is_possible(x, y, number):
    global board
    """check y coordinate"""
    if number in board[y]:
        return False

    """check x coordinate"""
    for i in range(9):
        if board[i][x] == number:
            return False

    """check if it's in the same box"""
    x_box=3*(x//3)
    y_box=3*(y//3)

    for i in range(x_box,x_box+3):
        for j in range(y_box,y_box+3):
            if board[j][i] == number:
                return False

    return True



def solver():
    global board
    """solves and returns the solved Sudoku puzzle"""
    for i in range(9):
        for j in range(9):
            if board[j][i] == 0:
                """itterate through each number to place on board"""
                for k in range(1,10):
                    if is_possible(i, j, k):
                        board[j][i] = k
                        solver()
                        board[j][i] = 0
                return
    return print(np.matrix(board))

solver()
