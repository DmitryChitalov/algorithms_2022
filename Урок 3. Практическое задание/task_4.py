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


kash_dict = {}

def kash_hash(url):
    if url in kash_dict:
        return f'Хэш url-a: {kash_dict[url]}'
    else:
        for_url = bytes(url, encoding='utf-8')
        salt = bytes(url[::-1], encoding='utf-8')
        hash_url = hashlib.sha512(salt + for_url).hexdigest()
        kash_dict[url] = hash_url
        return f'{url} - добавлен в кэш'



print(kash_hash('https://ya.ru'))
print(kash_hash('https://google.ru'))
print(kash_hash('https://mail.ru'))
print(kash_hash('https://ya.ru'))
