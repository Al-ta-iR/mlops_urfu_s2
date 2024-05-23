# Проект: Развертывание модели машинного обучения в Docker

## Описание

Этот проект демонстрирует, как развернуть микросервис в Docker контейнере, который включает модель машинного обучения. В качестве примера используется модель логистической регрессии, обученная на датасете Iris, которая принимает запросы по API и возвращает предсказания.

## Структура проекта

```
lab3/
├── app/
│   ├── model.py
│   ├── app.py
├── data/
│   ├── train.csv
│   ├── test.csv
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Требования

- Docker
- Docker Compose
- Учетная запись на Docker Hub (для загрузки образов)

## Установка и запуск

### 1. Клонирование репозитория

Клонируйте репозиторий на вашу локальную машину:

```sh
git clone <URL вашего репозитория>
cd lab3
```

### 2. Сборка Docker образа

Соберите Docker образ с помощью Docker Compose:

```sh
docker compose build
```

### 3. Запуск контейнера

Запустите контейнер в фоновом режиме:

```sh
docker compose up -d
```

### 4. Проверка работы API

Проверьте работу API, отправив POST-запрос с помощью `curl`:

```sh
curl -X POST -H "Content-Type: application/json" -d '{"features": [5.1, 3.5, 1.4, 0.2]}' http://localhost:5000/predict
```

Вы должны получить ответ с предсказанием в формате JSON, например: `{"prediction": 0}`.


## Остановка и удаление контейнеров

Для остановки запущенных контейнеров используйте:

```sh
docker compose down
```

## Очистка

Для удаления всех Docker образов и контейнеров используйте:

```sh
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```