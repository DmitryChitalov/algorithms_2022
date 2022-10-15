"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

key_values = [i for i in range(500)]
unordered_dict = {}
ordered_dict = OrderedDict()

# Заполнение словарей

def fill_unordered_dict(unordered_dict):
    for i in key_values:
        unordered_dict[i] = i
    return unordered_dict

def fill_ordered_dict(ordered_dict):
    for i in key_values:
        ordered_dict[i] = i
    return ordered_dict

print(timeit('fill_unordered_dict(unordered_dict)', globals=globals()))
print(timeit('fill_ordered_dict(ordered_dict)', globals=globals()))

"""
30.24810989998514
47.73105439997744
"""

# Копия словарей

def copy_unordered_dict(unordered_dict):
    test_dict = unordered_dict.copy()

def copy_ordered_dict(ordered_dict):
    test_dict = ordered_dict.copy()

print(timeit('copy_unordered_dict(unordered_dict)', globals=globals()))
print(timeit('copy_ordered_dict(ordered_dict)', globals=globals()))

"""
0.25826729997061193
0.3691518999985419
"""

# Удаление элементов словаря

def pop_from_ud(unordered_dict):
    for i in unordered_dict.keys():
        unordered_dict.pop(i)
    return unordered_dict

def pop_from_od(ordered_dict):
    for i in ordered_dict.keys():
        ordered_dict.pop(i)
    return ordered_dict

print(timeit('pop_from_ud(unordered_dict)', globals=globals()))
print(timeit('pop_from_od(ordered_dict)', globals=globals()))

"""
0.26318050001282245
0.3183615999878384
"""


"""
Вывод: OrderedDict работает существенное медленнее обычного словаря.
В последниях версиях Python неупорядоченный словать также, как и OrderedDict, помнит порядок добавления элементов,
поэтому нет особой необходимости в успользовании упорядоченного словаря"""