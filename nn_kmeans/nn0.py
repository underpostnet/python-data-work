

import pandas as pd
import numpy as np

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


    for i in range(2, 16):
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

# Back-Propagation Neural Networks
#
import math
import random
# from data_prep import pat_training, pat_test

random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no

        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error


    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=1000, N=0.05, M=0.01):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                print('error %-.5f' % error)




def demo():

    pat = []

    ind = 0
    for dat in data:
        pat.append([dat, [result[ind]]])
        ind += 1

    # print(pat)
    # print('format data ->')
    # print(np.array(pat))

    # create a network with two input, two hidden, and one output nodes

    n = NN(len(data[0]), len(data[0])*2, 1)
    # train it with some patterns
    n.train(pat)
    # test it
    n.test(pat)


    #  | 0 -> 0.5 |  0.5 -> 1 |
    #  pat.append([array_input, [class]]);

    while True:

        # pat = [None] * 2

        pat = []
        array_input = []

        print('start Neural Network calculator')

        array_input.append(int(input("Gender: ")))
        array_input.append(int(input("Polyuria: ")))
        array_input.append(int(input("Polydipsia: ")))
        array_input.append(int(input("sudden weight loss: ")))
        array_input.append(int(input("weakness: ")))
        array_input.append(int(input("Polyphagia: ")))
        array_input.append(int(input("Genital thrush: ")))
        array_input.append(int(input("visual blurring: ")))
        array_input.append(int(input("Itching: ")))
        array_input.append(int(input("Irritability: ")))
        array_input.append(int(input("delayed healing: ")))
        array_input.append(int(input("partial paresis: ")))
        array_input.append(int(input("muscle stiffness: ")))
        array_input.append(int(input("Alopecia: ")))
        array_input.append(int(input("Obesity: ")))



        pat.append([array_input, []]);

        print("input ->")
        print(pat)

        n.test(pat)






if __name__ == '__main__':
    demo()















# end
