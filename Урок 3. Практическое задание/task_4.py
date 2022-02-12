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
import random
from uuid import uuid4

class HashUrl:

    def __init__(self):
        self.base_hash = {}

    def add_and_check_hash(self, url):
        hash_ = self.base_hash.get(url, False)
        if not hash_:
            salt = uuid4().hex
            hash_ = hashlib.sha256(url.encode() + salt.encode()).hexdigest()
            self.base_hash.update({url: (hash_, salt)})
            return f"{url} добавлен в базу"
        else:
            return f"{url} уже есть в базе"

        return hash_

    def get_count_url(self):
        return len(self.base_hash.keys())

base_url = HashUrl()
for i in range(2500):
    print(i, base_url.add_and_check_hash(f"http://test{random.randint(0,1000)}"))

print(f"Число записей {base_url.get_count_url()}")

