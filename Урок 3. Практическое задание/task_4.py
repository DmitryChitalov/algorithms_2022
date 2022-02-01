"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет.

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

from hashlib import sha512
from uuid import uuid4


class cash_web:
    def __init__(self):
        self.urls = {}

    def hashing(self, url):
        salt = uuid4().hex
        url_hash = sha512(salt.encode() + url.encode()).hexdigest()
        return url_hash

    def cash_save(self, url):
        url_hash = self.hashing(url)
        self.urls.setdefault(url, url_hash)
        return print(f'Запись {url} добавлена!')


url_1 = 'https://habr.com/ru/company/ruvds/blog/'
search_url = cash_web()
search_url.cash_save(url_1)
print(search_url.urls)
