import shap  # package used to calculate Shap values
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import webbrowser

df = pd.read_csv("../01-08-2023/data/BBDD-OB-CON-VARIABLES-MODIFICADAS.CSV.csv",
                 sep=",", skip_blank_lines=False, low_memory=False)

data = df.loc[:, ['Edad', 'OB', 'E', 'I',
                  'Paridad', 'AñosEscolaridad']]

y = (df['TIENEONO'] == 1)

X = data[data.columns]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
my_model = RandomForestClassifier(random_state=0).fit(train_X, train_y)

# row_to_show = len(val_y)-1
row_to_show = 5
# use 1 row of data here. Could use multiple rows if desired

data_for_prediction = val_X.iloc[row_to_show]
data_for_prediction_array = data_for_prediction.values.reshape(1, -1)

print('row_to_show', row_to_show)
print('data_for_prediction', data_for_prediction)
print('data_for_prediction_array', data_for_prediction_array)

my_model.predict_proba(data_for_prediction_array)


# Create object that can calculate shap values
explainer = shap.TreeExplainer(my_model)

# Calculate Shap values
shap_values = explainer.shap_values(data_for_prediction)


shap.initjs()
force_plot = shap.force_plot(
    explainer.expected_value[1], shap_values[1], data_for_prediction)

shap_html = f"<head>{shap.getjs()}</head><body>{force_plot.html()}</body>"

# Write html object to a file (adjust file path; Windows path is used here)
with open('./test_shap.html', 'wb') as f:
    f.write(shap_html.encode("UTF-8"))

# Open the stored HTML file on the default browser
url = r'file:///C:/dd/python-data-work/1709/test_shap.html'
webbrowser.open(url, new=2)


# end
