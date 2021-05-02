import numpy as np
import pandas as pd

admissions = pd.read_csv('binary.csv')

print('admissions ->')
print(admissions)

# Make dummy variables for rank
data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)

print('dummy variables ->')
print(data)

data = data.drop('rank', axis=1)

print('drop rank ->')
print(data)

# Standarize features
for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:,field] = (data[field]-mean)/std

print('Standarize ->')
print(data)

# Split off random 10% of the data for testing
np.random.seed(21)
sample = np.random.choice(data.index, size=int(len(data)*0.9), replace=False)
data, test_data = data.iloc[sample], data.drop(sample)

print('Split data ->')
print(data)
print('Split test_data ->')
print(test_data)

# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']

print('features ->')
print(features)
print('targets ->')
print(targets)

features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']

print('features_test ->')
print(features_test)
print('targets_test ->')
print(targets_test)

pat_training = []
for fila, columna in features.iterrows():
    pat_training.append([[
    columna[0],
    columna[1],
    columna[2],
    columna[3],
    columna[4],
    columna[5]]])

pat_test = []
for fila, columna in features_test.iterrows():
    pat_test.append([[
    columna[0],
    columna[1],
    columna[2],
    columna[3],
    columna[4],
    columna[5]]])

index = 0
for val in targets:
    pat_training[index].append([val])
    index = index + 1

index = 0
for val in targets_test:
    pat_test[index].append([val])
    index = index + 1


# print(pat_training)

# print(pat_test)



# end
