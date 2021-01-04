import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import pandas as pd

def isNaN(num):
    return num != num

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

df = pd.read_csv("data.csv", sep=";", skip_blank_lines=False)

print(df)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

conjunto_ml = []
conjunto_ml_color = []

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

for fila, columna in df.iterrows():

    add = True

    for ml in conjunto_ml:
        if ml == columna[1]:
            add = False

    if add:
        conjunto_ml.append(columna[1])

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

from random import randint

for i in range(len(conjunto_ml)):
    conjunto_ml_color.append('#%06X' % randint(0, 0xFFFFFF))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

conjunto_pre = ['Preeclampsia', 'Prematurez']
conjunto_pre_marker = ['v','x']

plt.scatter([],
            [],
            c='white',
            label=' ',
            marker='')

plt.scatter([],
            [],
            c='black',
            label='Preeclampsia',
            marker='v')

plt.scatter([],
            [],
            c='black',
            label='Prematurez',
            marker='x')

plt.scatter([],
            [],
            c='white',
            label=' ',
            marker='')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

for fila, columna in df.iterrows():

    ind_pre = -1
    for pre in conjunto_pre:
        ind_pre = ind_pre + 1
        if pre == columna[0]:
            ind_ml = -1
            for ml in conjunto_ml:
                ind_ml = ind_ml + 1
                if (ml == columna[1]) and (not isNaN(columna[2])) and (not isNaN(columna[3])):
                    plt.scatter([columna[2]],
                                [columna[3]],
                                c=conjunto_ml_color[ind_ml],
                                label=conjunto_ml[ind_ml],
                                marker=conjunto_pre_marker[ind_pre])



plt.scatter([],
            [],
            c='white',
            label=' ',
            marker='')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.xticks.html
# https://matplotlib.org/3.3.3/gallery/pyplots/axline.html#sphx-glr-gallery-pyplots-axline-py
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.axhline.html
# https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.axes.Axes.axvline.html

tick = []
n = 5

for i in range(n):
    tick.append((1/(n-1))*i)

plt.xticks(tick)
plt.yticks(tick)

plt.axhline(y=0.5, color="gray", linestyle="-.")
plt.axvline(x=0.5, color="gray", linestyle="-.")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.title(label='AUC v/s sensibilidad')
plt.xlabel("AUC")
plt.ylabel("Sensibilidad")

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.show()


















#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
