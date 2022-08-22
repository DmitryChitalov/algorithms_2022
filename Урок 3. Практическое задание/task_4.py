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


class CacheWeb:
    def __init__(self):
        self.web_dict = {}
        self.salt_dict = {}

    def web_to_cache(self, url):
        if self.web_dict.get(url):
            return self.web_dict[url]
        else:
            salt = uuid4().hex
            self.salt_dict.setdefault(url, salt)
            self.web_dict.setdefault(url, hashlib.sha256(url.encode('utf-8') + salt.encode()).hexdigest())


our_web_cache = CacheWeb()
print(our_web_cache.web_to_cache('www.google.com'))
print(our_web_cache.web_to_cache('www.google.com'))
print(our_web_cache.web_to_cache('www.yandex.tr'))
print(our_web_cache.web_to_cache('www.yandex.tr'))