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


cash_dict = {}
salt = uuid4().hex


def url_cash(key_url):
    if key_url in cash_dict.keys():
        print(f'{cash_dict[key_url]}')
    else:
        cash_dict[key_url] = hashlib.sha512(salt.encode('utf-8') + key_url.encode('utf-8')).hexdigest()
        print(f'Страница записана в кэш. Хеш {cash_dict[key_url]}')


url_cash('mail.ru')
url_cash('labirint.ru')
url_cash('gb.ru')
url_cash('labirint.ru')
