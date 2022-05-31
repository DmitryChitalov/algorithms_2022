"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

simple_dict = {}
order_dict = OrderedDict()


def append_dict():
    for i in range(10000):
        simple_dict[i] = i


def append_ord_dict():
    for i in range(10000):
        order_dict[i] = i


print(timeit(append_dict, number=1000))  # 0.7
print(timeit(append_ord_dict, number=1000))  # 0.8


def get_val_dict():
    for k in simple_dict:
        simple_dict.get(k)


def get_val_ord_dict():
    for k in simple_dict:
        order_dict.get(k)


print(timeit(get_val_dict, number=1000))  # 0.4
print(timeit(get_val_ord_dict, number=1000))  # 0.5


def popitem_dict():
    simple_dict_copy = simple_dict.copy()
    for k in range(1000):
        simple_dict_copy.popitem()


def popitem_ord_dict():
    order_dict_copy = order_dict.copy()
    for k in range(1000):
        order_dict_copy.popitem()


print(timeit(popitem_dict, number=1000))  # 0.08
print(timeit(popitem_ord_dict, number=1000))  # 0.7

'''
Смысла использовать OrderedDict в Python 3.6 и более поздних версиях практически нет,
но метод popitem() меня заинтересовал, т.к. там есть параметр last,
который позволяет удалить последний элемент словаря.
'''
