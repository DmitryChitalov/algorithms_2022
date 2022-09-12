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
from uuid import uuid4


def web_cash(url):
    url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
    if url in cash.keys():
        return f'Хэш url-a {url} уже есть: {url_hash}'
    else:
        cash[url] = url_hash
        return f'Хэш url-a {url} добавлен в базу'


salt = uuid4().hex
cash = {}
print(web_cash('gb.ru'))
print(web_cash('gb.ru'))
print(web_cash('ya.ru'))
print(web_cash('ya.ru'))
