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

cache = dict()
salt = 'veritas'


# Алгоритм хеширования выбрала sha512 по Вашей подсказке. Т.к. кол-во символов для url-страницы большое.
def caching_url(cache, url):
    return cache.setdefault(url, hashlib.sha512(url.encode() + salt.encode()).hexdigest())


print(caching_url(cache, 'https://habr.com/ru/post/321510/'))
print(caching_url(cache, 'https://gb.ru/lessons/260942'))
print(caching_url(cache, 'https://4pda.to/forum/index.php?act=idx'))
print(cache)
print(caching_url(cache, 'https://github.com/'))
