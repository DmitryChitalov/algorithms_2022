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


    def hash_on(self,url):
        salt = uuid4().hex
        url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        return url_hash

    def cash_in(self, url):
        url_hash = self.hash_on(url)
        self.urls.setdefault(url, url_hash)
        return f"Запись HASH для {url} успешно совершена!"

url1 = 'https://siteactiv.ru/terminy/URL-adress/'
url2 = 'https://yandex.ru'

lst_urls = CashWeb()

lst_urls.cash_in(url1)
lst_urls.cash_in(url2)

print(lst_urls.urls)