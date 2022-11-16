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

from hashlib import sha512

cache_sites = {}


def cache_url(url):
    salt = "solaris"
    if cache_sites.get(url):
        print(f'Страница: {url} кеширована')
    else:
        res = sha512(url.encode() + salt.encode()).hexdigest()
        cache_sites[url] = res
        print(cache_sites)


cache_url("https://yandex.ru/search/?text=solaris&search_source=dzen_desktop_safe&lr=62")
cache_url("https://yandex.ru")
cache_url("https://yandex.ru/search/?text=solaris&search_source=dzen_desktop_safe&lr=62")
