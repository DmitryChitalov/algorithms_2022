"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import requests
import hashlib

# url = 'https://www.google.com'
hash_table = {}
while True:
    url = input('Введите URL или 0 - для выхода: ')
    try:
        url = int(url)
        if url == 0:
            break
    except ValueError:
        pass
    try:
        r = requests.get(url)
    except requests.exceptions.MissingSchema:
        print('Введенная строка не является url')
        break
    if r.status_code == 200:
        if url not in hash_table:
            salt = hashlib.sha256(url.encode()).hexdigest()  # У меня скромная фантазия
            hash_url = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
            hash_table.setdefault(url, hash_url)
        else:
            print(hash_table[url])
    else:
        print('URL не действителен')