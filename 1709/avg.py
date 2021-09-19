


import pandas as pd







def isNaN(num):
    return num != num

# https://www.delftstack.com/es/howto/python-pandas/pandas-correlation-matrix/

df = pd.read_csv("data/diabetes.csv", sep=",", skip_blank_lines=False)

print(df)

df=df.mask((  (df==0) & (df.columns != 'Pregnancies') & (df.columns != 'Outcome') )).fillna(df.mean())

print(df)
