import numpy as np
from sklearn.preprocessing import minmax_scale

# Normalization typically means rescales the values into a range of [0,1].
# Standardization typically means rescales data to have a mean of 0 and
# a standard deviation of 1 (unit variance).

# your function
def normalize_list(list_normal):
    max_value = max(list_normal)
    min_value = min(list_normal)
    for i in range(len(list_normal)):
        list_normal[i] = (list_normal[i] - min_value) / (max_value - min_value)
    return list_normal

#Scikit learn version
def normalize_list_numpy(list_numpy):
    normalized_list = minmax_scale(list_numpy)
    return normalized_list

test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_array_numpy = np.array(test_array)

print(normalize_list(test_array))
print(normalize_list_numpy(test_array_numpy))

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.pyplot import show
from sklearn import preprocessing

X_scaled = (np.random.rand(100)*10)
print('1 X_scaled ->')
print(X_scaled)
plt.hist(X_scaled)
show();

X_scaled = normalize_list(X_scaled)
print('3 X_scaled ->')
print(X_scaled)
plt.hist(X_scaled)
show();

X_scaled = preprocessing.scale(X_scaled)
print('2 X_scaled ->')
print(X_scaled)
plt.hist(X_scaled)
show();

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
