import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def isNaN(num):
    return num != num

# https://empresas.blogthinkbig.com/python-para-todos-tutorial-de-pca-en-5/

df = pd.read_csv("data/diabetes.csv", sep=",", skip_blank_lines=False)
df=df.mask((  (df==0) & (df.columns != 'Pregnancies') & (df.columns != 'Outcome') )).fillna(df.mean())

# dimension de variables
dim = 8

# Se divide la matriz del dataset en dos partes

X = df.iloc[:,0:dim].values
# la submatriz x contiene los valores de las primeras 8 columnas del dataframe y todas las filas

y = df.iloc[:,dim].values
# El vector y contiene los valores de la 8 columna (outcome) para todas las filas


#Aplicamos una transformación de los datos para poder aplicar las propiedades de la distribución normal
X_std = StandardScaler().fit_transform(X)

# Calculamos la matriz de covarianza
print('NumPy covariance matrix: \n%s' %np.cov(X_std.T))

#Calculamos los autovalores y autovectores de la matriz y los mostramos

cov_mat = np.cov(X_std.T)

eig_vals, eig_vecs = np.linalg.eig(cov_mat)

print('Eigenvectors \n%s' %eig_vecs)
print('\nEigenvalues \n%s' %eig_vals)

#  Hacemos una lista de parejas (autovector, autovalor)
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Ordenamos estas parejas den orden descendiente con la función sort
eig_pairs.sort(key=lambda x: x[0], reverse=True)

# Visualizamos la lista de autovalores en orden desdenciente
print('Autovalores en orden descendiente:')
for i in eig_pairs:
    print(i[0])

# A partir de los autovalores, calculamos la varianza explicada
tot = sum(eig_vals)
var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)] # sorted(eig_vals, reverse=True)
cum_var_exp = np.cumsum(var_exp)

# Representamos en un diagrama de barras la varianza explicada por cada autovalor, y la acumulada
with plt.style.context('seaborn-pastel'):
    plt.figure(figsize=(6, 4))

    plt.bar(range(dim), var_exp, alpha=0.5, align='center',
            label='Varianza individual explicada', color='g')
    plt.step(range(dim), cum_var_exp, where='mid', linestyle='--', label='Varianza explicada acumulada')
    plt.ylabel('Ratio de Varianza Explicada')
    plt.xlabel('Componentes Principales')
    plt.legend(loc='best')
    plt.tight_layout()
    show()


#Generamos la matríz a partir de los pares autovalor-autovector
matrix_w = np.hstack((eig_pairs[0][1].reshape(dim,1),
                      eig_pairs[1][1].reshape(dim,1)))

print('Matriz W:\n', matrix_w)



Y = X_std.dot(matrix_w)



with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 4))
    for lab, col in zip((0,1),
                        ('red', 'blue')
                        ):
        plt.scatter(Y[y==lab, 0],
                    Y[y==lab, 1],
                    label=lab,
                    c=col)
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.legend(loc='lower center')
    plt.tight_layout()
    plt.show()










# end
