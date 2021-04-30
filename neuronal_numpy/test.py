

import numpy as np

from data_prep import features,targets, features_test, targets_test

mu, sigma, size_data_number = 0, 0.1, 1000 # mean and standard deviation
s = np.random.normal(mu, sigma, size_data_number)


# print(s)
# print(len(s))

mu, sigma, size_data_number = 0, 0.1, (5,2) # mean and standard deviation
s = np.random.normal(mu, sigma, size_data_number)

# print(s)
# print(len(s))


# print('features.values ->')
# print(features.values)
# print('zip ->')
# print(zip(features.values,targets))

# https://likegeeks.com/es/funcion-zip-de-python/

x = ("Joey", "Monica", "Ross")
y = ("Chandler", "Pheobe")
z = ("David", "Rachel", "Courtney")

result = zip(x, y, z)
# print(result)
# print(tuple(result))


# funcion sigmoide en numpy por lo tanto la entrada deve ser ->
# <class 'numpy.ndarray'>
def sigmoide(x):
    return 1/(1 + np.exp(-x))


a = np.array([1, 2, 3]);
b = np.array([[1, 2, 3],[1, 2, 3]]);

print(type(a))
print(type(b))

print(np.matmul(b,a));
print(np.dot(b,a));

# end
