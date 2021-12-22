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
from uuid import uuid4
import hashlib

def caching(func):
    def wrapper(url, cache={}):
        key = url
        if key not in cache:
            cache[key] = func(url)
        return cache[key]
    return wrapper

@ caching
def hashing(url):
    salt = uuid4().hex
    url_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
    print(f'Создан новый хэш')
    return url_hash


hash1 = hashing('https://gb.ru/')
hash2 = hashing('https://www.google.ru/?hl=ru')
hash3 = hashing('https://yandex.ru/')
hash4 = hashing('https://gb.ru/')
print()
print(hash1)
print(hash2)
print(hash3)
print(hash4)
