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
from hashlib import pbkdf2_hmac
from uuid import uuid4


def memorize(url, memory={}):
    url_hash = memory.get(url)
    if url_hash is None:
        salt = uuid4().hex.encode()
        memory[url] = pbkdf2_hmac(hash_name='sha512', password=url.encode(), salt=salt, iterations=10000)
        print(f'{url} добавлен в кэш')
    else:
        print(memory[url])


memorize('vk.com')
memorize('gb.ru')
memorize('gb.ru')
memorize('www.ya.ru')
