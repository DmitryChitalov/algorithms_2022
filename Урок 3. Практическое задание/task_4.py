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

memory = {}


def cash_web(url, mem):
    if url in mem:
        res = mem.get(url)
        return res
    else:
        res = hashlib.sha512('salt'.encode('utf-8') + url.encode('utf-8')).hexdigest()
        mem[url] = res


print(cash_web('https://gb.ru/lessons/259239', memory))
print(cash_web('https://mail.ru/', memory))
print(cash_web('https://yandex.ru/', memory))
print(cash_web('https://gb.ru/lessons/259239', memory))
print(cash_web('https://gb.ru/lessons/259239', memory))
print(cash_web('https://yandex.ru/', memory))
print(memory)

