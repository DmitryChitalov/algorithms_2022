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
import hashlib

cache_dict = {}


def counting_hash_url(url):
    if cache_dict.get(url, None):
        return f'Страница {url} прсутствует в кеше: {cache_dict[url]}'
    else:
        salt = uuid4().hex
        hash_url = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
        cache_dict[url] = hash_url

    return f'Вычислили хеш {hash_url} и записали в кеш'


print(counting_hash_url('https://pythonworld.ru'))
print(counting_hash_url('https://pythonworld.ru'))
print(counting_hash_url('https://python.ru'))
