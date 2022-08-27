"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

ordinary_dict = {}
ordered_dict = OrderedDict()


def create_ordinary_dict():
    for i in range(1, 10000):
        ordinary_dict[i] = i + 1
    return ordinary_dict


def create_ordered_dict():
    for i in range(1, 10000):
        ordered_dict[i] = i + 1
    return ordered_dict


print(
    timeit("create_ordinary_dict()", globals=globals(), number=1000))  # 0.551315 - заполняется быстрее, чем OrderedDict
print(timeit("create_ordered_dict()", globals=globals(), number=1000))  # 0.7332737


def ordinary_dict_change():
    for i in ordinary_dict.keys():
        ordinary_dict[i] = 'val'
    map(ordinary_dict.pop, [i for i in range(100)])
    return ordinary_dict


def ordered_dict_change():
    for i in ordered_dict.keys():
        ordered_dict[i] = 'val'
    map(ordered_dict.pop, [i for i in range(100)])
    return ordered_dict


print(timeit("ordinary_dict_change()", globals=globals(),
             number=1000))  # 0.28774710000000003 - операции с обычным словарем выполняются быстрее, чем OrderedDict
print(timeit("ordered_dict_change()", globals=globals(), number=1000))  # 0.4711966000000001
# Использовать OrderedDict имеет смысл, если важен порядок элементов в словаре,
# нужно переставить или переупорядочить элементы в словаре,
# если необходимо проверить словари на предмет равенства, и порядок элементов важен в этом сравнении.
# В остальных случаях использовать OrderedDict неэффективно.
