import pandas as pd
import seaborn as sns

# https://interactivechaos.com/es/manual/tutorial-de-machine-learning/ejemplo-con-t-sne

data = pd.read_csv("data/diabetes.csv", sep=",", skip_blank_lines=False)
data=data.mask((  (data==0) & (data.columns != 'Pregnancies') & (data.columns != 'Outcome') )).fillna(data.mean())


# A continuación, importamos el algoritmo y lo instanciamos:

from sklearn.manifold import TSNE
tsne = TSNE(random_state = 0)

# Lo entrenamos y transformamos los datos iniciales:

data_t = tsne.fit_transform(data.drop("Outcome", axis = 1))

# Por último, mostramos los datos resultantes en una gráfica:

import matplotlib.pyplot as plt
from matplotlib.pyplot import show

sns.scatterplot(data_t[:, 0], data_t[:, 1], hue = data.Outcome);
show()

# Obsérvese, en todo caso, lo mucho que puede cambiar la visualización
# escogiendo unos parámetros diferentes:

tsne = TSNE(perplexity = 9, early_exaggeration = 11, learning_rate = 451, random_state = 0)
data_t = tsne.fit_transform(data.drop("Outcome", axis = 1))
sns.scatterplot(data_t[:, 0], data_t[:, 1], hue = data.Outcome);
show()









# end
