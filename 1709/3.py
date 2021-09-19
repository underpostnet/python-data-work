"""
Algoritmo Agrupamiento Jerárquico
"""
import pandas as pd
import matplotlib.pyplot as plt

# https://aprendeia.com/algoritmo-agrupamiento-jerarquico-practica/

import matplotlib.pyplot as plt
from matplotlib.pyplot import show

#### CARGAR LOS DATOS ####
data = pd.read_csv("data/diabetes.csv", sep=",", skip_blank_lines=False)
data=data.mask((  (data==0) & (data.columns != 'Pregnancies') & (data.columns != 'Outcome') )).fillna(data.mean())

### ANALIZAR LOS DATOS ###
#Conocer la forma de los datos
data.shape
#Conocer los datos nulos
data.isnull().sum()
#Conocer el formato de los datos
data.dtypes
### PROCESAMIENTO DE LOS DATOS ###
#Eliminamos las columna Outcome
data = data.drop(['Outcome'], axis = 1)
#Se realiza el escalamiento de los datos
from sklearn import preprocessing
data_escalada = preprocessing.Normalizer().fit_transform(data)
### ANÁLISIS DE MACHINE LEARNING ###
#Se determina las variables a evaluar
X = data_escalada
#Se gráfica el dendrograma para obtener el número de clúster
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(6, 4))
plt.title("Dendrogramas")
dendrograma = shc.dendrogram(shc.linkage(X, method = 'ward'))
show()
