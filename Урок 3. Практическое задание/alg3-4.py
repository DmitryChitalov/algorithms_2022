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
import json

salt = 'Hello'
cache_obj = {}

def chek_url(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутствует в кэше')

    else:
        res = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(json.dumps(cache_obj, indent=0, sort_keys=True))


chek_url('https://geekbrains.ru/')
chek_url('https://geekbrainsss.ru/')

chek_url('https://geekbrains.ru/')
