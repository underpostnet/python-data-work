import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import show


df = pd.read_csv("data.csv", sep=";", skip_blank_lines=False)

# print(df)

data = []

for fila, columna in df.iterrows():
    # if fila==1:
    fila = []
    for i in range(len(columna)):
        fila.append(columna[i])

    data.append(fila)

print(data)


a = []
b = []
c = []
d = []
e = []


# Semana Gestacional;Semana gestacional;Talla;Peso 1er Trimestre;IMC 1er Trimestre
#   0                            1        2          3               4

for i_ in data:
    a.append(i_[0])
    b.append(i_[1])
    c.append(i_[2])
    d.append(i_[3])
    e.append(i_[4])
    
    
fig, ax = plt.subplots()



l1 = ax.scatter(a, e, color='red')
l2 = ax.scatter(a, d, color='blue')
l3 = ax.scatter(b, e, color='yellow')
l4 = ax.scatter(b, d, color='magenta')


# plt.title("title")

plt.legend((l1, l2, l3, l4),
           ('a', 'b', 'c', 'd'),
           scatterpoints=1,
           loc='lower left',
           ncol=3,
           fontsize=8)


plt.xlabel('a')
plt.ylabel('b')



show()
