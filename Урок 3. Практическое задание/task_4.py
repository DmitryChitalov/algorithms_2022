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
from uuid import uuid4

class webCaching:

    def __init__(self):
        self._cache = {}

    def set_cache(self, url: str):
        if url and url not in self._cache:
            salt = uuid4().hex.encode("utf-8")
            self._cache.update({url: hashlib.sha512(salt + url.encode("utf-8")).hexdigest()})
        elif url in self._cache.keys():
            print("already exists: %s" % self.show_cache[url])


    @property
    def show_cache(self):
        return self._cache


if __name__ == "__main__":
    cache = webCaching()
    cache.set_cache("https://vk.com")
    print(cache.show_cache)
