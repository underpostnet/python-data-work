import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import random

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# x: cantidad de publicaciones por dias seleccionadas por mes
# y: cantidad de ventas por dias seleccionadas por mes
# numero, dia, publicaciones, ventas

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

data_agosto = np.loadtxt("data_mes/agosto.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_agosto[0])):
    list.append(i)

choose_agosto = random.sample(list,  13)
choose_agosto.sort()
print(choose_agosto)

filter_agosto_ventas = []
filter_agosto_publicaciones = []

for i in choose_agosto:
    filter_agosto_publicaciones.append(data_agosto[2][i])
    filter_agosto_ventas.append(data_agosto[3][i])


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

data_julio = np.loadtxt("data_mes/julio.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_julio[0])):
    list.append(i)

choose_julio = random.sample(list,  13)
choose_julio.sort()
print(choose_julio)

filter_julio_ventas = []
filter_julio_publicaciones = []

for i in choose_julio:
    filter_julio_publicaciones.append(data_julio[2][i])
    filter_julio_ventas.append(data_julio[3][i])

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

data_junio = np.loadtxt("data_mes/junio.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_junio[0])):
    list.append(i)

choose_junio = random.sample(list,  13)
choose_junio.sort()
print(choose_junio)

filter_junio_ventas = []
filter_junio_publicaciones = []

for i in choose_junio:
    filter_junio_publicaciones.append(data_junio[2][i])
    filter_junio_ventas.append(data_junio[3][i])

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

data_mayo = np.loadtxt("data_mes/mayo.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_mayo[0])):
    list.append(i)

choose_mayo = random.sample(list,  13)
choose_mayo.sort()
print(choose_mayo)

filter_mayo_ventas = []
filter_mayo_publicaciones = []

for i in choose_mayo:
    filter_mayo_publicaciones.append(data_mayo[2][i])
    filter_mayo_ventas.append(data_mayo[3][i])

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

data_septiembre = np.loadtxt("data_mes/septiembre.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_septiembre[0])):
    list.append(i)

choose_septiembre = random.sample(list,  16)
choose_septiembre.sort()
print(choose_septiembre)

filter_septiembre_ventas = []
filter_septiembre_publicaciones = []

for i in choose_septiembre:
    filter_septiembre_publicaciones.append(data_septiembre[2][i])
    filter_septiembre_ventas.append(data_septiembre[3][i])

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

main_data_ventas = []
main_data_publicaciones = []
main_dia = []

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

in_ = 0

for i in filter_agosto_ventas:
    main_data_ventas.append(i)
    main_dia.append(in_)
    in_ = in_ + 1

for i in filter_julio_ventas:
    main_data_ventas.append(i)
    main_dia.append(in_)
    in_ = in_ + 1

for i in filter_junio_ventas:
    main_data_ventas.append(i)
    main_dia.append(in_)
    in_ = in_ + 1

for i in filter_mayo_ventas:
    main_data_ventas.append(i)
    main_dia.append(in_)
    in_ = in_ + 1

for i in filter_septiembre_ventas:
    main_data_ventas.append(i)
    main_dia.append(in_)
    in_ = in_ + 1

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------


for i in filter_agosto_publicaciones:
    main_data_publicaciones.append(i)

for i in filter_julio_publicaciones:
    main_data_publicaciones.append(i)

for i in filter_junio_publicaciones:
    main_data_publicaciones.append(i)

for i in filter_mayo_publicaciones:
    main_data_publicaciones.append(i)

for i in filter_septiembre_publicaciones:
    main_data_publicaciones.append(i)


#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------



plt.plot(main_dia, main_data_publicaciones, 'k', label='publicaciones', color='blue')
plt.xlabel("Tiempo (días)")
plt.ylabel("Publicaciones")
#plt.legend()
show()

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

plt.plot(main_dia, main_data_ventas, 'k', label='ventas', color='red')
plt.xlabel("Tiempo (días)")
plt.ylabel("Ventas")
#plt.legend()
show()

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# plt.plot(data[0], data[1], 'k', label='publicaciones', color='blue')
# plt.plot(data[0], data[2], 'k', label='ventas', color='red')
# plt.xlabel("Tiempo (días)")
# plt.ylabel(" ")
# plt.legend()
# show()

#-------------------------------------------------------------------------------------------------
# parámetros involucrados
#-------------------------------------------------------------------------------------------------

print('')
print('--------------------------------------------------------')
print('media de publicaciones diarias: ', np.mean(main_data_publicaciones))
print('desviacion estandar de publicaciones diarias: ', np.std(main_data_publicaciones))
print('--------------------------------------------------------')
print('')

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

print('')
print('--------------------------------------------------------')
print('media de ventas diarias:', np.mean(main_data_ventas))
print('desviacion estandar de ventas diarias: ', np.std(main_data_ventas))
print('--------------------------------------------------------')
print('')

#-------------------------------------------------------------------------------------------------
# normal distribution
#-------------------------------------------------------------------------------------------------

from scipy.stats import norm
def generateNormal(plot_data):

    # Generate some data for this demonstration.
    # data = norm.rvs(10.0, 2.5, size=500)

    # Fit a normal distribution to the data:
    mu, std = norm.fit(plot_data)

    # print(mu)
    # print(std)

    # Plot the histogram.
    plt.hist(plot_data, bins=25, density=True, alpha=0.6, color='g')

    # Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    show();

    return True

generateNormal(main_data_ventas)

generateNormal(main_data_publicaciones)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------











#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
