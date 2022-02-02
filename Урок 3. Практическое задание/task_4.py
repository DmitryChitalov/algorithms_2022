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

import hashlib
from binascii import hexlify
from uuid import uuid4
from timer import Timer

class UrlCacheClass:
    def __init__(self):
        self.password = uuid4().hex.encode()
        self.salt = uuid4().hex.encode()
        self.data = {}

    @Timer(text="Поиск URL за {:.6f} секунд")
    def add_url(self, url):
        url_exists = self.data.get(url, 0)
        if url_exists == 0:
            self.data[url] = self.get_hash(url)
        else:
            print(f'URl {url} already exists. Hash {self.data[url]}')

    def get_data(self):
        return self.data

    def get_hash(self, url):
        return hexlify(hashlib.pbkdf2_hmac(hash_name='sha256',
                                           password=self.password,
                                           salt=self.salt,
                                           iterations=10)).decode('utf-8')


uc = UrlCacheClass()
uc.add_url('mail.ru')
uc.add_url('google.com')
uc.add_url('yandex.com')
uc.add_url('bob.com')
uc.add_url('mail.ru')
print(uc.get_data())
