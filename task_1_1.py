"""
Курс: Алгоритмы и структуры данных на Python. Базовый курс
Урок: 3
Задание: 4
-----------------------------------------------------------------------------
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
from memory_profiler import memory_usage

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

def get_hash(salt, url):
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest()

##############################################################################
"""
ИСХОДНОЕ РЕШЕНИЕ

Последовательность ввода значений:
https://numpy.org --> https://numpy.org --> https://www.multitran.com --> https://gb.ru

Используемая память: 0.03515625 Mib
"""

@decor
def origin():
    dct_url = {}
    salt = '404 not found'
    while True:
        url = input('Введите url-адрес: ')
        if url == 'stop':
            break
        elif dct_url.get(url):
            print(dct_url[url])
        else:
            dct_url[url] = get_hash(salt, url)


print('---> ИСХОДНОЕ РЕШЕНИЕ')
res, mem_diff = origin()
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')


##############################################################################
"""
ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ

Описание: для хранения кэша вместо словаря - <class 'dict'>
---> {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
используется массив из библиотеки numpy - <class 'numpy.ndarray'>
---> [['url-адрес' 'хеш url-а'], ['url-адрес' 'хеш url-а']]

Последовательность ввода значений:
https://numpy.org --> https://numpy.org --> https://www.multitran.com --> https://gb.ru

Используемая память: 0.0 Mib
"""

@decor
def optimize():
    arr_url = np.vander([], 2)  # определяем пустой 2-мерный массив вместо словаря
    salt = '404 not found'
    while True:
        url = input('Введите url-адрес: ')
        if url == 'stop':
            break
        i, = np.where(arr_url[:, 0] == url)
        if i.size > 0:
            print(arr_url[int(i),1])
        else:
            np.append(arr_url, [[url,  get_hash(salt, url)]], axis=0)

print('---> ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ')
res, mem_diff = origin()
print('----------------------------------')
print(f'Выполнение заняло {mem_diff} Mib')
print('----------------------------------')