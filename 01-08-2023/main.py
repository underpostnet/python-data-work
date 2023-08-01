import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Datos de ejemplo con no más de 5 filas
X = np.array([[2, 3],
              [4, 2],
              [1, 5],
              [3, 2],
              [5, 4]])

# Etiquetas de clase correspondientes a los datos
y = np.array([0, 1, 0, 1, 1])

# Crear el modelo SVM
clf = svm.SVC(kernel='linear')

# Ajustar el modelo a los datos de entrenamiento
clf.fit(X, y)

# Coeficientes del hiperplano
coef = clf.coef_[0]
intercept = clf.intercept_[0]

# Imprimir la ecuación del hiperplano (en este caso, solo funcionará para 2 características)
print("Ecuación del hiperplano: {}x + {}y + {} = 0".format(coef[0], coef[1], intercept))

# Plotear los puntos y el hiperplano resultante
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

# Dibujar el hiperplano
plt.xlim(0, 6)
plt.ylim(0, 6)

# Calcular las coordenadas del hiperplano
xx = np.linspace(0, 6)
yy = (-coef[0] / coef[1]) * xx - intercept / coef[1]

# Dibujar el hiperplano
plt.plot(xx, yy, 'k-')

# Resaltar los márgenes
plt.plot(xx, yy + 1 / coef[1], 'k--')
plt.plot(xx, yy - 1 / coef[1], 'k--')

plt.title('SVM con datos de ejemplo')
plt.show()