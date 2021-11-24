

import pandas as pd

def isNaN(num):
    return num != num

df = pd.read_csv("datos_.csv", sep=";", skip_blank_lines=False)


x_data = []
trial = []
fail = []

for row, column in df.iterrows():


    x_data.append(column[1])
    trial.append(column[0])
    fail.append(column[2])

print(x_data)
print(trial)
print(len(x_data))
print(len(trial))

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show

df = pd.DataFrame({
    'x1': trial,
    'x2': x_data
})

np.random.seed(200)
# Número de centroides k = 3
k = 3
# Inicializamos los centroides a valores aleatorios en el espacio de datos
centroids = {
    i+1: [np.random.randint(0, 30), np.random.randint(2500, 6000)]
    for i in range(k)
}

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x1'], df['x2'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title(u'Los k centroides están inicializados')
# plt.xlim(0, 80)
# plt.ylim(0, 25)

show()

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


## Asignación de las observaciones a los centroides

def asignacion(df, centroids):
    for i in centroids.keys():
        # sqrt((x1 - c1)^2 - (x2 - c2)^2)
        df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x1'] - centroids[i][0]) ** 2
                + (df['x2'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = asignacion(df, centroids)

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x1'], df['x2'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title(u'Asignación de los datos al clúster del centroide más cercano')
# plt.xlim(0, 80)
# plt.ylim(0, 80)
show()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


## Actualización de los centroides

import copy

old_centroids = copy.deepcopy(centroids)

def update(k):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x1'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['x2'])
    return k

centroids = update(centroids)

fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x1'], df['x2'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title(u'Actualización de los centroides como la media de los datos del clúster')
# plt.xlim(0, 80)
# plt.ylim(0, 80)
for i in old_centroids.keys():
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])

show()







# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


## Repetición de la asignación de las observaciones al centroide más cercano

df = asignacion(df, centroids)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# calcular vlaor mayor de cada cluster

# print(df)

data_fix = np.array(df);
data_r = [];
data_g = [];
data_b = [];

for d_ in data_fix:

    if d_[6]=='g':
        data_b.append(d_[1])

    if d_[6]=='r':
        data_g.append(d_[1])

    if d_[6]=='b':
        data_r.append(d_[1])


print(" max g ->")
print(max(data_g))

print(" max b ->")
print(max(data_b))

print(" max r ->")
print(max(data_r))

limit_ = [max(data_g), max(data_b), max(data_r)]

limit_ = sorted(limit_, reverse=False)

print("order limit ->")
print(limit_)

states = []
for d_ in data_fix:

    if d_[1] <= limit_[0]:
        states.append(1)
    elif d_[1] > limit_[0] and d_[1] <= limit_[1]:
        states.append(2)
    else:
        states.append(3)


df['States'] = states




data_fix = np.array(df);
next_column = []
f_ = False;
for d_ in data_fix:
    if f_:
        next_column.append(d_[7])
    if not f_:
        f_ = True

next_column.append(0)

df['Nex States'] = next_column


data_fix = np.array(df);

#   1 - 1    1 - 2    1 - 3
#   2 - 1    2 - 2    2 - 3
#   3 - 1    3 - 2    3 - 3

dim_ = 3
final_matrix = []

for x_ in range(1, dim_+1):
    case = []
    for y_ in range(1, dim_+1):
        sum = 0
        for d_ in data_fix:
            if d_[7]==x_ and d_[8]==y_:
                sum += 1

        case.append(sum)

    final_matrix.append(case)


print(" sum matrix change ->")
print(np.array(final_matrix))

df['fail'] = fail

f_1 = 0
f_2 = 0
f_3 = 0
data_fix = np.array(df);

for d_ in data_fix:

    if d_[7] == 1:
        f_1 += d_[9]

    if d_[7] == 2:
        f_2 += d_[9]

    if d_[7] == 3:
        f_3 += d_[9]

print(" f1 -> ")
print(f_1)
print(" f2 -> ")
print(f_2)
print(" f3 -> ")
print(f_3)


matrix_dix = []
for x_ in range(0, dim_):
    case = []
    for y_ in range(0, dim_):
        if x_ != y_:
            if x_ == 0:
                case.append(final_matrix[x_][y_]/f_1)

            if x_ == 1:
                case.append(final_matrix[x_][y_]/f_2)

            if x_ == 2:
                case.append(final_matrix[x_][y_]/f_3)
        else:
            case.append(0)

    matrix_dix.append(case);

print(" matrix div ->")

matrix_dix[0][0] = -1*(matrix_dix[0][1] + matrix_dix[0][2])
matrix_dix[1][1] = -1*(matrix_dix[1][0] + matrix_dix[1][2])
matrix_dix[2][2] = -1*(matrix_dix[2][0] + matrix_dix[2][1])

from math import e

for x_ in range(0, dim_):
    case = []
    for y_ in range(0, dim_):
        if x_ != y_:
            matrix_dix[x_][y_] = (e**matrix_dix[x_][y_]) - 1
        else:
            matrix_dix[x_][y_] = (e**matrix_dix[x_][y_])



print(np.array(matrix_dix))

print(df)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# Representación de resultados
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x1'], df['x2'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title(u'Repetición de la asignación de las observaciones al centroide más cercano')


# plt.xlim(0, 80)
# plt.ylim(0, 80)


show()




print(centroids)




# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
