"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict


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

# print(timeit('fill_unordered_dict(unordered_dict)', globals=globals()))
# print(timeit('fill_ordered_dict(ordered_dict)', globals=globals()))

"""
12.821962500001973
17.698497000001225
"""

# Копия словарей

def copy_unordered_dict(unordered_dict):
    test_dict = unordered_dict.copy()

def copy_ordered_dict(ordered_dict):
    test_dict = ordered_dict.copy()

print(timeit('copy_unordered_dict(unordered_dict)', globals=globals()))
print(timeit('copy_ordered_dict(ordered_dict)', globals=globals()))

"""
0.08535740000297665
0.10361689999990631
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
0.10212419999879785
0.13642949999848497
"""

"""Использование OrderedDict не имеет смысла, потому что работа с
OrderedDict заметно медленнее чем с Dict"""