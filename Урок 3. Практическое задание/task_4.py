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

url = input()

cache = {'https://www.youtube.com/': hashlib.sha512(uuid4().hex.encode() + b'https://www.youtube.com/').hexdigest(),
         'https://mail.google.com/': hashlib.sha512(uuid4().hex.encode() + b'https://mail.google.com/').hexdigest()}

if url in list(cache.keys()):
    print(cache[url])
else:
    cache[url] = hashlib.sha512(uuid4().hex.encode() + url.encode()).hexdigest()

# print(list(cache.keys()))
print(cache)
