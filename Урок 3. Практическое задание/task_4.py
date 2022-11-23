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

url = input('url')

kash = {'8008d168c5564201c09d2e1f58446990498116d893f37d6f1ab88955d4004253cab66bad0ff9975b9161b79ba6e37b4bf28a80d252100daca7ffa9ab825ad6b7': 'gb.ru'}
salt = uuid4().hex

def chek_url(u):
    hash_u = hashlib.sha512(salt.encode() + u.encode()).hexdigest()
    if hash_u in kash.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    kash.update(chek_url(url))
except TypeError:
    print("Такой объект уже есть в кэше")

print(kash)