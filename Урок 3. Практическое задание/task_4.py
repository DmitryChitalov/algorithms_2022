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

from hashlib import sha512


def memorize(url, memory={}):
    url_hash = memory.get(url)
    if url_hash is None:
        salt = 'my_salt'
        memory[url] = sha512(salt.encode() + url.encode())
        print(f'{url} добавлен в кэш {memory[url]}')
    else:
        print(f'{url} - уже существует')


memorize('www.yandex.ru')
memorize('www.google.ru')
memorize('www.opera.ru')
memorize('www.google.ru')

