"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

o_dct = OrderedDict()
dct = {}


def o_dct_fill():
    global o_dct
    o_dct = {i: i for i in range(1000000)}


def dct_fill():
    global dct
    dct = {i: i for i in range(1000000)}


def o_dct_pop(d):
    for key in d.copy().keys():
        d.pop(key)


def dct_pop(d):
    for key in d.copy().keys():
        d.pop(key)


def o_dct_get(d):
    for key in d.keys():
        d.get(key)


def dct_get(d):
    for key in d.keys():
        d.get(key)


def o_dct_item(d):
    for key, val in d.items():
        pass


def dct_item(d):
    for key, val in d.items():
        pass


def o_dct_popitem(d):
    while len(d) > 0:
        d.popitem()


def dct_popitem(d):
    while len(d) > 0:
        d.popitem()


print(f'Время работы функции {o_dct_fill.__name__} - {timeit("o_dct_fill()", globals=globals(), number=10)}')
print(f'Время работы функции {dct_fill.__name__} - {timeit("dct_fill()", globals=globals(), number=10)}')
print(f'Время работы функции {o_dct_pop.__name__} - {timeit("o_dct_pop(o_dct)", globals=globals(), number=100000)}')
print(f'Время работы функции {dct_pop.__name__} - {timeit("dct_pop(dct)", globals=globals(), number=100000)}')
print(f'Время работы функции {o_dct_get.__name__} - {timeit("o_dct_get(o_dct)", globals=globals(), number=1000)}')
print(f'Время работы функции {dct_get.__name__} - {timeit("dct_get(dct)", globals=globals(), number=1000)}')
print(f'Время работы функции {o_dct_item.__name__} - {timeit("o_dct_item(o_dct)", globals=globals(), number=1000)}')
print(f'Время работы функции {dct_item.__name__} - {timeit("dct_item(dct)", globals=globals(), number=1000)}')
print(f'Время работы функции {o_dct_popitem.__name__} - {timeit("o_dct_popitem(o_dct)", globals=globals(), number=100000)}')
print(f'Время работы функции {dct_popitem.__name__} - {timeit("dct_popitem(dct)", globals=globals(), number=100000)}')


"""

ЗАМЕРЫ

Время работы функции o_dct_fill - 1.9352168000041274
Время работы функции dct_fill - 1.9140021000057459
Время работы функции o_dct_pop - 0.29518639999150764
Время работы функции dct_pop - 0.2831632999877911
Время работы функции o_dct_get - 2.0643611999985296
Время работы функции dct_get - 2.0465689999982715
Время работы функции o_dct_item - 2.9313687999965623
Время работы функции dct_item - 2.6742691999970702
Время работы функции o_dct_popitem - 0.03841120000288356
Время работы функции dct_popitem - 0.037300899988622405

ВЫВОДЫ

Как показали замеры, обычный словарь немного быстрее, но критичной разности я не наблюдаю. Как я понял OrderedDict есть
смысл использовать когда очень важен порядкок элементов, в остальных случаях принципиальной разности нет.
"""