import pandas as pd


train_df = pd.read_csv('data/titanic_modified.csv')
train_df = pd.get_dummies(train_df, columns=['Sex'])
dataset_encoded_path = 'data/titanic_encoded.csv'
train_df.to_csv(dataset_encoded_path, index=False)
