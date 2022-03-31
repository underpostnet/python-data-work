
import pandas as pd

def isNaN(num):
    return num != num

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

A = np.array([[1, 6, 500, 0.008, 0.030],
            [2, 10, 400, 0.010, 0.025],
            [3, 14,	600, 0.011, 0.020],
            [4, 15,	350, 0.009,	0.015]])

# Empty 2 x 3 matrix


def iterateArray(MATRIX):

    arr = np.zeros([3, 3])
    arrX = 0
    arrY = 0

    y = 0
    for row in MATRIX:
        x = 0
        for value in row:
            if y < ( len(MATRIX) - 1 ) and x > 1:
                print('value ->')
                print(value)
                # arr[arrY][arrX] = A[y][x] / A[y + 1][x]
                # if arrX == (len(A[0]) - 2):
                #     arrX = 0
                #     arrY += 0
                # else:
                #     arrX += 1

            # print('y ->')
            # print(y)
            # print('x ->')
            # print(x)
            # print('value ->')
            # print(value)
            # print(arr[y][x])
            x += 1
        y += 1

    print('arr ->')
    print(arr)

iterateArray(A)








# ------------------------------------------------------------------------------
