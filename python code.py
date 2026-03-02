import pandas as pd
df = pd.read_csv('customer_shopping_behavior.csv')
print(df.head())
df.info()
df.describe(include='all')
df.isnull().sum()
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower().str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
df.columns
labels = ['Young Adult','Adult','Middle-Aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']].head(10))
frequency_mapping = {'Fortnightly':14,'Weekly':7,'Bi-Weekly':14,'Monthly':30,'Quarterly':90,'Annually':365,'Every 3 MDFonths':90}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[['frequency_of_purchases','purchase_frequency_days']].head(10))
df[['discount_applied','promo_code_used']].head(10)
print((df['discount_applied'] == df['promo_code_used']).all())
df = df.drop('promo_code_used', axis=1) 
print(df.columns)


import mysql.connector
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/customer_db")
df.to_sql(name='customer_shopping_behaviour', con=engine, if_exists='replace', index=False)
print("data inserted into mysql successfully")