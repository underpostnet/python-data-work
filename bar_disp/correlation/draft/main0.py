import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import pandas as pd

def isNaN(num):
    return num != num

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

df = pd.read_csv("data.csv", sep=";", skip_blank_lines=False)

print(df)

#preclam

preclam_auc_especificidad_bayes_ingenuo = []
preclam_especificidad_bayes_ingenuo = []

preclam_auc_especificidad_adaboost = []
preclam_especificidad_adaboost = []

preclam_auc_especificidad_svm = []
preclam_especificidad_svm = []

preclam_auc_especificidad_j48 = []
preclam_especificidad_j48 = []

#prema

prema_auc_especificidad_ada = []
prema_especificidad_ada = []

prema_auc_especificidad_svm = []
prema_especificidad_svm = []

prema_auc_especificidad_mae = []
prema_especificidad_mae = []

prema_auc_especificidad_rl = []
prema_especificidad_rl = []

prema_auc_especificidad_rrmag = []
prema_especificidad_rrmag = []

prema_auc_especificidad_rrmab = []
prema_especificidad_rrmab = []

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

for fila, columna in df.iterrows():

    if columna[0]=='Preeclampsia' and columna[1]=='Bayes ingenuo' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        preclam_auc_especificidad_bayes_ingenuo.append(columna[2])
        preclam_especificidad_bayes_ingenuo.append(columna[4])
        print('-> 1')

    if columna[0]=='Preeclampsia' and columna[1]=='Adaboost' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        preclam_auc_especificidad_adaboost.append(columna[2])
        preclam_especificidad_adaboost.append(columna[4])
        print('-> 2')

    if columna[0]=='Preeclampsia' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        preclam_auc_especificidad_svm.append(columna[2])
        preclam_especificidad_svm.append(columna[4])
        print('-> 3')

    if columna[0]=='Preeclampsia' and columna[1]=='J48' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        preclam_auc_especificidad_j48.append(columna[2])
        preclam_especificidad_j48.append(columna[4])
        print('-> 4')

    if columna[0]=='Prematurez' and columna[1]=='Autocodificador disperso apilado' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_ada.append(columna[2])
        prema_especificidad_ada.append(columna[4])
        print('-> 5')

    if columna[0]=='Prematurez' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_svm.append(columna[2])
        prema_especificidad_svm.append(columna[4])
        print('-> 6')

    if columna[0]=='Prematurez' and columna[1]=='Maquina aprendizaje extrema' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_mae.append(columna[2])
        prema_especificidad_mae.append(columna[4])
        print('-> 7')

    if columna[0]=='Prematurez' and columna[1]=='Regresion logistica' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_rl.append(columna[2])
        prema_especificidad_rl.append(columna[4])
        print('-> 8')

    if columna[0]=='Prematurez' and columna[1]=='RL + RF + MAG continuo' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_rrmag.append(columna[2])
        prema_especificidad_rrmag.append(columna[4])
        print('-> 9')

    if columna[0]=='Prematurez' and columna[1]=='RL + RG + MAG binario' and (not isNaN(columna[2])) and (not isNaN(columna[4])):
        prema_auc_especificidad_rrmab.append(columna[2])
        prema_especificidad_rrmab.append(columna[4])
        print('-> 10')



# AUC v/s sensibilidad, AUC v/s especificidad, AUC v/s precision

print('1:')
print(preclam_auc_especificidad_bayes_ingenuo)
print(preclam_especificidad_bayes_ingenuo)
print('2:')
print(preclam_auc_especificidad_adaboost)
print(preclam_especificidad_adaboost)
print('3:')
print(preclam_auc_especificidad_svm)
print(preclam_especificidad_svm)
print('5:')
print(prema_auc_especificidad_ada)
print(prema_especificidad_ada)
print('6:')
print(prema_auc_especificidad_svm)
print(prema_especificidad_svm)
print('7:')
print(prema_auc_especificidad_mae)
print(prema_especificidad_mae)
print('8:')
print(prema_auc_especificidad_rl)
print(prema_especificidad_rl)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.scatter([],
            [],
            c='black',
            label='Preeclampsia',
            marker='v')

plt.scatter(preclam_auc_especificidad_bayes_ingenuo,
            preclam_especificidad_bayes_ingenuo,
            c='blue',
            label='Bayes Ingenuo',
            marker='v')

plt.scatter(preclam_auc_especificidad_adaboost,
            preclam_especificidad_adaboost,
            c='red',
            label='Adaboost',
            marker='v')

plt.scatter(preclam_auc_especificidad_svm,
            preclam_especificidad_svm,
            c='yellow',
            label='SVM',
            marker='v')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.scatter([],
            [],
            c='black',
            label='Prematurez',
            marker='x')

plt.scatter(prema_auc_especificidad_ada,
            prema_especificidad_ada,
            c='#42bd43',
            label='ADA',
            marker='x')

plt.scatter(prema_auc_especificidad_svm,
            prema_especificidad_svm,
            c='yellow',
            label='SVM',
            marker='x')

plt.scatter(prema_auc_especificidad_mae,
            prema_especificidad_mae,
            c='pink',
            label='Maquina aprendizaje extrema',
            marker='x')

plt.scatter(prema_auc_especificidad_rl,
            prema_especificidad_rl,
            c='#254195',
            label='Regresion logistica',
            marker='x')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.title(label='AUC v/s especificidad')
plt.xlabel("AUC")
plt.ylabel("Especificidad")

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.show()
