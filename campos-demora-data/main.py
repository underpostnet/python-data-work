import pandas as pd
import numpy


def isNaN(num):
    return num != num

# ------------------------------------------------
# ------------------------------------------------


df = pd.read_csv("./demora-data.csv", sep=",")  # skip_blank_lines=False

data = []

conjuntos = []


# iterating the columns
headers = []
headerIndex = 0
for col in df.columns:
    headers.append(col)
    if col == 'Demora':
        print(headerIndex)
    headerIndex += 1

print(headers)

for fila, columna in df.iterrows():

    # 6 -> numero de doc
    # 17 -> sociedad

    # columna[20] = columna[20].replace(",", "")

    index = 0
    foundSet = False
    for conjunto in conjuntos:
        if columna[6] == conjunto[0] and columna[17] == conjunto[1]:
            foundSet = True

        if columna[6] == conjunto[0] and columna[17] == conjunto[1] and int(columna[20]) > int(conjunto[2]):
            conjuntos[index][2] = int(columna[20])

        index += 1

    if not foundSet:
        conjuntos.append([
            columna[6],
            columna[17],
            columna[20]
        ])

    data.append(columna)

print(conjuntos)

indexData = 0
for dataObj in data:
    for d in conjuntos:
        if (dataObj[6] == d[0] and dataObj[17] == d[1]):
            data[indexData][20] = int(d[2])

    indexData += 1


data.insert(0, headers)

a = numpy.asarray(data)

numpy.savetxt("demoralista.csv", a, delimiter=";", fmt='%s')
