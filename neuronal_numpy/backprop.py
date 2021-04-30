import numpy as np

# https://www.youtube.com/watch?v=jKPWYlOxPMU

from data_prep import features,targets, features_test, targets_test

print('--------------')
print('Init BackoProp')
print('--------------')

# funcion establecida por una regresion lineal ?
def sigmoide(x):
    return 1/(1 + np.exp(-x))


# Hyperparameters
n_hidden = 2 # Número de unidades en la capa escondida
epochs = 1000 # Número de iteraciones sobre el conjunto de entrenamiento
alpha = 0.01 # Taza de aprendizaje

ult_costo = None

m,k = features.shape # Número de ejemplos de entrenamiento, número de dimensiones en los datos

print('(m) numero ejemplos entrenamiento ->')
print(m)
print('(k) numero de dimensiones datos ->')
print(k)

# Inicialización de los pesos
# Scale-> Standard deviation
scale = 1/k**0.5
# scale = 0
print('(scale) (1/k**0.5) ->')
print(scale)

# np.random.normal(mu, sigma, size_data_number)

print('(entrada_escondida) ->')
entrada_escondida = np.random.normal(0, scale, size = (k,n_hidden) )
print(entrada_escondida)

print('(escondida_salida) ->')
escondida_salida = np.random.normal(0, scale, size = n_hidden )
print(escondida_salida)

# Entrenamiento

for e in range(epochs):

    # Variables para el gradiente
    gradiente_entrada_escondida = np.zeros(entrada_escondida.shape)
    gradiente_escondida_salida =  np.zeros(escondida_salida.shape)

    # print('--------------------------------')
    # print('epochs ->')
    # print(e)
    # print('gradiente_entrada_escondida ->')
    # print(gradiente_entrada_escondida)
    # print('gradiente_escondida_salida ->')
    # print(gradiente_escondida_salida)


    # Itera sobre el conjunto de entrenamiento
    _zip = zip(features.values,targets);

    # print('---')
    # print(type(features.values[0]))
    # print(type(targets))

    # el zip lo que hace es unir 2 listas para luego ser iteradas de una forma previamente definida

    # print('--->')
    # print(_zip);
    # print(tuple(_zip));
    # (array([ 0.10647826, -0.68292878,  0.        ,  1.        ,  0.        ,  0.        ]), 0)

    for x,y in _zip:

        # print('x ->')
        # print(x)
        # print('y ->')
        # print(y)

        # Pasada hacia adelande (forward pass)

        # producto punto o escala -> un numero
        # producto matricial -> matriz

        # matmul -> producto matricial

        z_matmul = np.matmul(x, entrada_escondida);
        # print('(z_matmul) np.matmul(x, entrada_escondida) ->')
        # print(z_matmul)

        z = sigmoide(z_matmul)
        # print('(z) sigmoide ->')
        # print(z)

        # print('---')
        # print(type(escondida_salida))
        # print(type(z))

        y_ = sigmoide(np.matmul(escondida_salida,z)) # predicción

        # Pasada hacia atrás (backward pass)
        salida_error = (y - y_) * y_ *(1- y_)

        escondida_error = np.dot(salida_error, escondida_salida) * z * (1 -z)

        gradiente_entrada_escondida += escondida_error * x[:,None]
        gradiente_escondida_salida += salida_error * z


    # Actualiza los parámetros (pesos)
    entrada_escondida += alpha * gradiente_entrada_escondida / m
    escondida_salida +=  alpha * gradiente_escondida_salida / m

    if e % (epochs / 10 ) == 0:
        z = sigmoide(np.dot(features.values, entrada_escondida))
        y_ = sigmoide(np.dot(z, escondida_salida))

        # Función de costo
        costo = np.mean(( y_ - targets)**2 )

        if ult_costo  and ult_costo < costo:
            print("Costo de  entrenamiento: ", costo, " ADVERTENCIA -  Costo subiendo")
        else:
            print("Costo de entrenamiento: ", costo )

        ult_costo = costo

#  Precisión en los datos de prueba

print('features_test ->')
print(features_test)

z = sigmoide(np.dot(features_test, entrada_escondida))

print('(z final) ->')
print(z)

y_ = sigmoide(np.dot(z, escondida_salida))

print('(y_ final) ->')
print(y_)

predicciones =  y_ > 0.5

print('predicciones ->')
print(predicciones)

precision = np.mean(predicciones == targets_test)

print('precision ->')
print(precision)

print("Precisión: {:.3f}".format(precision))
