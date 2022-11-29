"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from timeit import timeit
from collections import OrderedDict


# Заполнение словарей

def fill_unordered_dict(unordered_dict):
    for i in key_values:
        unordered_dict[i] = i
    return unordered_dict


def fill_ordered_dict(ordered_dict):
    for i in key_values:
        ordered_dict[i] = i
    return ordered_dict


# Копия словарей

def copy_unordered_dict(unordered_dict):
    test_dict = unordered_dict.copy()


def copy_ordered_dict(ordered_dict):
    test_dict = ordered_dict.copy()


# Удаление элементов словаря

def pop_from_ud(unordered_dict):
    for i in list(unordered_dict.keys()):
        unordered_dict.pop(i)
    return unordered_dict


def pop_from_od(ordered_dict):
    for i in list(ordered_dict.keys()):
        ordered_dict.pop(i)
    return ordered_dict


key_values = [i for i in range(10**5)]
unordered_dict = {}
unordered_dict = fill_unordered_dict(unordered_dict)
ordered_dict = OrderedDict()
ordered_dict = fill_ordered_dict(ordered_dict)

print(timeit('fill_unordered_dict(unordered_dict)', globals=globals(), number=100))
print(timeit('fill_ordered_dict(ordered_dict)', globals=globals(), number=100))
"""
fill_unordered_dict: 3.1822425999853294
fill_ordered_dict: 4.568379700009245
"""

print(timeit('copy_unordered_dict(unordered_dict)', globals=globals(), number=100))
print(timeit('copy_ordered_dict(ordered_dict)', globals=globals(), number=100))
"""
copy_unordered_dict: 1.9332848000049125
copy_ordered_dict: 9.924188400007552
"""

print(timeit('pop_from_ud(unordered_dict)', globals=globals(), number=1000))
print(timeit('pop_from_od(ordered_dict)', globals=globals(), number=1000))


"""
pop_from_ud: 0.07717209999100305
pop_from_od: 0.01076830000965856
"""

"""OrderedDict в Python 3.6 и более поздних версиях не имеет смысла, 
так как результаты всех замеров в пользу обычного словаря.
"""