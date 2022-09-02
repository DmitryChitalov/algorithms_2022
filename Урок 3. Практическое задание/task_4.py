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
my_memory = {}
def my_hesh_cash(my_url):
    my_url_hash = hashlib.sha512(salt.encode() + my_url.encode()).hexdigest()
    if my_url in my_memory.keys():
        return f'[хеш url-a {my_url} есть в базе: {my_url_hash}'
    else:
        my_memory[my_url] = my_url_hash
        return f'Хэш url-a {my_url} добавлен в базу'

print(my_hesh_cash('mail.ru'))
print(my_hesh_cash('home.ru'))
print(my_hesh_cash('lenta.ru'))
print(my_hesh_cash('mail.ru'))
print(my_hesh_cash('home.ru'))
print(my_hesh_cash('lenta.ru'))