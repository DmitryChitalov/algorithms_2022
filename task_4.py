from collections import OrderedDict
from timeit import timeit
from random import randint

keys_values = [i for i in range(500)]
simple_dict = {}
ordered_dict = OrderedDict()

# Заполнение словарей


def fill_simple_dict(simple_dict):
    for i in keys_values:
        simple_dict[i] = i
    return simple_dict


def fill_ordered_dict(ordered_dict):
    for i in keys_values:
        ordered_dict[i] = i
    return ordered_dict


# Замеры времени
# print(timeit('fill_simple_dict(simple_dict)', globals=globals()))
# print(timeit('fill_ordered_dict(ordered_dict)', globals=globals()))

"""
54.416168199999994
76.48371530000001
"""

# Изменение ключей-значений словаря


def change_simple_dict(simple_dict):
    for i in simple_dict.keys():
        simple_dict[i] = randint(0, 100)
    return simple_dict


def change_ordered_dict(ordered_dict):
    for i in ordered_dict.keys():
        simple_dict[i] = randint(0, 100)
    return ordered_dict


# Замеры времени


print(timeit('change_simple_dict(simple_dict)', globals=globals()))
print(timeit('change_ordered_dict(ordered_dict)', globals=globals()))

"""
0.4449611
0.5320864000000001
"""

# Удаление элементов словарей


def pop_items_from_simple_dict(simple_dict):
    for i in simple_dict.keys():
        simple_dict.pop(i)
    return simple_dict


def pop_items_from_ordered_dict(ordered_dict):
    for i in ordered_dict.keys():
        ordered_dict.pop(i)
    return ordered_dict


# Замеры времени
print(timeit('pop_items_from_simple_dict(simple_dict)', globals=globals()))
print(timeit('pop_items_from_ordered_dict(ordered_dict)', globals=globals()))

"""
0.43857040000000014
0.5342665999999998
"""

"""
Как можно увидеть из полученных замеров, простой словарь работает заметно быстрее упорядоченного.
Учитывая, что в последних версиях Python, обычный словарь тоже помнит порядок добавления элементов,
нет необходимости в использовании упорядоченного словаря.
