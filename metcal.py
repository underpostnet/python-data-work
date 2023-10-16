# coding=utf-8

import pandas as pd
import csv


def isNaN(num):
    return num != num


df = pd.read_csv("calculo-met-ppaq.csv", sep=";", skip_blank_lines=False)

data = []

# Menos de media hora al día : * 0.15
# De media hora a 1 hora al día : * 0.45
# De 1 a 2 horas al día : * 1.5
# De 2 a 3 horas al día : *2.5
# Más de 3 horas al día : *4
# Ninguno: 0

with open('output.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')

    index = 0
    for row, col in df.iterrows():
        row = []
        for i in range(len(col)):
            if index > 0:
                if col[i] == "Menos de media hora al día":
                    col[i] = float(data[0][i]) * 0.15

                if col[i] == "De 1 a 2 horas al día":
                    col[i] = float(data[0][i]) * 0.45

                if col[i] == "De media hora a 1 hora al día":
                    col[i] = float(data[0][i]) * 1.5

                if col[i] == "De 2 a 3 horas al día":
                    col[i] = float(data[0][i]) * 2.5

                if col[i] == "Más de 3 horas al día":
                    col[i] = float(data[0][i]) * 4
                    
                if col[i] == "Ninguno":
                    col[i] = float(data[0][i]) * 0
            
            row.append(col[i])

        data.append(row)
        writer.writerow(row)

        index += 1


# print(data)
