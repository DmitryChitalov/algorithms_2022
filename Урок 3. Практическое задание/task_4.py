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

memory = {}


def check_url(data):
    if memory.get(data) is None:
        memory[data] = hashlib.sha512(data.encode() + uuid4().bytes).hexdigest()
        return f'url добавлен в хэш'
    else:
        return f'Хэш  {data} : {memory.get(data)}'


url = 'ya.ru'
url2 = 'ya.ru'
url3 = 'mail.ru'

print(check_url(url))
print(check_url(url2))
print(check_url(url3))
