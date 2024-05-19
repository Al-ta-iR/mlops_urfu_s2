#!/bin/bash

# Проверка на ошибки
set -e

echo "Создание данных..."
python data_creation.py

echo "Предобработка данных..."
python model_preprocessing.py

echo "Обучение модели..."
python model_preparation.py

echo "Тестирование модели..."
python model_testing.py

echo "Конвейер завершен успешно."
