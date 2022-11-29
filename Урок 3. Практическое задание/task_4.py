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

import uuid
import hashlib


class CacheStorage:
    def __init__(self):
        self.cache = dict()

    def add_hash(self, url: str):
        print('adding hash')
        salt = str(uuid.uuid4())
        url_hash = hashlib.sha256(str(url).encode() + salt.encode()).hexdigest()
        self.cache[str(url)] = {"hash": url_hash,
                                "salt": salt}

    def get_hash(self, url):
        url_hash = self.cache.get(url)
        if not url_hash:
            self.add_hash(url)
            return
        print(url_hash['hash'])


if __name__ == '__main__':
    cache = CacheStorage()
    cache.get_hash('gb.ru')
    cache.get_hash('heroku.com')
    cache.get_hash('youtube.com')
    cache.get_hash('google.ru')
    cache.get_hash('habr.com')
    cache.get_hash('gb.ru')
    cache.get_hash('heroku.com')
    cache.get_hash('youtube.com')
    cache.get_hash('google.ru')
    cache.get_hash('habr.com')