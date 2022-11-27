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
from uuid import uuid4
from hashlib import sha256

# Сделаем "ленивую" соль:
salt = uuid4().hex

# Словарь в качестве кэша:
cache_dict = {}


def cash_filler(link):
    if not cache_dict.get(link):
        cache_dict[link] = sha256(salt.encode() + link.encode()).hexdigest()
        for key, value in cache_dict.items():
            print(f'{key} - {value}')
        print('-'*50)
    else:
        print(f'{link} есть в кэше, хеш - {sha256(salt.encode() + link.encode()).hexdigest()}')
        print('-'*50)


cash_filler('https://google.com/')
cash_filler('https://yandex.ru/')
cash_filler('https://google.com/')
