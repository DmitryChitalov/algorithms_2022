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
from uuid import uuid4

salt = uuid4().hex
print(salt)
url = input('url: ')

cache_url = {'10dd6e016c6ddd709c730ea8db557c20a6e5a2558d5b73178bc68797bbb22e19': 'gb.ru'}


def chek_url(u):
    hash_u = hashlib.sha256(salt.encode() + u.encode()).hexdigest()

    if hash_u in cache_url.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    cache_url.update(chek_url(url))
except TypeError:
    print("Такой объект уже есть в кэше")

print(cache_url)
