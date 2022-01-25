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

class CashWeb:
    def __init__(self):
        self.urls = {}

    def hashing(self, url):
        salt = uuid4().hex
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return url_hash

    def cash_save(self, url):
        url_hash = self.hashing(url)
        self.urls.setdefault(url, url_hash)
        return print(f'Запись {url} добавлена!')


url_test1 = 'https://www.python.org/dev/peps/pep-0008/#imports'
url_test2 = 'https://gb.ru/lessons/195691'
url_test3 = 'https://gb.ru/b/s30'

search_url = CashWeb()

search_url.cash_save(url_test1)
search_url.cash_save(url_test2)
search_url.cash_save(url_test3)
print(search_url.urls)
