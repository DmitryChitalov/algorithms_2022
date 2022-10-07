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

from hashlib import sha256
from uuid import uuid4

salt = uuid4().hex
cache_obj = {}

def check_cache(url):
    hash_url = sha256(salt.encode() + url.encode()).hexdigest()
    if cache_obj.get(url):
        print('хеш url-а: ', hash_url)
    else:
        cache_obj[url] = hash_url

check_cache('https://translate.yandex.ru/')
check_cache('https://www.youtube.com/')
check_cache('https://gb.ru/education')
check_cache('https://translate.yandex.ru/')
print(cache_obj)


