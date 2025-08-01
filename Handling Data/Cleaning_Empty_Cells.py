
# Remove Rows
# The dropna() method returns a new DataFrame, and will not change the original.

import pandas as pd

x = pd.read_csv('cumulative.csv')

y = x.dropna()

print(y) # show the Empty columns 


print("-----------------------------------------------------------")


# The dropna(implace = True) remove all rows which are containing NULL values

print(x.dropna(inplace = True))

print("Remove all null rows")

print("----------------------------------------------------------")

print(y.to_string())




