import numpy as np


import pandas as pd

def isNaN(num):
    return num != num

#------------------------------------------------
#------------------------------------------------

df = pd.read_csv("./data/matriz_distancia.csv", sep=";", skip_blank_lines=False)


matrix = [];

cont_fila = 0
for fila, columna in df.iterrows():
    cont_columna = 0
    fila_ = []
    if cont_fila>0:
        for i in range(len(columna)):
            if cont_columna>0 and cont_fila>0:
                if columna[i]!=-1 and columna[i]!=0 and (cont_columna-1)>0:
                    fila_.append(1)
                else:
                    fila_.append(0)

            cont_columna = cont_columna + 1

    if cont_fila>0:
        matrix.append(fila_)

    cont_fila = cont_fila + 1



print(matrix)

#------------------------------------------------
#------------------------------------------------


import numpy as np

A = np.matrix(matrix)

##Funciones

def columns(c,matrix):
    row, column = matrix.shape
    col = list()
    for i in range(0,row):
        col.append(matrix[i,c])
    return col

def rows(r,matrix):
    row, column = matrix.shape
    fila = list()
    for i in range(0,column):
        fila.append(matrix[r,i])
    return fila

def dominancia(column1,column2):
    large = len(column1)
    cont = 0
    for i in range(0,large):
        if sum(column1) >= sum(column2) and  column1[i] >= column2[i]:
            cont += 1
    if cont == large:
        return True

def delete_equal_column(c,matrix):
    column = matrix.shape[1]
    cont = 0
    for j in range(0,column):
        if c!=j and columns(c,matrix) == columns(j,matrix):
            new_matrix = np.delete(matrix, j, axis=1)
            cont += 1
    if cont == 0:
        new_matrix = matrix
    return new_matrix

def delete_equal_row(r,matrix):
    row = matrix.shape[0]
    cont = 0
    for j in range(0,row):
        if r!=j and rows(r,matrix) == rows(j,matrix):
            new_matrix = np.delete(matrix, j, axis=0)
            cont += 1
    if cont == 0:
        new_matrix = matrix
    return new_matrix

def delete_row(c,matrix):
    row, column = matrix.shape
    cont = 0
    if sum(rows(c,matrix)) == 1:
        for j in range(0,column):
            if rows(c,matrix)[j] == 1:
                for i in range(0,row):
                    if i!=c and rows(j,matrix)[j] == 1:
                        new_matrix = np.delete(matrix, j, axis=0)
                        cont +=1
    if cont == 0:
        new_matrix = matrix
    return new_matrix

##Codigo reducción de Columnas

print("Matriz original: \n",A)

column = A.shape[1]
i = 0
while i!= column:
    for j in range(0,column):
        A = delete_equal_column(i,A)
    column = A.shape[1]
    i +=1

print("Matriz sin columnas repetidas: \n",A)

column = A.shape[1]

aux = set()
for i in range(0,column):
    for j in range(0,column):
        if i!=j and dominancia(columns(i,A),columns(j,A)):
            aux.add(j)

A = np.delete(A, list(aux), axis=1)
print("Matriz sin columnas dominadas: \n",A)

##Código reducción de filas

column = A.shape[1]
i = 0
while i!= column:
    for j in range(0,column):
        A = delete_equal_row(j,A)
    column = A.shape[0]
    i +=1

print("Matriz sin filas repetidas: \n",A)

row, column = A.shape
aux = set()
var = set()
for i in range(0,row):
    if sum(rows(i,A)) == 1:
        for j in range(0,column):
            if rows(i,A)[j] == 1:
                var.add(j)
                for e in range(0,row):
                    if rows(e,A)[j] == 1:
                        aux.add(e)


A = np.delete(A, list(aux), axis=0)
print("Matriz sin variables iguales a 1: \n",A)
print("Variables iguales a 1:",var)





#------------------------------------------------
#------------------------------------------------
























#------------------------------------------------
#------------------------------------------------
