"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

num = range(10000)
dct = {i: i for i in num}
odct = OrderedDict(dct)


# получение


def dict_getting():
    for i in num:
        dct.get(i)


def odict_getting():
    for i in num:
        odct.get(i)


print('получение:')
print(f'dict: {timeit("dict_getting()", globals=globals(), number=1000)}')
print(f'OrderedDict: {timeit("odict_getting()", globals=globals(), number=1000)}')


# изменение


def dict_changing():
    for i in num:
        dct[i] = 0


def odict_changing():
    for i in num:
        odct[i] = 0


print('изменение:')
print(f'dict: {timeit("dict_changing()", globals=globals(), number=1000)}')
print(f'OrderedDict: {timeit("odict_changing()", globals=globals(), number=1000)}')


# удаление


def dict_deletion():
    dct_copy = dct.copy()
    for i in num:
        dct_copy.pop(i)


def odict_deletion():
    odct_copy = odct.copy()
    for i in num:
        odct_copy.pop(i)


print('удаление:')
print(f'dict: {timeit("dict_deletion()", globals=globals(), number=1000)}')
print(f'OrderedDict: {timeit("odict_deletion()", globals=globals(), number=1000)}')


# операции с OrderedDict занимают больше времени
# нет смысла использовать OrderedDict, т.к. дольше по времени и с версии 3.6 обычные словари тоже упорядочены
