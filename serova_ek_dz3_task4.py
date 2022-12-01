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

url = input('Введите URL: ')

kash = {'ed3e6c152ca05e66ee16b6d0212dea8344e72c4bd57bb01e024b4040eebcca69': 'serial.ru',
        '877ca9b8dd0b5eebe0dd82437c136d98ff863d5710a77dbad227895c35e851ce': 'vk.com',
        'd0621fe28e3bc3028217d73972c12f0c35e6129ba403d28040c7389b6a015d2a': 'python.com'}


def chek_url(url):
    hash_url = hashlib.sha256(url.encode()).hexdigest()
    if hash_url in kash.keys():
        return True
    else:
        return {hash_url: url}


chek_url(url)

try:
    kash.update(chek_url(url))
except TypeError:
    for key, value in kash.items():
        if value == url:
           print("Такой объект уже есть в кэше, его хэш: ", key)

print(kash)
