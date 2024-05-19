from sklearn.metrics import mean_squared_error
import pandas as pd
import pickle


# Чтение тестовых данных
X_test = pd.read_csv('X_test.csv')
y_test = pd.read_csv('y_test.csv')

# Загрузка модели
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Предсказание
y_pred = model.predict(X_test)

# Оценка качества модели
accuracy = mean_squared_error(y_test, y_pred)
print(f'Accuracy: {accuracy}')
