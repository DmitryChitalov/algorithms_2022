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

url = input('Введите URL:')

kash = {'10dd6e016c6ddd709c730ea8db557c20a6e5a2558d5b73178bc68797bbb22e19': 'gb.ru'}


def chek_url(u):
    hash_u = hashlib.sha256(u.encode()).hexdigest()
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



import hashlib
from uuid import uuid4

salt = uuid4().hex
cache_obj = {}


def get_page(url):
    if cache_obj.get(url):
        print(f'Данный адрес: {url} присутсвует в кэше')
    else:
        res = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_obj[url] = res
        print(cache_obj)


get_page('https://gb.ru/')
