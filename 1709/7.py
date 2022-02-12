# Tratamiento de datos
# ------------------------------------------------------------------------------
import numpy as np
import pandas as pd

# https://www.cienciadedatos.net/documentos/py07_arboles_decision_python.html

# Gráficos
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# Preprocesado y modelado
# ------------------------------------------------------------------------------
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import plot_tree
from sklearn.tree import export_graphviz
from sklearn.tree import export_text
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

# Configuración warnings
# ------------------------------------------------------------------------------
import warnings
warnings.filterwarnings('once')

# Se unen todos los datos (predictores y variable respuesta en un único dataframe)
# boston = load_boston(return_X_y=False)
# datos = np.column_stack((boston.data, boston.target))
# datos = pd.DataFrame(datos,columns = np.append(boston.feature_names, "Outcome"))
data = pd.read_csv('./data/diabetes.csv')
data = data.mask((  (data==0) & (data.columns != 'Pregnancies') & (data.columns != 'Outcome') )).fillna(data.mean())
datos = data;

datos.head(3)

print(datos)



# División de los datos en train y test
# ------------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
                                        datos.drop(columns = "Outcome"),
                                        datos['Outcome'],
                                        random_state = 123
                                    )
# Creación del modelo
# ------------------------------------------------------------------------------
modelo = DecisionTreeRegressor(
            max_depth         = 3,
            random_state      = 123
          )

# Entrenamiento del modelo
# ------------------------------------------------------------------------------
modelo.fit(X_train, y_train)


# Estructura del árbol creado
# ------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 5))

print(f"Profundidad del árbol: {modelo.get_depth()}")
print(f"Número de nodos terminales: {modelo.get_n_leaves()}")

plot = plot_tree(
            decision_tree = modelo,
            feature_names = datos.drop(columns = "Outcome").columns,
            class_names   = 'Outcome',
            filled        = True,
            impurity      = False,
            fontsize      = 10,
            precision     = 2,
            ax            = ax
       )


import matplotlib.pyplot as plt
from matplotlib.pyplot import show

show()


importancia_predictores = pd.DataFrame(
                            {'predictor': datos.drop(columns = "Outcome").columns,
                             'importancia': modelo.feature_importances_}
                            )
print("Importancia de los predictores en el modelo")
print("-------------------------------------------")
importancia_predictores.sort_values('importancia', ascending=False)
print(importancia_predictores)