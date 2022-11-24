"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib

hash_dict = {}


def caching_url(url, cache):
    salt = 'sha512'
    res = hashlib.sha512(url.encode() + salt.encode()).hexdigest()
    if cache.get(url):
        print(f'Хеш {url} уже есть в кэше. Его хеш: {cache[url]}')
    else:
        cache[url] = res
        print(f'Хеш {url} добавлен в кэш.')


if __name__ == "__main__":
    caching_url('https://google.com/', hash_dict)
    caching_url('https://yandex.ru/', hash_dict)
    caching_url('https://google.com/', hash_dict)
