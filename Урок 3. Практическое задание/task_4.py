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

# Функция uuid4() модуля uuid генерирует случайный UUID и возвращает объект UUID.
# Для преобразования объекта UUID в строку используйте встроенную функцию str().

from hashlib import sha256
from uuid import uuid4

salt = uuid4().hex
cache_obj = {}


def check_cache(url):
    hash_url = sha256(salt.encode() + url.encode()).hexdigest()
    if hash_url in cache_obj.keys():
        return True
    else:
        return {hash_url: url}


url_1 = input('Введите url: ')
check_cache(url_1)

try:
    cache_obj.update(check_cache(url_1))
except TypeError:
    print("Данная страница уже есть в кэше")

print(cache_obj)

url_2 = input('Введите url: ')
check_cache(url_2)

try:
    cache_obj.update(check_cache(url_2))
except TypeError:
    print("Данная страница уже есть в кэше")

print(cache_obj)
