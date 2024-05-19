import numpy as np
import pandas as pd
import os


# Функция для создания набора данных
def create_dataset(n_samples=100, n_features=1, noise=False, anomalies=False):
    np.random.seed(42)
    X = np.linspace(0, 10, n_samples)
    y = np.sin(X) + 0.1 * np.random.randn(n_samples)  # Основная функция

    if noise:
        y += 0.2 * np.random.randn(n_samples)  # Добавление шума

    if anomalies:
        y[::10] += 3 * (0.5 - np.random.rand(n_samples // 10))  # Добавление аномалий

    data = np.column_stack((X, y))
    return pd.DataFrame(data, columns=[f'feature_{i}' for i in range(n_features)] + ['target'])

# Создание директорий, если их нет
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)

# Создание и сохранение наборов данных
datasets = {
    'train_data_1.csv': create_dataset(),
    'train_data_2.csv': create_dataset(noise=True),
    'train_data_3.csv': create_dataset(anomalies=True),
    'test_data_1.csv': create_dataset(),
    'test_data_2.csv': create_dataset(noise=True),
    'test_data_3.csv': create_dataset(anomalies=True),
}

for filename, dataset in datasets.items():
    if 'train' in filename:
        dataset.to_csv(os.path.join('train', filename), index=False)
    else:
        dataset.to_csv(os.path.join('test', filename), index=False)

print("Датасеты успешно созданы и сохранены в соответствующих папках.")
