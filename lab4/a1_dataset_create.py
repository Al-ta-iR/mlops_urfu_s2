import os
import pandas as pd
from catboost.datasets import titanic


# Создание директории 'data', если она не существует
os.makedirs('data', exist_ok=True)

# Загрузка датасета из облачного хранилища CatBoost
train_df, _ = titanic()

# Указание пути для сохранения датасета
dataset_path = 'data/titanic.csv'

# Сохранение датасета в CSV файл
train_df.to_csv(dataset_path, index=False)

print(f'Dataset saved to {dataset_path}')
