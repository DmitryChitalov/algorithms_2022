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
from hashlib import pbkdf2_hmac


def hash_url(input_url):
    input_url_hash = pbkdf2_hmac('sha256',
                                 password=(input_url.encode('UTF-8')),
                                 salt=b'bubu',
                                 iterations=10000)
    print(dict_url)
    if input_url_hash == dict_url.get(input_url):
        print(f'хеш-url: {input_url_hash}')
    else:
        dict_url.update({input_url: input_url_hash})
        print(dict_url)
        return hash_url(input('Введите URL: '))



dict_url = {}
hash_url(input('Введите URL: '))

