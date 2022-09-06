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
import uuid


def cash_addr(addr, cash):
    """
    Кэширование url-адресов
    """
    # addr_url = input('Введите url-адрес: ')
    if cash.get(addr):
        return f'Адрес {addr} уже в кэше: {cash[addr][1]}'
    cash[addr] = []
    cash[addr].append(uuid.uuid4().hex)
    cash[addr].append(hashlib.sha512(cash[addr][0].encode() + addr.encode()).hexdigest())
    return f'Заносим адрес {addr} в кэш: {cash[addr][1]}'


cash_dict = {}
print(cash_addr('http://mail.ru', cash_dict))
print(cash_addr('http://mail.ru', cash_dict))
print(cash_addr('http://gb.ru', cash_dict))
print(cash_addr('http://ya.ru', cash_dict))
