import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(file_path):
    # Загрузка данных
    data = pd.read_csv(file_path)
    
    # Разделение признаков и целевой переменной
    X = data.drop(columns=['target'])
    y = data['target']
    
    # Стандартизация признаков
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Создание предобработанного датафрейма
    preprocessed_data = pd.DataFrame(X_scaled, columns=X.columns)
    preprocessed_data['target'] = y.values
    
    return preprocessed_data


# Предобработка и сохранение данных для train
train_files = [f for f in os.listdir('train') if f.endswith('.csv')]
for file in train_files:
    file_path = os.path.join('train', file)
    preprocessed_data = preprocess_data(file_path)
    preprocessed_data.to_csv(file_path, index=False)
    
# Предобработка и сохранение данных для test
test_files = [f for f in os.listdir('test') if f.endswith('.csv')]
for file in test_files:
    file_path = os.path.join('test', file)
    preprocessed_data = preprocess_data(file_path)
    preprocessed_data.to_csv(file_path, index=False)

print("Данные успешно предобработаны и сохранены.")
