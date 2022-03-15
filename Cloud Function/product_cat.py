import pandas as pd

df = pd.read_csv('train.csv')

print(df.head())

df_prods = df[['Product_ID','Product_Category_1', 'Product_Category_2']].drop_duplicates()
df_prods['Product_Category_1'] = df['Product_Category_1'].fillna(0)
df_prods['Product_Category_2'] = df['Product_Category_2'].fillna(0)

# Get product
row = df_prods.loc[df_prods['Product_ID'] == 'P00069042']
print(row)
print(row.iloc[0]['Product_Category_1'])
df_prods.to_csv('prods.csv', index=False)