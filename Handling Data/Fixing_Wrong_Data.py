
# Wrong data Replace

import pandas as pd

x = pd.read_csv('cumulative.csv')

print(x)

print("--------------------------------------------------------------")

# Replace 3 no.row shihab :

x.loc[3, 'kepid'] = "shihab"

print(x)

print("--------------------------------------------------------")



# We can use loops for repalce

for a in x.index:
    if x.loc[a, 'kepid'] =='shihab':
        x.loc[a, 'kepid'] = 'Redowan'
        print(x)

print("----------------------------------------------------------")



# Remove Rows using loop

for a in x.index:
    if x.loc[a, 'kepoi_name'] == "K00752.02":
        x.drop(a, inplace = True)
        print(x)


