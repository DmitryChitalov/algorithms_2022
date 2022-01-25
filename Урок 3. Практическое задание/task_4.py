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
from hashlib import sha256
from uuid import uuid4

cash = {}
salt = uuid4().hex


def url_check(url):
    if cash.get(url):
        print(cash[url])
    else:
        new_url = sha256(salt.encode() + url.encode()).hexdigest()
        cash[url] = new_url
    return cash


url_check('http://geekbrains.ru/')
url_check('http://yandex.ru/')
url_check('http://geekbrains.ru/')
url_check('http://yandex.ru/')
print(cash)