"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from time import time
from collections import OrderedDict


def measure_time(some_func):
    def wrapper(*args, **kwargs):
        start = time()
        result = some_func(*args, **kwargs)
        print(f'Время выполнения = {time() - start}.')
        return result
    return wrapper


some_dict = {}
ordered_dict = OrderedDict()
n = 10 ** 7


@measure_time
def fill_dict(dict, n):
    for i in range(n):
        dict[i] = i


@measure_time
def mod_dict(dict):
    for i in range(int(0.5 * n)):
        dict.pop(i)
    for j in range(0, n):
        dict[j] = 'lorem ipsum'
    for k, v in dict.items():
        dict[k] = 'some new value'


print('Заполнение. Обычный словарь:')
fill_dict(some_dict, n)
print('Заполнение. Упорядоченный словарь:')
fill_dict(ordered_dict, n)

print('Изменение. Обычный словарь:')
mod_dict(some_dict)
print('Изменение. Упорядоченный словарь:')
mod_dict(ordered_dict)


"""
Выводы:
Заполнение обычного словаря быстрее по 2 причинам:
1. OrderedDict реализован на чистом Python, обычный dict - на C
2. Упорядоченный словарь делает больше "работы" во время вставки, потому что на ходу переупорядочивает словарь.

При изменении обычный словарь также намного быстрее, чем упорядоченный

"""
