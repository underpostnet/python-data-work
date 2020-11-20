import numpy as np #Librería numérica
import matplotlib.pyplot as plt # Para crear gráficos con matplotlib
from matplotlib.pyplot import show
import random

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

# x: cantidad de publicaciones por dias seleccionadas por mes
# y: cantidad de ventas por dias seleccionadas por mes
# numero, dia, publicaciones, ventas

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

print('seleccion de datos aleatorios estratificados por mes:')

data_agosto = np.loadtxt("data_mes/agosto.csv", delimiter=";", skiprows=1, usecols=[0,2,3,4], unpack=True)

list = []

for i in range(len(data_agosto[0])):
    list.append(i)

choose_agosto = random.sample(list,  13)
choose_agosto.sort()
print('agosto: ',choose_agosto)

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
print('julio: ',choose_julio)

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

choose_junio = random.sample(list,  14)
choose_junio.sort()
print('junio: ',choose_junio)

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

choose_mayo = random.sample(list,  14)
choose_mayo.sort()
print('mayo: ',choose_mayo)

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

choose_septiembre = random.sample(list,  14)
choose_septiembre.sort()
print('septiembre: ',choose_septiembre)

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
plt.legend()
show()

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

plt.plot(main_dia, main_data_ventas, 'k', label='ventas', color='red')
plt.xlabel("Tiempo (días)")
plt.ylabel("Ventas")
plt.legend()
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



# https://www.cienciadedatos.net/documentos/py10-regresion-lineal-python.html

# ¿Existe una relación entre el número de publicaciones y el número de ventas?

import pandas as pd
from scipy.stats import pearsonr

datos = pd.DataFrame({'dias': main_dia, 'publicaciones': main_data_publicaciones, 'ventas': main_data_ventas})
datos.head(3)

# El primer paso antes de generar un modelo de regresión simple
# es representar los datos para poder intuir si existe una
# relación y cuantificar dicha relación mediante un coeficiente
# de correlación.

print(datos)

fig, ax = plt.subplots(figsize=(6, 3.84))

datos.plot(
    x    = 'publicaciones',
    y    = 'ventas',
    c    = 'firebrick',
    kind = "scatter",
    ax   = ax
)
ax.set_title('Distribución de publicaciones y ventas');

show()

corr_test = pearsonr(x = datos['publicaciones'], y =  datos['ventas'])
print("Coeficiente de correlación de Pearson: ", corr_test[0])
print("P-value: ", corr_test[1])



# El gráfico y el test de correlación muestran una relación lineal,
# de intensidad considerable (r = []) y significativa
# (p-value = []). Tiene sentido intentar generar un
# modelo de regresión lineal con el objetivo de predecir
# el número de ventas en función del número de publicaciones.

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------



# Ajuste del modelo

# Se ajusta un modelo empleando como variable respuesta ventas y
# como predictor publicaciones. Como en todo estudio predictivo,
# no solo es importante ajustar el modelo, sino también
# cuantificar su capacidad para predecir nuevas observaciones.
# Para poder hacer esta evaluación, se dividen los datos en dos
# grupos, uno de entrenamiento y otro de test.


import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf


# División de los datos en train y test
# ==============================================================================
X = datos[['publicaciones']]
y = datos['ventas']

X_train, X_test, y_train, y_test = train_test_split(
                                        X.values.reshape(-1,1),
                                        y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

# Creación del modelo
# ==============================================================================
modelo = LinearRegression()
modelo.fit(X = X_train.reshape(-1, 1), y = y_train)

# Información del modelo
# ==============================================================================
print("Intercept:", modelo.intercept_)
del list
li = list(zip(X.columns, modelo.coef_.flatten()))
print("Coeficiente:", li)
print("Coeficiente de determinación R^2:", modelo.score(X, y))


# Una vez entrenado el modelo, se evalúa la capacidad predictiva
# empleando el conjunto de test.

# Error de test del modelo
# ==============================================================================
predicciones = modelo.predict(X = X_test)
print('evaluacion de la capacidad predictiva:')
print(predicciones)
print('')

rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = predicciones,
        squared = False
       )
print("")
print(f"El error (rmse) de test es: {rmse}")

# División de los datos en train y test
# ==============================================================================
X = datos[['publicaciones']]
y = datos['ventas']

X_train, X_test, y_train, y_test = train_test_split(
                                        X.values.reshape(-1,1),
                                        y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

# Creación del modelo utilizando matrices como en scikitlearn
# ==============================================================================
# A la matriz de predictores se le tiene que añadir una columna de 1s para el intercept del modelo
X_train = sm.add_constant(X_train, prepend=True)
modelo = sm.OLS(endog=y_train, exog=X_train,)
modelo = modelo.fit()
print(modelo.summary())


# Intervalos de confianza para los coeficientes del modelo
# ==============================================================================
print('')
print('Intervalos de confianza para los coeficientes del modelo')
print(modelo.conf_int(alpha=0.05))
print('')


# Predicciones:

# Una vez entrenado el modelo, se pueden obtener predicciones
# para nuevos datos. Los modelos de statsmodels permiten
# calcular las predicciones de dos formas:

# .predict(): devuelve únicamente el valor de las predicciones.

# .get_prediction().summary_frame(): devuelve, además de
# las predicciones, los intervalos de confianza asociados.

predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
predicciones.head(4)


print('data - predicciones')
print(predicciones)


# Predicciones con intervalo de confianza del 95%
# ==============================================================================
predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
predicciones['x'] = X_train[:, 1]
predicciones['y'] = y_train
predicciones = predicciones.sort_values('x')

# Gráfico del modelo
# ==============================================================================
fig, ax = plt.subplots(figsize=(6, 3.84))

ax.scatter(predicciones['x'], predicciones['y'], marker='o', color = "gray")
ax.plot(predicciones['x'], predicciones["mean"], linestyle='-', label="OLS")
ax.plot(predicciones['x'], predicciones["mean_ci_lower"], linestyle='--', color='red', label="95% CI")
ax.plot(predicciones['x'], predicciones["mean_ci_upper"], linestyle='--', color='red')
ax.fill_between(predicciones['x'], predicciones["mean_ci_lower"], predicciones["mean_ci_upper"], alpha=0.1)
ax.legend();

show()


# Error de test del modelo
# ==============================================================================
X_test = sm.add_constant(X_test, prepend=True)
predicciones = modelo.predict(exog = X_test)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = predicciones,
        squared = False
       )
print("")
print(f"El error (rmse) de test es: {rmse}")

# El error de test del modelo es de [rmse]
# Las predicciones del modelo final se
# alejan en promedio 59.34 unidades del valor real.




















#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
















#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
