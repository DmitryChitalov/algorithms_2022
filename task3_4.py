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

from hashlib import sha256
from uuid import uuid4


class Cache:
    def __init__(self):
        self.hash_storage = {}
        self.salt_storage = {}

    def get_hash(self, url: str):
        url_cache = self.hash_storage.get(url)
        if url_cache:
            return url_cache

        self.hash_storage[url] = self.make_hash(url)
        return 'Hash Saved'

    def get_salt(self, url: str):
        salt = self.salt_storage.get(url)
        if salt:
            return salt

        salt = uuid4().hex
        self.salt_storage[url] = salt
        return salt

    def make_hash(self, url: str):
        """
        создаю хэш
        """
        salt: str = self.get_salt(url)
        result: str = sha256(salt.encode() + url.encode()).hexdigest()
        return result


"""
Очень отстаю от уроков поэтому делаю все как можно быстрее 
А так задаие интереснной если еще больше развить тут ООП
"""
# https://gb.ru/, https://drive.google.com,
if __name__ == "__main__":
    cache = Cache()
    print(cache.get_hash("https://drive.google.com"))
    print(cache.get_hash("https://gb.ru/"))
    print(cache.get_hash("https://www.google.ru/"))
    print(cache.get_hash("https://drive.google.com"))
    print(cache.get_hash("https://gb.ru/"))
    print(cache.get_hash("https://www.google.ru/"))