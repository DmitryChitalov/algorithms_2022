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

from uuid import uuid4
import hashlib

salt = uuid4().hex
cache_lst = {}


def web_cache(url):
    if cache_lst.get(url):
        print(f'{url} есть в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_lst[url] = res
        print(cache_lst)


if __name__ == '__main__':
    web_cache('https://gb.ru')
    web_cache('https://gb.ru')
    web_cache('https://gb.ru/lessons/260943')
