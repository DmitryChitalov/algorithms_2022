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
from hashlib import sha256
from uuid import uuid4


def memorize(func):
    def wrapper(url, salt, memory={}):
        url_hash = memory.get(url)
        if url_hash is None:
            url_hash = func(url, salt)
            memory[url] = url_hash
            print(f'\nHash for {url} has been cached\n')
        return f'Hash of {url}: {url_hash}'
    return wrapper


@memorize
def url_cache_hash(url, salt):
    url_hash = sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    return url_hash


print(url_cache_hash('https://vk.com/im', 'uuid4().hex'))
print(url_cache_hash('https://gb.ru/education', uuid4().hex))
print(url_cache_hash('https://vk.com/im', uuid4().hex))
print(url_cache_hash('https://vk.com/im', uuid4().hex))
print(url_cache_hash('https://e.mail.ru/inbox/', uuid4().hex))
print(url_cache_hash('https://gb.ru/education', 'asd'))
print(url_cache_hash('https://gb.ru/education', uuid4().hex))
