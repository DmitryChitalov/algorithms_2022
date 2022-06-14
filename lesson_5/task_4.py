"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def seed_simple_dict():
    for i in range(100):
        simple_dict[i] = f'value{i}'
    return simple_dict


def seed_ordered_dict():
    for i in range(100):
        ordered_dict[i] = f'value{i}'
    return ordered_dict


def get_values_dict():
    for i in range(100):
        return simple_dict.get(i)


def get_values_ordered():
    for i in range(100):
        return ordered_dict.get(i)


def simple_dict_items():
    return simple_dict.items


def ordered_dict_items():
    return ordered_dict.items


simple_dict = {}
ordered_dict = OrderedDict()

print(f'seed_simple_dict = {timeit("seed_simple_dict()", globals=globals(), number=10000)}')
print(f'seed_ordered_dict = {timeit("seed_ordered_dict()", globals=globals(), number=10000)}')
print(f'get_values_dict = {timeit("get_values_dict()", globals=globals())}')
print(f'get_values_ordered = {timeit("get_values_ordered()", globals=globals())}')
print(f'simple_dict_items = {timeit("simple_dict_items()", globals=globals())}')
print(f'ordered_dict_items = {timeit("ordered_dict_items()", globals=globals())}')

"""
seed_simple_dict = 0.21352539999999998
seed_ordered_dict = 0.22944170000000003
get_values_dict = 0.3146905
get_values_ordered = 0.3323802
simple_dict_items = 0.13427809999999996
ordered_dict_items = 0.12574850000000004

В целом операции в обычном словаре выполняются быстрее, чем в OrderedDict.
Нет смысла использовать OrderedDict в 3.6 и более поздних версиях.
"""
