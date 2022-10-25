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

url_store = {}


def url_hash(url):
    if url in url_store.keys():
        return url_store[url]
    else:
        url_store.setdefault(url, hashlib.sha512(url.encode('utf-8')).hexdigest() + uuid4().hex)
    return url_store


url_hash('www.in.com')
url_hash('www.off.com')
print(url_hash('www.in.com'))
print(url_store)
