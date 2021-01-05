import matplotlib.pyplot as plt
from matplotlib.pyplot import show
import pandas as pd

def isNaN(num):
    return num != num

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

df = pd.read_csv("Preeclampsia.csv", sep=";", skip_blank_lines=False)

print(df)

data_label = []
data_value = []

for fila, columna in df.iterrows():

    data_label.append(columna[0])
    data_value.append(round(columna[1],3))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


importances =  data_value
features = data_label

unsorted_list = [(importance, feature) for feature, importance in
                  zip(features, importances)]

# print(unsorted_list)

sorted_list = sorted(unsorted_list, reverse=True)

# print(sorted_list)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# money = [0.9, 0.5, 0.4, 0.7]

fig, ax = plt.subplots()

# ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money, color=['red', 'blue', 'green', 'blue'])

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# https://pypi.org/project/colour/

from colour import Color
init_color = Color("#381dcf")
colors = list(init_color.range_to(Color("#a09ee6"),len(data_label)))

arr_color = []

for c in colors:
    arr_color.append(("%s" % c))

# print(arr_color)

# rgb to hex
# print('#%02x%02x%02x' % (0, 128, 64))

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# https://stackoverflow.com/questions/54424256/sort-bar-chart-by-list-values-in-matplotlib

features_sorted = []
importance_sorted = []

for i in sorted_list:
    features_sorted += [i[1]]
    importance_sorted += [i[0]]

val_label = ax.bar(range(len(importance_sorted)), importance_sorted, color=arr_color)
plt.xticks(range(len(importance_sorted)), features_sorted);
# plt.yticks

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    i_val = 0
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.8*height,
                sorted_list[i_val][0],
                ha='center', va='bottom')
        i_val = i_val + 1

autolabel(val_label)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

tick = []
n = 5

for i in range(n):
    tick.append((1/(n-1))*i)

plt.yticks(tick)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

plt.title(label='Preeclampsia')
plt.xlabel("ML")
plt.ylabel("AUC")

show()
