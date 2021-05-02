# https://github.com/shreyasibarman/XOR-using-Numpy/blob/master/xorusingnumpy.py

import numpy as np

X= np.array([[0,0],[0,1],[1,0],[1,1]])
Y= np.array([[0,1,1,0]]).T
print ("Input")
print(X)
print ("\nOutput")
print(Y)

m=X.shape[0]
n=X.shape[1]
hidden_s=2
l_r=1

theta1=(np.random.random((n+1,hidden_s)))
theta2=(np.random.random((hidden_s +1,1)))

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_grad(z):
    s=sigmoid(z)
    return s*(1-s)

def forward_propagate(X,theta1,theta2):
    a1=np.c_[np.ones(X.shape[0]),X]
    z1=a1.dot(theta1)
    a2=np.c_[np.ones(X.shape[0]),sigmoid(z1)]
    z3=a2.dot(theta2)
    h3=sigmoid(z3)
    return a1,z1,a2,z3,h3

for i in range(1000):
    a1,z1,a2,z3,hyp=forward_propagate(X,theta1,theta2)
    del_2=Y-hyp
    del_1=del_2.dot(theta2[1:,:].T)
    delta2=del_2
    delta1=del_1*sigmoid_grad(z1)
    theta2+=l_r*a2.T.dot(delta2)
    theta1+=l_r*a1.T.dot(delta1)

print("\nPredicted Output")
print(hyp)
