import pandas as pd

df = pd.read_csv('train.csv')

print(df.head())

df_prods = df[['User_ID','Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status']].drop_duplicates()

df_prods.to_csv('users.csv', index=False)