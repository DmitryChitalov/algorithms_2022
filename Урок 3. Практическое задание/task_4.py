"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib

salt = 'cache_salt'
url_cache = {}


def main():
    while True:
        url = input('Введите URL: ')
        res = cache_url(url)
        if res == "":
            print('Добавлено')
        else:
            print(f'Уже есть {res}')


def cache_url(url: str):
    if url in url_cache:
        return url_cache[url]
    else:
        url_hash = hashlib.sha256((url + salt).encode('utf-8')).hexdigest()
        url_cache[url] = url_hash
        return ""


if __name__ == '__main__':
    main()
