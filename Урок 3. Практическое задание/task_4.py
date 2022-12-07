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
encrypt = str(uuid4())
url_arr = {}
def go_web_cash():
    while True:
        value = input('Add url: ')
        url_hash = add_url(value)
        if url_hash == "":
            print('Added web url to memory.')
        else:
            print(f'This url  in  memory \n{url_hash}')
def add_url(value: str):
    if value in url_arr:
        return url_arr[value]
    else:
        new_arr_cash = hashlib.sha512((value + encrypt).encode('utf-8')).hexdigest()
        url_arr[value] = new_arr_cash
        return ""
go_web_cash()