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


mport hashlib

url = {}
salt = 'mysalt'


def update_hesh(url_adr):
    if url_adr in url:
        return url[url_adr]
    else:
        new_hesh = hashlib.sha512(salt.encode() + url_adr.encode()).hexdigest()
        url[url_adr] = new_hesh
        return True


print(update_hesh('https://www.google.com'))

print(update_hesh('https://www.google.com'))

