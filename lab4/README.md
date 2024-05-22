```markdown
# MLOps (dvc)

Ссылка в Google Drive: https://drive.google.com/drive/folders/1XkNc5NWCdiMkaKrr-PTYOx0cEkigg0YV?usp=sharing

## Шаг 1: Создание папки и установка утилит

```bash
mkdir lab4
cd lab4
sudo apt-get update
sudo apt-get install git
sudo apt-get install dvc
```

## Шаг 2: Настройка проекта для работы с git и dvc

```bash
git init
dvc init
```

## Шаг 3: Настройка удаленного хранилища

```bash
dvc remote add -d myremote gdrive://<folder_id>
dvc remote modify myremote gdrive_use_service_account true
dvc remote modify myremote gdrive_service_account_json_path /path/to/your/service/account/json/file
```

## Шаг 4: Создание и модификация датасета

Создание датасета о пассажирах «Титаника»: `a1_dataset_create.py`

Добавление файла под управление dvc и фиксация изменений:

```bash
dvc add data/titanic.csv
git add data/titanic.csv.dvc .gitignore
git commit -m "[description]"
dvc push
```

## Шаг 5: Модификация датасета

Модификация датасета, оставляя только нужные столбцы: `a2_dataset_modify.py`

Добавление модифицированного файла под управление dvc и фиксация изменений:

```bash
dvc add data/titanic_modified.csv
git add data/titanic_modified.csv.dvc
git commit -m "[description]"
dvc push
```

## Шаг 6: Создание новой версии датасета

Заполнение пропущенных значений в поле "Age" средним значением: `a3_dataset_fill.py`

Добавление новой версии под управление dvc и фиксация изменений:

```bash
dvc add data/titanic_filled.csv
git add data/titanic_filled.csv.dvc
git commit -m "[description]"
dvc push
```

## Шаг 7: Создание нового признака

Создание нового признака с использованием one-hot-encoding: `a4_dataset_new_feature.py`

Добавление файла с новым признаком под управление dvc и фиксация изменений:

```bash
dvc add data/titanic_encoded.csv
git add data/titanic_encoded.csv.dvc
git commit -m "[description]"
dvc push
```

## Шаг 8: Переключение между версиями датасета

Для переключения между версиями датасета используйте команды dvc checkout:

```bash
dvc checkout data/titanic.csv
dvc checkout data/titanic_modified.csv
dvc checkout data/titanic_filled.csv
dvc checkout data/titanic_encoded.csv
```

## Структура проекта

```plaintext
lab4/
│
├── data/
│   ├── titanic.csv
│   ├── titanic_modified.csv
│   ├── titanic_filled.csv
│   └── titanic_encoded.csv
│
├── .git/
├── .dvc/
├── .gitignore
└── a1_dataset_create.py
└── a2_dataset_modify.py
└── a3_dataset_fill.py
└── a4_dataset_new_feature.py
└── README.md
```

```