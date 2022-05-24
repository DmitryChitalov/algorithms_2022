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

hash_obj = {}
salt = uuid4().hex

def get_cash_url(url):
    if hash_obj.get(url):
        return f'для такого {url} уже есть хеш {hash_obj[url]}'
    else:
        hash_obj[url] = sha256(salt.encode() + url.encode()).hexdigest()
        return hash_obj[url]


print(get_cash_url('https://gb.ru/'))
print(get_cash_url('https://yandex.ru/'))
print(get_cash_url('https://gb.ru/'))
