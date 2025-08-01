
# wrong format can make it difficult or even impossible to analze data

# Two option to fix it (remove the rows, or Convert all cells)


import pandas as pd

x = pd.read_csv('cumulative.csv')

x['kepid'] = pd.to_numeric(x['kepid'], format = 'fixed') # want numaric number

print(x.to_string)



# Remove cells

print(x.dropna(subset = ['kepid'], inplace = True))

