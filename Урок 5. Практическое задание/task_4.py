"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


def ord_dict_app(count):
    my_ord_dict = OrderedDict()
    for i in range(count):
        my_ord_dict[i] = f'{i}-й элемент'
    return my_ord_dict


def dict_append(count):
    my_dict = {}
    for i in range(count):
        my_dict[i] = f'{i}-й элемент'
    return my_dict


counts = 100
ord_dict = ord_dict_app(counts)
new_dict = dict_append(counts)

# print(f'Добавление в OrderedDict: {timeit("ord_dict_app(counts)",globals=globals())}')
# print(f'Добавление в Dict: {timeit("dict_append(counts)",globals=globals())}')
"""
Добавление в OrderedDict: 41.79986500000814
Добавление в Dict: 33.96403490001103
В обычный словарь элементы добавляются быстрее
"""


def pop_ord_dict(count):
    my_ord_dict = ord_dict.copy()
    for i in range(count):
        my_ord_dict.pop(i)


def pop_dict(count):
    my_dict = new_dict.copy()
    for i in range(count):
        my_dict.pop(i)


# print(f'Удаление элементов из OrderedDict: {timeit("pop_ord_dict(counts)",globals=globals())}')
# print(f'Удаление элементов из Dict: {timeit("pop_dict(counts)",globals=globals())}')
"""
Удаление элементов из OrderedDict: 34.96224429999711
Удаление элементов из Dict: 12.313148200017167
Удаление из обычного словаря происходит значительно быстрее, чем из OrderedDict
"""


def items_ord_dict():
    i = 0
    j = 0
    for key, val in ord_dict.items():
        i = key
        j = val
    return i, j


def items_dict():
    i = 0
    j = 0
    for key, val in new_dict.items():
        i = key
        j = val
    return i, j


print(f'Получение элементов из OrderedDict: {timeit("items_ord_dict()",globals=globals())}')
print(f'Получение элементов из Dict: {timeit("items_dict()",globals=globals())}')
"""
Получение элементов из OrderedDict: 13.332228500017663
Получение элементов из Dict: 6.248382699996
Из обычного словаря гораздо быстрее происходит получение элементов
"""
