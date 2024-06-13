import pandas as pd

df1 = pd.read_csv('swmath_to_codemeta.csv',skiprows=1,header=None,names=['swMATH','Property','Schema.org'])
df2 = pd.read_csv('properties_description.csv')

df = pd.merge(df2,df1, on='Property',how='outer',)



df = df[['Property','swMATH']]
df.drop_duplicates(inplace=True)
df.to_csv('swMATH.csv', index=False)

