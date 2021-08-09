

import pandas as pd

def isNaN(num):
    return num != num

df = pd.read_csv("diabetes_data_upload.csv", sep=",", skip_blank_lines=False)

data = []
result = []

for row, column in df.iterrows():
    row = []

    # for i in range(len(column)):
    #     row.append(column[i])


    if column[1]=='Male':
        row.append(1)
    else:
        row.append(0)


    for i in range(2, 15):
        if column[i]=='Yes':
            row.append(1)
        else:
            row.append(0)


    if column[16]=='Positive':
        result.append(1)
    else:
        result.append(0)


    data.append(row)



print(len(data))
print(len(result))


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) -> arr.shape -> (2,4)


import numpy as np

X= np.array(data)
Y= np.array(result).T
print ("Input")
print(X)
print ("\nOutput")
print(Y)

m=X.shape[0]
n=X.shape[1]

hidden_s=len(data)
l_r=6

# theta1=(np.random.random( ( len(data)+1 , len(data[0]) ) ))
theta1=(np.random.random( ( n+1 , len(data) ) ))
theta2=(np.random.random( ( len(data)+1 , 1 ) ))

print('theta1 ->')
print(len(theta1))
print(len(theta1[0]))
print('theta2 ->')
print(len(theta2))

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

















# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------







# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
