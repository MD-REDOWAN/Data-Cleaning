
# Replace Empty values


# The fillna() method allows us to replace empty cells with a value:

import pandas as pd

x = pd.read_csv('cumulative.csv')



print(x.fillna(100, inplace = True)) # fillna() method fill all empty cells by 100


print()


# Replace Only Specified Columns

print(x.fillna({"kepler_name": "Shihab"},inplace = True))



print()


# Replace Using Mean() , average value

a = x["kepoi_name"].mean()

x.fillna({"kepai_name": a}, inplace = True)



print()



# Replace the Median() value , middle value after ascending

b = x["kepoi_name"].median()

x.fillna({"kepoi_name": b}, inplace = True)



print()


# Replace mode(), that appears most frequently

c = x["kepoi_name"].mode()

x.fillna({"kepoi_name": c}, inplace = True)

print(x.__dataframe__)


