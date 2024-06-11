import pandas as pd

df1 = pd.read_csv('swmath_to_codemeta.csv',skiprows=2,header=None,names=['swMATH','Property'])
df2 = pd.read_csv('Cargo.csv')

df = pd.merge(df2,df1, on='Property',how='outer',)

df.drop('Rust Package Manager', axis=1, inplace=True)

df = df[['Property','swMATH']]
df.drop_duplicates(inplace=True)
df.to_csv('swMATH.csv', index=False)

