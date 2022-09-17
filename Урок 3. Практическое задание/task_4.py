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
salt = 'my_salt'
def func(adress, dct={}):
    try:
        return dct[adress]
    except KeyError:
        dct.update({adress: hashlib.sha512(adress.encode() + salt.encode()).hexdigest()})
        return "Хеш вычислен и записан в кеш!!"

print(func("https://yandex.ru/"))
print(func("https://yandex.ru/"))
print(func("https://gb.ru/"))

import hashlib
salt = 'my_salt'
def func(adress, dct={}):
    return dct.setdefault(adress, hashlib.sha512(adress.encode() + salt.encode()).hexdigest())

print(func('https://gb.ru/'))
print(func('https://gb.ru/'))
print(func('https://yandex.ru/'))
print(func('https://yandex.ru/'))