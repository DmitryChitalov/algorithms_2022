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
from secrets import token_hex
from hashlib import sha256


class Cache:

    def __init__(self):
        self.cache = {}

    def get_hash(self, url: str):
        salt = token_hex(8)
        return salt, sha256(salt.encode() + url.encode()).hexdigest()

    def ask(self):
        url = input('Введите url (или 0 для выхода): ')
        if url == '0':
            exit()
        salt, hash = self.get_hash(url)
        if self.cache.get(url):
            print('Существует: %s' % (hash))
        else:
            self.cache[url] = hash
            print('Записано: %s' % (hash))
        self.ask()

Cache().ask()