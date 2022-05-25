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

from hashlib import sha512
from uuid import uuid4


class Cache:
    def __init__(self):
        self.data = {}

    def check_url(self, url: str):
        try:
            print(f"URL's hash: {self.data.__getitem__(url)}")
        except KeyError:
            print("URL is not cached")

    def add_url(self, url: str):
        if self.data.get(url) is None:
            salt = uuid4().hex
            url_hash = sha512(salt.encode() + url.encode()).hexdigest()
            self.data[url] = url_hash
        else:
            print("This URL is already cached")

    def get_data(self):
        return self.data


cache = Cache()

cache.add_url('https://web.telegram.org/k/')
cache.add_url('https://web.telegram.org/k/')
cache.add_url('https://gb.ru/')
cache.add_url('https://py.checkio.org/')

cache.check_url('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwi89cfz1Pr3AhXxoosKHUqmAFkQPAgI')
cache.check_url('https://py.checkio.org/')
