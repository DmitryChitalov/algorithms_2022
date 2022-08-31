"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


obj_dict = {x: x+1 for x in range(10000)}
ordered_dict = OrderedDict({x: x+1 for x in range(10000)})


def popitem_dict():
    obj_dict.popitem()


def popitem_od():
    ordered_dict.popitem()


def pop_dict(n):
    obj_dict.pop(n)


def pop_od(n):
    ordered_dict.pop(n)


print(timeit("popitem_dict()", globals=globals(), number=1000))
print(timeit("popitem_od()", globals=globals(), number=1000))
print(timeit("for i in range(1000):" "pop_dict(i)", globals=globals(), number=1))
print(timeit("for i in range(1000):" "pop_od(i)", globals=globals(), number=1))

"""
OrderedDict чуть медленнее чем обычный словарь, после версии Python 3.6 - OD становится не актуален
"""
