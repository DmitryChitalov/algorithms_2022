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


salt = uuid4().hex
cash_dict = {}


def url_page(url):
    if cash_dict.get(url):
        print(f'Хэш url {url} - {cash_dict[url]}')
    else:
        result = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cash_dict[url] = result
        print(cash_dict)


if __name__ == '__main__':
    url_page('https://gb.ru/lessons/260942/homework')
    url_page('https://gb.ru/lessons/260942/homework')
