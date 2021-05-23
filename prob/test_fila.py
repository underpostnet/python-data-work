
import numpy as np

H = [12,34,52,54,76]
ind = 0
new_H = []
for x in range(len(H)):
    fila_ = []
    for y in range(len(H)):
        if x==y:
            fila_.append(H[ind])
            ind = ind + 1
        else:
            fila_.append(0)

    new_H.append(fila_)

print(np.matrix(new_H))
