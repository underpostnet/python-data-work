import numpy as np
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


df = pd.read_csv("data/BBDD-OB-CON-VARIABLES-MODIFICADAS.CSV.csv",
                 sep=",", skip_blank_lines=False, low_memory=False)

# data = df.iloc[:,[1,3,4,5,8,14,15,18,19,20,21,22,23,24,25,26]].values

data = df.loc[:, ['Edad', 'OB', 'E', 'I',
                  'Paridad', 'AñosEscolaridad', 'TIENEONO']]

train, test = train_test_split(data, test_size=0.2)

print('x_train', train)
print('y_train', test)


x_train = train.loc[:, ['Edad', 'OB', 'E', 'I',
                  'Paridad', 'AñosEscolaridad']]

y_train = (train['TIENEONO'] == 1)

print('x_train', x_train)
print('y_train', y_train)

# Crear el clasificador SVM
svm_classifier = SVC(kernel='linear')

# Entrenar el clasificador SVM
svm_classifier.fit(x_train, y_train)

# Datos de prueba para predecir
x_test = test.loc[:, ['Edad', 'OB', 'E', 'I',
                  'Paridad', 'AñosEscolaridad']]

# Realizar predicciones
predicciones = svm_classifier.predict(x_test)

# Imprimir las predicciones
print("Predicciones:", predicciones)

for i in predicciones:
    print(i)
