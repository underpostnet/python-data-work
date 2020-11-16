
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import show


Exp1=np.loadtxt('data/Exp1a.csv', delimiter=",", skiprows=1)
Exp2=np.loadtxt('data/Exp2a.csv', delimiter=",", skiprows=1)
Exp3=np.loadtxt('data/Exp3a.csv', delimiter=",", skiprows=1)
Exp4=np.loadtxt('data/Exp4a.csv', delimiter=",", skiprows=1)
Exp5=np.loadtxt('data/Exp5a.csv', delimiter=",", skiprows=1)


#Exp1
Tiempo1=Exp1[:,0]
Voltaje1=Exp1[:,1:]
Vmáx1=np.max(Voltaje1,axis=0)
Lbase1T0=Voltaje1[0]
Lbase1T60=Voltaje1[60]
LB1=((Lbase1T0+Lbase1T60)/2)
LB1a=np.array(LB1)
AmpPSP1=Vmáx1-LB1a
unos=np.ones_like(LB1a)

#Exp2
Tiempo2=Exp2[:,0]
Voltaje2=Exp2[:,1:]
Vmáx2=np.max(Voltaje2,axis=0)
Lbase2T0=Voltaje2[0]
Lbase2T60=Voltaje2[60]
LB2=((Lbase2T0+Lbase2T60)/2)
LB2a=np.array(LB2)
AmpPSP2=Vmáx2-LB2a
dos=np.ones_like(LB2a)*2

#Exp3
Tiempo3=Exp3[:,0]
Voltaje3=Exp3[:,1:]
Vmáx3=np.max(Voltaje3,axis=0)
Lbase3T0=Voltaje3[0]
Lbase3T60=Voltaje3[60]
LB3=((Lbase3T0+Lbase3T60)/2)
LB3a=np.array(LB3)
AmpPSP3=Vmáx3-LB3a
tres=np.ones_like(LB3a)*3

#Exp4
Tiempo4=Exp4[:,0]
Voltaje4=Exp4[:,1:]
Vmáx4=np.max(Voltaje4,axis=0)
Lbase4T0=Voltaje4[0]
Lbase4T60=Voltaje4[60]
LB4=((Lbase4T0+Lbase4T60)/2)
LB4a=np.array(LB4)
AmpPSP4=Vmáx4-LB4a
cuatros=np.ones_like(LB4a)*4

#Exp5
Tiempo5=Exp5[:,0]
Voltaje5=Exp5[:,1:]
Vmáx5=np.max(Voltaje5,axis=0)
Lbase5T0=Voltaje5[0]
Lbase5T60=Voltaje5[60]
LB5=((Lbase5T0+Lbase5T60)/2)
LB5a=np.array(LB5)
AmpPSP5=Vmáx5-LB5a
cincos=np.ones_like(LB5a)*5

#Plots

LBData={'1':LB1a,'2':LB2a,'3':LB3a,'4':LB4a,'5':LB5a}
PSPdata= {'1':AmpPSP1,'2':AmpPSP2,'3':AmpPSP3,'4':AmpPSP4,'5':AmpPSP5}
unos_ = {'unos': unos, 'dos': dos, 'tres': tres, 'cuatros': cuatros, 'cincos': cincos}

dodgerblue_diamond = dict(markerfacecolor='dodgerblue', marker='D')
fig, ax = plt.subplots()
ax.boxplot(LBData.values(), flierprops=dodgerblue_diamond)
plt.plot(unos,LB1a,color='dodgerblue',marker='D')
plt.plot(dos,LB2a,color='orange',marker='D')
plt.plot(tres,LB3a,color='limegreen',marker='D')
plt.plot(cuatros,LB4a,color='red',marker='D')
plt.plot(cincos,LB5a,color='mediumpurple',marker='D')
ax.set_xticklabels(LBData.keys())
plt.ylabel("Baseline voltage (mV)")
plt.xlabel("Condition")
show()

fig, ax = plt.subplots()
ax.boxplot(PSPdata.values(), flierprops=dodgerblue_diamond)
plt.plot(unos,AmpPSP1,color='dodgerblue',marker='D')
plt.plot(dos,AmpPSP2,color='orange',marker='D')
plt.plot(tres,AmpPSP3,color='limegreen',marker='D')
plt.plot(cuatros,AmpPSP4,color='red',marker='D')
plt.plot(cincos,AmpPSP5,color='mediumpurple',marker='D')
plt.ylabel("PSP amplitude (mV)")
plt.xlabel("Condition")
ax.set_xticklabels(PSPdata.keys())
show()
