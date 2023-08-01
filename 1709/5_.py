import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import webbrowser

#  https://www.kaggle.com/dansbecker/permutation-importance/tutorial

df = pd.read_csv("../01-08-2023/data/BBDD-OB-CON-VARIABLES-MODIFICADAS.CSV.csv",
                 sep=",", skip_blank_lines=False, low_memory=False)

data = df.loc[:, ['Edad', 'OB', 'E', 'I',
                  'Paridad', 'AñosEscolaridad']]

y = (df['TIENEONO'] == 1)

X = data[data.columns]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(n_estimators=50,
                                  random_state=0).fit(train_X, train_y)


import eli5
from eli5.sklearn import PermutationImportance

perm = PermutationImportance(my_model, random_state=1).fit(val_X, val_y)

print(eli5.format_as_text(eli5.explain_weights(perm, feature_names = val_X.columns.tolist())))

exit()

render = eli5.show_weights(perm, feature_names = val_X.columns.tolist())

# Write html object to a file (adjust file path; Windows path is used here)
with open('./test.html','wb') as f:
    f.write(render.data.encode("UTF-8"))

# Open the stored HTML file on the default browser
url = r'file:///C:/dd/deploy_area/python/1709/test.html'
webbrowser.open(url, new=2)
