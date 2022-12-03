"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет -- ???

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import json
import hashlib


def unloading_the_cache():
    with open('urls.json', 'r') as f:
        return json.load(f)


def adding_to_the_cache(data):
    with open('urls.json', 'w') as f:
        json.dump(data, f)


url = input('Введите адрес - ')
data = unloading_the_cache()
if url in data:
    print(data[url])
else:
    data[url] = hashlib.sha256(url.encode()).hexdigest()
    adding_to_the_cache(data)
    print('Данной страницы нет.')
