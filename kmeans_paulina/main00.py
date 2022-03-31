
import pandas as pd

def isNaN(num):
    return num != num

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

Y = []
X = []

A = np.array([[1, 6, 500, 0.008, 0.030],
            [2, 10, 400, 0.010, 0.025],
            [3, 14,	600, 0.011, 0.020],
            [4, 15,	350, 0.009,	0.015]])

for i in range(0, 46):
    X.append(i)
    if i <= 6:
        k = 1
    elif i <= 16:
        k = 2
    elif i <= 30:
        k = 3
    else:
        k = 4

    Y.append(k * i)


plt.plot(X, Y, 'k', color='green') # label='Confiabilidad',
# plt.plot(tiempo, pob2, 'k:', label='Población B', color='red')
plt.xlabel("Tiempo (días)")
plt.ylabel("Confiabilidad")
plt.legend()

show()


# ------------------------------------------------------------------------------
