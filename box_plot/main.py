
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import show

# https://pro.arcgis.com/es/pro-app/help/analysis/geoprocessing/charts/box-plot.htm

datos=np.loadtxt('data/Exp1a.csv', delimiter=",", skiprows=1)
tiempo1=datos[:,0]
volt1=datos[:,1:]
lineabase1=datos[0,1:]
lineabas1=datos[60,1:]
LB1=((lineabas1+lineabase1)/2)
LiB1=np.array(LB1)
# segundo plot
Maximos1=np.max(volt1,0)
PSP1=Maximos1-LiB1
unos1=np.ones_like(LiB1)

datos=np.loadtxt('data/Exp2a.csv', delimiter=",", skiprows=1)
tiempo2=datos[:,0]
volt2=datos[:,1:]
lineabase2=datos[0,1:]
lineabas2=datos[60,1:]
LB2=((lineabas2+lineabase2)/2)
LiB2=np.array(LB2)
# segundo plot
Maximos2=np.max(volt2,0)
PSP2=Maximos2-LiB2
unos2=np.ones_like(LiB2)

datos=np.loadtxt('data/Exp3a.csv', delimiter=",", skiprows=1)
tiempo3=datos[:,0]
volt3=datos[:,1:]
lineabase3=datos[0,1:]
lineabas3=datos[60,1:]
LB3=((lineabas3+lineabase3)/2)
LiB3=np.array(LB3)
# segundo plot
Maximos3=np.max(volt3,0)
PSP3=Maximos3-LiB3
unos3=np.ones_like(LiB3)


datos=np.loadtxt('data/Exp4a.csv', delimiter=",", skiprows=1)
tiempo4=datos[:,0]
volt4=datos[:,1:]
lineabase4=datos[0,1:]
lineabas4=datos[60,1:]
LB4=((lineabas4+lineabase4)/2)
LiB4=np.array(LB4)
# segundo plot
Maximos4=np.max(volt4,0)
PSP4=Maximos4-LiB4
unos4=np.ones_like(LiB4)

datos=np.loadtxt('data/Exp5a.csv', delimiter=",", skiprows=1)
tiempo5=datos[:,0]
volt5=datos[:,1:]
lineabase5=datos[0,1:]
lineabas5=datos[60,1:]
LB5=((lineabas5+lineabase5)/2)
LiB5=np.array(LB5)
# segundo plot
Maximos5=np.max(volt5,0)
PSP5=Maximos5-LiB5
unos5=np.ones_like(LiB5)





my_dict = {'Exp1a.csv': LiB1, 'Exp2a.csv': LiB2, 'Exp3a.csv': LiB3, 'Exp4a.csv': LiB4, 'Exp5a.csv': LiB5}
PS = {'P1':PSP1,'P2':PSP2,'P3':PSP3,'P4':PSP4,'P5':PSP5}
un_ = {'unos1': unos1, 'unos2': unos2, 'unos3': unos3, 'unos4': unos4, 'unos5': unos5}


# paint out points
dodgerblue_diamond = dict(markerfacecolor='dodgerblue', marker='D')

# ax.plot(un_.values(), my_dict.values(),color='dodgerblue',marker='D')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

fig, ax = plt.subplots()
ax.boxplot(my_dict.values(), flierprops=dodgerblue_diamond)
ax.set_xticklabels(my_dict.keys())
plt.ylabel("Baseline voltage (mV)")
plt.xlabel("Condition")
show()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

fig, ax = plt.subplots()
ax.boxplot(PS.values(), flierprops=dodgerblue_diamond)
plt.ylabel("Baseline voltage (mV)")
plt.xlabel("Condition")
ax.set_xticklabels(my_dict.keys())
show()
