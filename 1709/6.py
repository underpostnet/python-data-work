import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import webbrowser

# data = pd.read_csv('./data/fifa.csv')
# y = (data['Man of the Match'] == "Yes")  # Convert from string "Yes"/"No" to binary
# feature_names = [i for i in data.columns if data[i].dtype in [np.int64, np.int64]]

data = pd.read_csv('./data/diabetes.csv')
data=data.mask((  (data==0) & (data.columns != 'Pregnancies') & (data.columns != 'Outcome') )).fillna(data.mean())
y =(data['Outcome'] == 1)
feature_names = [i for i in data.columns ]
feature_names.pop()

X = data[feature_names]
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)

row_to_show = 5
data_for_prediction = val_X.iloc[row_to_show]  # use 1 row of data here. Could use multiple rows if desired
data_for_prediction_array = data_for_prediction.values.reshape(1, -1)


my_model.predict_proba(data_for_prediction_array)


import shap  # package used to calculate Shap values

# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# Calculate Shap values
shap_values = explainer.shap_values(data_for_prediction)


shap.initjs()
force_plot = shap.force_plot(explainer.expected_value[1], shap_values[1], data_for_prediction)

shap_html = f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>"

import webbrowser
# Write html object to a file (adjust file path; Windows path is used here)
with open('./test_shap.html','wb') as f:
    f.write(shap_html.encode("UTF-8"))

# Open the stored HTML file on the default browser
url = r'file:///C:/dd/deploy_area/python/1709/test_shap.html'
webbrowser.open(url, new=2)



# end
