import pandas as pd
import numpy


def isNaN(num):
    return num != num

#------------------------------------------------
#------------------------------------------------

df = pd.read_csv("./demora-data.csv", sep=",") # skip_blank_lines=False

#print(df)

data = []


for fila, columna in df.iterrows():

    # 6 -> numero de doc
    # 17 -> sociedad

    fila = [] # arreglo 

    for i in range(len(columna)):

        fila.append(columna[i])


    data.append(fila)

conjuntos = []

for columna in data:

    for c in conjuntos:

        if c[0]==columna[6] and c[1]==columna[17] and int(c[2]) > int(c[20]):
            c[2] = int(c[20])
        else:
            conjunto = [
                columna[6],
                columna[17],
                int(c[20])
            ] # objeto
            conjuntos.append(conjunto)


for dataObj in data:
    for d in conjuntos:
        if(dataObj[6]==d[0] and dataObj[17]==d[1]):
            dataObj[20] = d[2]

a = numpy.asarray(data)

numpy.savetxt("demoralista.csv", a, delimiter=";",fmt='%s')