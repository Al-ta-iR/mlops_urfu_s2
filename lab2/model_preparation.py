from sklearn.ensemble import RandomForestRegressor
import pickle
import pandas as pd


# Чтение тренировочных данных
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv')

# Создание модели
model = RandomForestRegressor()

# Обучение модели
model.fit(X_train, y_train.values.ravel())

# Сохранение модели
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
