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


def hash_url(raw_url):
    hash_url = hashlib.sha512(raw_url.encode() + b'test_url').hexdigest()
    return {raw_url: hash_url}


def check_url(raw_url):
    return print(url_hash_dict[raw_url]) if raw_url in url_hash_dict else url_hash_dict.update(hash_url(raw_url))


url_hash_dict = {}
url_hash_dict.update(hash_url('http://gb.ru/'))
url_hash_dict.update(hash_url('http://filldb.info/'))
url_hash_dict.update(hash_url('https://github.com/'))
url_hash_dict.update(hash_url('https://start.fedoraproject.org/'))
url_hash_dict.update(hash_url('https://mysqlru.com/'))
url_hash_dict.update(hash_url('https://www.bigocheatsheet.com/'))

check_url('http://filldb.info/')
check_url('https://ru.wikipedia.org/')
