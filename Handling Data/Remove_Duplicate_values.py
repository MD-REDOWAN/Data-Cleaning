
# Find the duplicate value

# use duplicated() method for find duplicate values

import pandas as pd
x = pd.read_csv('cumulative.csv')

print(x.duplicated()) 


# if any duplicate value found show True without False

print("-------------------------------------------------")

# Remove Duplicates drop_duplicates()

x.drop_duplicates(inplace = True)


print(x)

