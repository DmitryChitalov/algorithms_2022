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
from hashlib import sha512


def memorize(url, mem={}):
    url_hash = mem.get(url)
    if url_hash is None:
        salt = 'protection'
        mem[url] = sha512(salt.encode() + url.encode()).hexdigest()
        print(f'{url} записан в кэш с хешем {mem[url]}')
    else:
        print(f'{url} - уже в кэше и имеет хеш {mem[url]}')


print('Даём программе новые url:')
memorize('www.vk.com')
memorize('www.google.ru')
memorize('www.yandex.ru')
memorize('www.youtube.com')
print('Проверяем программу, дав уже известный url:')
memorize('www.yandex.ru')
