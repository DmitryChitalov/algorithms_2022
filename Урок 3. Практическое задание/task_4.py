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
import uuid

def memorize(func):
    def g(n, memory={}):
        if n not in memory:
            r = func(n)
            memory[n] = r
            return 'нет такой страницы'
        else:
            return memory
    return g


@memorize
def f(url):
    salt = 'salt01'
    key = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    storage = salt + key
    return storage

                                # если возвращать memory[n]
print(f('http://www.abc.ru'))  #нет такой
print(f('http://www.abc.ru'))  #повторно вызываю, показывает хэш
print(f('http://www.abcd.ru')) #снова нет
print(f('http://www.qwerty.ru')) #нет
print(f('http://www.abcd.ru')) #хэш
print(f('http://www.qwerty.ru')) #хэш
                                  #если возвращать memory, то будет возвращать словарь на 1 элемент больше.