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

preclam_auc_preci_bayes_ingenuo = []
preclam_preci_bayes_ingenuo = []

preclam_auc_preci_svm = []
preclam_preci_svm = []

preclam_auc_preci_j48 = []
preclam_preci_j48 = []

#prema

prema_auc_preci_ada = []
prema_preci_ada = []

prema_auc_preci_svm = []
prema_preci_svm = []

prema_auc_preci_mae = []
prema_preci_mae = []

prema_auc_preci_svmrf = []
prema_preci_svmrf = []

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

for fila, columna in df.iterrows():

    if columna[0]=='Preeclampsia' and columna[1]=='Bayes ingenuo' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        preclam_auc_preci_bayes_ingenuo.append(columna[2])
        preclam_preci_bayes_ingenuo.append(columna[5])
        print('-> 1')

    if columna[0]=='Preeclampsia' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        preclam_auc_preci_svm.append(columna[2])
        preclam_preci_svm.append(columna[5])
        print('-> 3')

    if columna[0]=='Preeclampsia' and columna[1]=='J48' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        preclam_auc_preci_j48.append(columna[2])
        preclam_preci_j48.append(columna[5])
        print('-> 4')

    if columna[0]=='Prematurez' and columna[1]=='Autocodificador disperso apilado' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        prema_auc_preci_ada.append(columna[2])
        prema_preci_ada.append(columna[5])
        print('-> 5')

    if columna[0]=='Prematurez' and columna[1]=='SVM' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        prema_auc_preci_svm.append(columna[2])
        prema_preci_svm.append(columna[5])
        print('-> 6')

    if columna[0]=='Prematurez' and columna[1]=='Maquina aprendizaje extrema' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        prema_auc_preci_mae.append(columna[2])
        prema_preci_mae.append(columna[5])
        print('-> 7')

    if columna[0]=='Prematurez' and columna[1]=='SVM + RF' and (not isNaN(columna[2])) and (not isNaN(columna[5])):
        prema_auc_preci_svmrf.append(columna[2])
        prema_preci_svmrf.append(columna[5])
        print('-> 11')


# AUC v/s sensibilidad, AUC v/s especificidad, AUC v/s precision

print('1:')
print(preclam_auc_preci_bayes_ingenuo)
print(preclam_preci_bayes_ingenuo)
print('3:')
print(preclam_auc_preci_svm)
print(preclam_preci_svm)
print('4:')
print(preclam_auc_preci_j48)
print(preclam_preci_j48)
print('5:')
print(prema_auc_preci_ada)
print(prema_preci_ada)
print('6:')
print(prema_auc_preci_svm)
print(prema_preci_svm)
print('7:')
print(prema_auc_preci_mae)
print(prema_preci_mae)
print('11:')
print(prema_auc_preci_svmrf)
print(prema_preci_svmrf)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.scatter([],
            [],
            c='black',
            label='Preeclampsia',
            marker='v')

plt.scatter(preclam_auc_preci_bayes_ingenuo,
            preclam_preci_bayes_ingenuo,
            c='blue',
            label='Bayes Ingenuo',
            marker='v')

plt.scatter(preclam_auc_preci_svm,
            preclam_preci_svm,
            c='yellow',
            label='SVM',
            marker='v')

plt.scatter(preclam_auc_preci_j48,
            preclam_preci_j48,
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

plt.scatter(prema_auc_preci_ada,
            prema_preci_ada,
            c='#42bd43',
            label='ADA',
            marker='x')

plt.scatter(prema_auc_preci_svm,
            prema_preci_svm,
            c='yellow',
            label='SVM',
            marker='x')

plt.scatter(prema_auc_preci_mae,
            prema_preci_mae,
            c='pink',
            label='Maquina aprendizaje extrema',
            marker='x')

plt.scatter(prema_auc_preci_svmrf,
            prema_preci_svmrf,
            c='red',
            label='SVM + RF',
            marker='x')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.title(label='AUC v/s Precisión')
plt.xlabel("AUC")
plt.ylabel("Precisión")

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.show()
