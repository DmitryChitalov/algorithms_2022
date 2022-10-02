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

class url_hash():
    def __init__(self):
        self.dUrl = dict()

    def getHash(self, u):
        salt = uuid4().hex
        hsh = hashlib.sha256(salt.encode() + u.encode()).hexdigest()
        return u, salt, hsh

    def inCash(self, url : tuple):
        if self.dUrl.get(url[0], False):
            print(f'Такая страница уже есть. Ее хэш: {self.dUrl.get(url[0])[1]}')
        else:
            self.dUrl[url[0]] = (url[1], url[2])
            print(f'Такой страницы нет. Добавлен хэш: {(url[1], url[2])}')

url_class = url_hash()
res = input('Введите URL для проверки или none для выхода: ')
while res != 'none':
    tuple_solt_hash = url_class.getHash(res)
    url_class.inCash(tuple_solt_hash)
    res = input('Введите URL для проверки или none для выхода: ')

print(url_class.dUrl)