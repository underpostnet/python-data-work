import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import webbrowser



# https://www.kaggle.com/dansbecker/permutation-importance/tutorial

data = pd.read_csv('./data/diabetes.csv')
data=data.mask((  (data==0) & (data.columns != 'Pregnancies') & (data.columns != 'Outcome') )).fillna(data.mean())

y =(data['Outcome'] == 1)

# data = pd.read_csv('./data/fifa.csv')
# y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary

# feature_names = [i for i in data.columns if data[i].dtype in [np.int64]]
feature_names = [i for i in data.columns ]

feature_names.pop()

print("feature_names ->")
print(feature_names)

X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=50,
                                  random_state=0).fit(train_X, train_y)


import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state=1).fit(val_X, val_y)

render = eli5.show_weights(perm, feature_names = val_X.columns.tolist())

# Write html object to a file (adjust file path; Windows path is used here)
with open('./test.html','wb') as f:
    f.write(render.data.encode("UTF-8"))

# Open the stored HTML file on the default browser
url = r'file:///C:/dd/deploy_area/python/1709/test.html'
webbrowser.open(url, new=2)
