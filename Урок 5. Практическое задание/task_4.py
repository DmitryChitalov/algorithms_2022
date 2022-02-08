"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {}
my_ordereddict = OrderedDict()


def fill_dict(c_dict):
    for i in range(100):
        c_dict[i] = i + 1
    return c_dict


def dict_get(c_dict):
    for i in range(100):
        return c_dict.get(i)


def dict_values(c_dict):
    for i in range(100):
        return c_dict.values

def dict_popitem(c_dict):
    for i in range(len(c_dict)):
        c_dict.popitem()
    return c_dict


print(fill_dict(my_dict))
print(fill_dict(my_ordereddict))

print(timeit("fill_dict(my_dict)", globals=globals(), number=1000))                 # 0.007513900000000004
print(timeit("fill_dict(my_ordereddict)", globals=globals(), number=1000))          # 0.009903200000000001

print(timeit("dict_get(my_dict)", globals=globals(), number=1000))                  # 0.00038040000000000296
print(timeit("dict_get(my_ordereddict)", globals=globals(), number=1000))           # 0.00038699999999999846

print(timeit("dict_popitem(my_dict)", globals=globals(), number=1000))              # 0.0003615000000000007
print(timeit("dict_popitem(my_ordereddict)", globals=globals(), number=1000))       # 0.0003530000000000061

print(timeit("dict_values(my_dict)", globals=globals(), number=1000))              # 0.00040719999999999645
print(timeit("dict_values(my_ordereddict)", globals=globals(), number=1000))       # 0.0004038999999999848

# время наполнения словаря меньше, чем время наполнения OrderedDict,
# при этом скорость выполнения других операций в Pyton 3.9 одинакова,
# поэтому использование OrderedDict в Python 3.6 и более поздних версиях не имеет смысла
