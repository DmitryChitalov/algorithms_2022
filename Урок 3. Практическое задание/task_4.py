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


def generate_hash_passwd(salt, passwd):
    hash_passwd = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    return hash_passwd


def chek_cashe(url_address):
    # проверяем есть ли адрес в кэше
    if my_cashe.get(url_address) is None:
        # если есть, то надо вычислить хеш и записать в кэш
        print('Этого адреса нет в кэше.')
        my_cashe[url_address] = generate_hash_passwd('salt', url_address)
    else:
        print('Этот адрес уже есть в кэше.')
    result = my_cashe[url_address]
    print(result)
    return


my_cashe = {}
while True:
    url_address = input('Введите url: ')
    chek_cashe(url_address)
