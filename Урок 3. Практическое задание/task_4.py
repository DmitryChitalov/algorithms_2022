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

"""Если можно использовать пакет, который не обсуждали"""

import hashlib
from uuid import uuid4
import validators

cash = {}
salt = str(uuid4().hex)

def cash_urls():
    url = input('Введите ссылку: ')
    if not validators.url(url):
        return
    else:
        if url in cash:
            print('Хэш url-а - ' + cash[url])
        else:
            cash[url] = hashlib.sha512((salt + url).encode('utf-8')).hexdigest()
        cash_urls()

cash_urls()

"""Если нельзя, то так:

import hashlib
from uuid import uuid4

cash = {}
salt = str(uuid4().hex)

def cash_urls():
    url = input('Введите ссылку. Если у вас больше нет ссылок, не вводите ничего: ')
    if url == '':
        return
    else:
        if url in cash:
            print('Хэш url-а - ' + cash[url])
        else:
            cash[url] = hashlib.sha512((salt + url).encode('utf-8')).hexdigest()
        cash_urls()
"""
