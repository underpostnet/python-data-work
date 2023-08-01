import numpy as np
from sklearn.svm import SVC

# Datos de entrada
X = np.array([[0.1, 0.5, 0.6, 0.2],
              [0.5, 0.7, 0.2, 0.8],
              [0.2, 0.1, 0.7, 0.9],
              [0.6, 0.9, 0.8, 0.4],
              [0.3, 0.4, 0.5, 0.1]])

# Datos de salida
y = np.array([1, 1, 0, 0, 1])

# Crear el clasificador SVM
svm_classifier = SVC(kernel='linear')

# Entrenar el clasificador SVM
svm_classifier.fit(X, y)

# Datos de prueba para predecir
X_prueba = np.array([[0.4, 0.3, 0.6, 0.7],
                     [0.7, 0.8, 0.3, 0.2]])

# Realizar predicciones
predicciones = svm_classifier.predict(X_prueba)

# Imprimir las predicciones
print("Predicciones:", predicciones)
