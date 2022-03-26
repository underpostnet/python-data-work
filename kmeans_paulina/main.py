import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import show
from tabulate import tabulate
def D_matrix(b,n,w,x,xe):
    D = np.identity(len(xe))
    for i in range(0,len(xe)):
        D[i,i] = (b/n)*((x/n)**(b-1))*np.exp(w*xe[i]);

    return D
def int_matrix(b,n,w,k,delta,xe):
    L = np.identity(len(xe))
    for i in range(0,5):
        L[i,i] = ( np.exp( ((delta/n)**b)* np.exp(w*xe[i])) )**(k**b - (k+1)**b)

    return np.matrix(L)
def P_matrix(A, delta):
    P = np.identity(len(A))
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if i == j:
                P[i,j] = np.exp(delta*A[i,j])
            elif (j == i + 1) or (j == i-1):
                P[i,j] = np.exp(delta*A[i,j]) -1
    return np.matrix(P)

a = np.matrix([[-2.687, 2.687, 0,0,0],
             [4.015, -7.157, 3.142,0,0],
             [0,8.566,-11.625,3.059,0],
             [0,0,6.378,-12.756,6.378],
             [0,0,0,5.830,-5.830]])
A = a * 10**(-4)

b = 1.78563
n = 21632.3
w = 0.0468681
delta = 10
x = 5000
xe = [0,15,30,55,85]
T = []
for i in range(5,26):
    T.append(i*1000)
valores = []


for t in T:
    k = int(x/delta)
    m = int(t/delta)
    P = P_matrix(A, delta)
    L = np.identity(5)

    for i in range(k,m):
        I = int_matrix(b,n,w,i,delta,xe)
        Li = I*P
        L = L*Li

    R = L.sum(axis=1)
    valores.append(R)

len(valores)


e0 = []
e1 = []
e2 = []
e3 = []
e4 = []
for i in range(0,len(valores)):
    e0.append(valores[i][0])
    e1.append(valores[i][1])
    e2.append(valores[i][2])
    e3.append(valores[i][3])
    e4.append(valores[i][4])
plt.plot(e0, color = "k", alpha = 0.2, label = "State = 0")
# plt.ion()
plt.plot(e1, color = "k", alpha = 0.4, label = "State = 1")
# plt.ion()
plt.plot(e2, color = "k", alpha = 0.6, label = "State = 2")
# plt.ion()
plt.plot(e3, color = "k", alpha = 0.8, label = "State = 3")
# plt.ion()
plt.plot(e4, color = "k", alpha = 1  , label = "State = 4")
plt.legend()

plt.title("Conditional RF for Weibull PHM")
plt.xlabel("Working Age, 1000 h")
plt.ylabel("Reability")
plt.xticks(np.arange(len(valores)),np.arange(5,26,1))

# plt.show() solo jupyter

valores[0] = ["State 0","State 1","State 2","State 3","State 4"]

print(tabulate(valores,
               headers='firstrow',
               tablefmt='fancy_grid',
               stralign='center'))

show()
