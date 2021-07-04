import pandas as pd

def isNaN(num):
    return num != num

#------------------------------------------------
#------------------------------------------------

df = pd.read_csv("plan_valpo.csv", sep=";", skip_blank_lines=False)

print(df)
