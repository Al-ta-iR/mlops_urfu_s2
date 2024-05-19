from sklearn.model_selection import train_test_split
import pandas as pd


# Чтение данных
data = pd.read_csv('data.csv')

# Обработка данных (пример)
data = data.dropna()  # Удаление пропущенных значений

# Выделение признаков и меток
X = data.drop('target', axis=1)  # Признаки
y = data['target']  # Метки

# Разделение на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Сохранение наборов данных
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
