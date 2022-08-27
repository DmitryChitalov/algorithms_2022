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
ordered_dict = OrderedDict()


def func_my_dict():
    for i in range(1, 10000):
        my_dict[i] = i + 1
    return my_dict


def func_ordered_dict():
    for i in range(1, 10000):
        ordered_dict[i] = i + 1
    return ordered_dict


print(
    timeit("func_my_dict()", globals=globals(), number=1000)) # 1.151253929
print(timeit("func_ordered_dict()", globals=globals(), number=1000)) # 1.3533036180000002

# обычный словарь заполняется быстрее но при использовании Ordereddict код проясняет,
# что порядок элементов в словаре важен, например, если необходимо сравнить словари,
# то Ordereddict правильный выбор.
