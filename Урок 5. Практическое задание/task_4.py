"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def dict_fill():
    my_dict = {1: 1, 2: 2, 3: 3}


def ordered_dict_fill():
    my_ordered_dict = OrderedDict([(1, 1), (2, 2), (3, 3)])


def dict_pop():
    my_dict = {'a': 1}
    my_dict.popitem()


def ordered_dict_pop():
    my_ordered_dict = OrderedDict({'a': 1})
    my_ordered_dict.popitem()


def dict_sort():
    my_dict = {'a': 1, 'c': 3, 'b': 2}
    my_list = sorted(my_dict)


def ordered_dict_sort():
    my_dict = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    my_list = sorted(my_dict)


print("dict test")
print(timeit("dict_fill()", globals = globals(), number=100000))
print(timeit("dict_pop()", globals = globals(), number=100000))
print(timeit("dict_sort()", globals = globals(), number=100000))
print("ordered dict test")
print(timeit("ordered_dict_fill()", globals = globals(), number=100000))
print(timeit("ordered_dict_pop()", globals = globals(), number=100000))
print(timeit("ordered_dict_sort()", globals = globals(), number=100000))
#
# dict test
# 0.014466800000000009
# 0.012963299999999997
# 0.032481800000000005
# ordered dict test
# 0.049329200000000004
# 0.0476415
# 0.07421069999999999


# По скорости обычный словарь работает быстрее
# Начиная с версии 3.6 применять OrderedDict не имеет смысла, данный функционаял уже реализован в обычном словаре и
# лучшую производительность.