import pandas as pd


train_df = pd.read_csv('data/titanic_modified.csv')
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
dataset_filled_path = 'data/titanic_filled.csv'
train_df.to_csv(dataset_filled_path, index=False)
