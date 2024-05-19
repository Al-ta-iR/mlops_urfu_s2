import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


def load_data(folder_path):
    data_frames = []
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    for file in files:
        file_path = os.path.join(folder_path, file)
        data_frames.append(pd.read_csv(file_path))
    return pd.concat(data_frames, ignore_index=True)


def train_model(train_data):
    # Разделение признаков и целевой переменной
    X = train_data.drop(columns=['target'])
    y = train_data['target']
    
    # Создание и обучение модели
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Загрузка и объединение всех тренировочных данных
train_data = load_data('train')

# Обучение модели
model = train_model(train_data)

# Сохранение обученной модели
os.makedirs('model', exist_ok=True)
model_path = os.path.join('model', 'trained_model.pkl')
joblib.dump(model, model_path)

print(f"Модель успешно обучена и сохранена по пути: {model_path}")
