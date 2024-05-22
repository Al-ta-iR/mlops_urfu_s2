import pandas as pd


train_df = pd.read_csv('data/titanic.csv')
train_df = train_df[['Pclass', 'Sex', 'Age']]
dataset_modified_path = 'data/titanic_modified.csv'
train_df.to_csv(dataset_modified_path, index=False)
