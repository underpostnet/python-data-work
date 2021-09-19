import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.pyplot import show






def isNaN(num):
    return num != num

# https://www.delftstack.com/es/howto/python-pandas/pandas-correlation-matrix/

df = pd.read_csv("data/diabetes.csv", sep=",", skip_blank_lines=False)
df=df.mask((  (df==0) & (df.columns != 'Pregnancies') & (df.columns != 'Outcome') )).fillna(df.mean())



# print(df)

corr_df = df.corr(method='pearson')

plt.matshow(corr_df)
sns.heatmap(corr_df, annot=True)
plt.show()

























# end
