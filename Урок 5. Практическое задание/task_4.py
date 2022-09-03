"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {}
ord_dict = OrderedDict()


def append_dict():
    for i in range(10000):
        my_dict[i] = i


def append_ord_dict():
    for i in range(10000):
        ord_dict[i] = i


print(f'Добавление словаря: {timeit(append_dict, number=1000)}')
print(f'Добавление упорядоченного словаря: {timeit(append_ord_dict, number=1000)}')


def get_val_dict():
    for k in my_dict:
        my_dict.get(k)


def get_val_ord_dict():
    for k in ord_dict:
        ord_dict.get(k)


print(f'Получение значений словаря: {timeit(get_val_dict, number=1000)}')
print(f'Получение значений упорядоченного словаря: {timeit(get_val_ord_dict, number=1000)}')


def popitem_dict():
    simple_dict_copy = my_dict.copy()
    for k in range(1000):
        simple_dict_copy.popitem()


def popitem_ord_dict():
    order_dict_copy = ord_dict.copy()
    for k in range(1000):
        order_dict_copy.popitem()


print(f'Удаление элементов из словаря: {timeit(popitem_dict, number=1000)}')
print(f'Удаление элементов из упорядоченного словаря: {timeit(popitem_ord_dict, number=1000)}')