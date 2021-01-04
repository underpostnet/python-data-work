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

preclam_auc_sensibilidad_bayes_ingenuo = []
preclam_sensibilidad_bayes_ingenuo = []

preclam_auc_sensibilidad_adaboost = []
preclam_sensibilidad_adaboost = []

preclam_auc_sensibilidad_svm = []
preclam_sensibilidad_svm = []

preclam_auc_sensibilidad_j48 = []
preclam_sensibilidad_j48 = []

#prema

prema_auc_sensibilidad_ada = []
prema_sensibilidad_ada = []

prema_auc_sensibilidad_svm = []
prema_sensibilidad_svm = []

prema_auc_sensibilidad_mae = []
prema_sensibilidad_mae = []

prema_auc_sensibilidad_rl = []
prema_sensibilidad_rl = []

prema_auc_sensibilidad_rrmag = []
prema_sensibilidad_rrmag = []

prema_auc_sensibilidad_rrmab = []
prema_sensibilidad_rrmab = []

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

for fila, columna in df.iterrows():

    if columna[0]=='Preeclampsia' and columna[1]=='Bayes ingenuo' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        preclam_auc_sensibilidad_bayes_ingenuo.append(columna[2])
        preclam_sensibilidad_bayes_ingenuo.append(columna[3])
        print('-> 1')

    if columna[0]=='Preeclampsia' and columna[1]=='Adaboost' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        preclam_auc_sensibilidad_adaboost.append(columna[2])
        preclam_sensibilidad_adaboost.append(columna[3])
        print('-> 2')

    if columna[0]=='Preeclampsia' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        preclam_auc_sensibilidad_svm.append(columna[2])
        preclam_sensibilidad_svm.append(columna[3])
        print('-> 3')

    if columna[0]=='Preeclampsia' and columna[1]=='J48' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        preclam_auc_sensibilidad_j48.append(columna[2])
        preclam_sensibilidad_j48.append(columna[3])
        print('-> 4')

    if columna[0]=='Prematurez' and columna[1]=='Autocodificador disperso apilado' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_ada.append(columna[2])
        prema_sensibilidad_ada.append(columna[3])
        print('-> 5')

    if columna[0]=='Prematurez' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_svm.append(columna[2])
        prema_sensibilidad_svm.append(columna[3])
        print('-> 6')

    if columna[0]=='Prematurez' and columna[1]=='Maquina aprendizaje extrema' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_mae.append(columna[2])
        prema_sensibilidad_mae.append(columna[3])
        print('-> 7')

    if columna[0]=='Prematurez' and columna[1]=='Regresion logistica' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_rl.append(columna[2])
        prema_sensibilidad_rl.append(columna[3])
        print('-> 8')

    if columna[0]=='Prematurez' and columna[1]=='RL + RF + MAG continuo' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_rrmag.append(columna[2])
        prema_sensibilidad_rrmag.append(columna[3])
        print('-> 9')

    if columna[0]=='Prematurez' and columna[1]=='RL + RG + MAG binario' and (not isNaN(columna[2])) and (not isNaN(columna[3])):
        prema_auc_sensibilidad_rrmab.append(columna[2])
        prema_sensibilidad_rrmab.append(columna[3])
        print('-> 10')



# AUC v/s sensibilidad, AUC v/s especificidad, AUC v/s precision

print('1:')
print(preclam_auc_sensibilidad_bayes_ingenuo)
print(preclam_sensibilidad_bayes_ingenuo)
print('2:')
print(preclam_auc_sensibilidad_adaboost)
print(preclam_sensibilidad_adaboost)
print('3:')
print(preclam_auc_sensibilidad_svm)
print(preclam_sensibilidad_svm)
print('4:')
print(preclam_auc_sensibilidad_j48)
print(preclam_sensibilidad_j48)
print('5:')
print(prema_auc_sensibilidad_ada)
print(prema_sensibilidad_ada)
print('6:')
print(prema_auc_sensibilidad_svm)
print(prema_sensibilidad_svm)
print('7:')
print(prema_auc_sensibilidad_mae)
print(prema_sensibilidad_mae)
print('8:')
print(prema_auc_sensibilidad_rl)
print(prema_sensibilidad_rl)
print('9:')
print(prema_auc_sensibilidad_rrmag)
print(prema_sensibilidad_rrmag)
print('10:')
print(prema_auc_sensibilidad_rrmab)
print(prema_sensibilidad_rrmab)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.scatter([],
            [],
            c='black',
            label='Preeclampsia',
            marker='v')

plt.scatter(preclam_auc_sensibilidad_bayes_ingenuo,
            preclam_sensibilidad_bayes_ingenuo,
            c='blue',
            label='Bayes Ingenuo',
            marker='v')

plt.scatter(preclam_auc_sensibilidad_adaboost,
            preclam_sensibilidad_adaboost,
            c='red',
            label='Adaboost',
            marker='v')

plt.scatter(preclam_auc_sensibilidad_svm,
            preclam_sensibilidad_svm,
            c='yellow',
            label='SVM',
            marker='v')

plt.scatter(preclam_auc_sensibilidad_j48,
            preclam_sensibilidad_j48,
            c='salmon',
            label='J48',
            marker='v')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.scatter([],
            [],
            c='black',
            label='Prematurez',
            marker='x')

plt.scatter(prema_auc_sensibilidad_ada,
            prema_sensibilidad_ada,
            c='#42bd43',
            label='ADA',
            marker='x')

plt.scatter(prema_auc_sensibilidad_svm,
            prema_sensibilidad_svm,
            c='yellow',
            label='SVM',
            marker='x')

plt.scatter(prema_auc_sensibilidad_mae,
            prema_sensibilidad_mae,
            c='pink',
            label='Maquina aprendizaje extrema',
            marker='x')

plt.scatter(prema_auc_sensibilidad_rl,
            prema_sensibilidad_rl,
            c='#254195',
            label='Regresion logistica',
            marker='x')

plt.scatter(prema_auc_sensibilidad_rrmag,
            prema_sensibilidad_rrmag,
            c='#570553',
            label='RL + RF + MAG continuo',
            marker='x')

plt.scatter(prema_auc_sensibilidad_rrmab,
            prema_sensibilidad_rrmab,
            c='#524e2e',
            label='RL + RG + MAG binario',
            marker='x')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.title(label='AUC v/s sensibilidad')
plt.xlabel("AUC")
plt.ylabel("Sensibilidad")

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.show()
