import requests


url = 'https://github.com/Al-ta-iR/mlops_urfu_s2/raw/main/lab1/train/train_data_1.csv'
response = requests.get(url)
with open('lab2/data.csv', 'wb') as f:
    f.write(response.content)