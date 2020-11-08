
import numpy as np

list = [1, 2, 5, 3]

print(np.mean(list))
print(np.std(list))


x = np.matrix(np.arange(12).reshape((3, 4)))

print(x)

#mediana

print(x.mean())

print(x.mean(0))

print(x.mean(1))

print('-----')

#desviacion estandar

print(x.std())

print(x.std(0))

print(x.std(1))
