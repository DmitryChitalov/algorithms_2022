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

import hashlib
import json


def hash_and_cache_func(url):
    cache_dict = {}

    salt = 'my_salt'
    res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()

    with open('data.txt') as json_file:
        cache = json.load(json_file)
        if res in cache.values():
            return print(res)
        else:
            cache_dict.setdefault('hash', res)
            with open('data.txt', 'w') as outfile:
                json.dump(cache_dict, outfile)
            return print("Url записан в кеш.")




hash_and_cache_func('ya.ru')
