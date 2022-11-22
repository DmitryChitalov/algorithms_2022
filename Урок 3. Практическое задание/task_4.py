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
import binascii


cache = {}


def caching(url):
    if url in cache:
        print(f"Хеш {url}: {cache[url]}")
    else:
        hashed_url = binascii.hexlify(hashlib.pbkdf2_hmac(hash_name='sha256', password=url.encode(), salt=b'privet', iterations=3))
        cache[url] = hashed_url
        print(f"Хэш {url} добавлен в кэш")


caching('https://brat.ru/')
caching('https://brat.ru/')
caching('https://brat.ru/')
caching('https://panamka.ru/')
caching('https://delivery.ru/')


# print("Все кеши:")
# for k, v in cache.items():
#     print(f"{k}: {v}")
