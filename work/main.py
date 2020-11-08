import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# a: cantidad de publicaciones registradas diarias
# b: cantidad de ventas registradas diarias

data = np.loadtxt("data.csv", delimiter=";", skiprows=1, usecols=[0,3,4], unpack=True)

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

plt.plot(data[0], data[1], 'k', label='publicaciones', color='blue')
plt.xlabel("Tiempo (días)")
plt.ylabel("Publicaciones")
#plt.legend()
show()

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

plt.plot(data[0], data[2], 'k', label='ventas', color='red')
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
print('media de publicaciones diarias: ', np.mean(data[1]))
print('desviacion estandar de publicaciones diarias: ', np.std(data[1]))
print('--------------------------------------------------------')
print('')

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

print('')
print('--------------------------------------------------------')
print('media de ventas diarias:', np.mean(data[2]))
print('desviacion estandar de ventas diarias: ', np.std(data[2]))
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

generateNormal(data[1])

generateNormal(data[2])

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------


# -> 68 datos aleatorios
# -> 68 datos estratificados
