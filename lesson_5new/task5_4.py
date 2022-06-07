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
my_ordered_dict = OrderedDict()


def add_dict(i_dict):
    for i in range(1000):
        i_dict[i] = i
    return i_dict


def add_ordered_dict(i_ordered_dict):
    for i in range(1000):
        i_ordered_dict[i] = i
    return i_ordered_dict


print(timeit('add_dict(my_dict)', globals=globals(), number=1000))
print(timeit('add_ordered_dict(my_ordered_dict)', globals=globals(), number=1000))


# Время выполенения 0.06811379990540445
# Время выполенения 0.13956880010664463

def get_dict(i_dict):
    for i in range(1000):
        i = i_dict.get(i)
    return


def get_ordered_dict(i_ordered_dict):
    for i in range(1000):
        i = i_ordered_dict.get(i)
    return


print(timeit('get_dict(my_dict)', globals=globals(), number=1000))
print(timeit('get_ordered_dict(my_ordered_dict)', globals=globals(), number=1000))


# Время выполенения 0.061777699971571565
# Время выполенения 0.06683879997581244

def setdef_dict(i_dict):
    for i in range(1000):
        i = i_dict.setdefault(i)
    return


def setdef_ordered_dict(i_ordered_dict):
    for i in range(1000):
        i = i_ordered_dict.setdefault(i)
    return


print(timeit('setdef_dict(my_dict.copy())', globals=globals(), number=1000))
print(timeit('setdef_ordered_dict(my_ordered_dict.copy())', globals=globals(), number=1000))


# Время выполенения 0.09511650004424155
# Время выполенения 0.19893419998697937


def pop_dict(i_dict):
    for i in range(1000):
        i_dict.pop(i)
    return


def pop_ordered_dict(i_ordered_dict):
    for i in range(1000):
        i_ordered_dict.pop(i)
    return


print(timeit('pop_dict(my_dict.copy())', globals=globals(), number=1000))
print(timeit('pop_ordered_dict(my_ordered_dict.copy())', globals=globals(), number=1000))
# Время выполенения 0.08359299995936453
# Время выполенения 0.2699134999420494

# Использование OrderedDict не дает временного преимущества, не целесообразно