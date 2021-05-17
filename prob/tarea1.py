import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import show


# A = np.array([
#     [0.997316607,0.002690613,0,0,0],
#     [0.004023071,0.99286855,0.003146941,0,0],
#     [0,0,0.008602793,0.988442309,0.003063684],
#     [0,0,0.006398383,0.987325013,0.006398383],
#     [0,0,0,0.005847028,0]
# ])

v = np.array([[-2.687,2.687,0,0,0],
     [4.015,-7.157,3.142,0,0],
     [0, 8.566,-11.625,3.059,0],
     [0,0, 6.378,-12.756,6.378],
     [0,0,0,5.830,-5.830]])

delta=10
A = np.exp((10**-4)*v*delta)

print('pre fix A ->')
print(A)

cont_y = 1
new_A = []
for fila in A:
    cont_x = 1
    new_fila = []
    for elemento_fila in fila:
        if not (cont_x==cont_y):
            new_fila.append((elemento_fila - 1))
        else:
            new_fila.append(elemento_fila)

        cont_x = cont_x + 1

    new_A.append(new_fila)
    cont_y = cont_y + 1

print('post fix A ->')
print(np.array(new_A))

A = new_A


b = 1.78563
n = 21632.3
w = 0.0468681
t = [0,15,30,55,85]

print('t ->')
print(t)

delta = 10
t0 = 5000
tf = 6000


I = np.array([
     [1,0,0,0,0],
     [0,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,0],
     [0,0,0,0,1]
])

h = []
for val in t:
    hazard = (b/n) * ((t0/n)**(b-1)) * np.exp((w*val))
    h.append(hazard)

print('h ->')
print(h)

Lt = [
     [1,0,0,0,0],
     [0,1,0,0,0],
     [0,0,1,0,0],
     [0,0,0,1,0],
     [0,0,0,0,1]
];

sum_limit = 600
plot_matriz = []
plot_axis_x = []

while sum_limit <= 2500:

    plot_axis_x.append((sum_limit*10))

    for i in range(500, sum_limit):
        H = []
        for val in t:

            exp_a = (delta/n)**(b)
            exp_c = (i)**( ( b - (i+1)**(b) ) )
            exp_b =  np.exp((w*val))**exp_c

            hazard = np.exp((exp_a*exp_b))
            H.append(hazard)

        mh = H * I
        Li = mh * A
        Lt = Lt * Li
        # print('Li ', i, ' ->')
        # print(Li)

        if i == (sum_limit-1):
            suma_Lt = []
            for fila in Lt:
                total_suma = 0
                for val_fila in fila:
                     total_suma = total_suma + val_fila
                suma_Lt.append(total_suma)

            print('suma_Lt ->')
            print(suma_Lt)
            plot_matriz.append(suma_Lt)


    sum_limit = sum_limit + 100



print('Lt ->')
print(Lt)


plot_matriz = np.array(plot_matriz)
print('plot_matriz ->')
plot_matriz = plot_matriz.T
print(plot_matriz)

print('x azis ->')
print(plot_axis_x)
print(len(plot_axis_x))
print(len(plot_matriz[0]))

# ploteo de grafico

import random
number_of_colors = len(plot_matriz)
color_ = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
print(color_)

cont_serie = 0
for generate_plot in plot_matriz:
    plt.plot(plot_axis_x, generate_plot, 'k', label=('{}{}'.format('Estado ', cont_serie)), color=color_[(cont_serie-1)])
    cont_serie = cont_serie + 1

plt.xlabel("Working Age")
plt.ylabel("Reliability")
plt.legend()
show()




# end
