"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

"""
OrderedDict - работает медленней обычного словаря.   в Python 3.6 и более поздних версиях - нет смысла использовать OrderedDict
"""
import timeit
from collections import OrderedDict

dct = {i: 'i' for i in range(1000)}

ordered_dict = OrderedDict(dct)


def pop_dict(obj):
    obj.popitem()


def pop_n(obj):
    for i in range(len(obj)):
        obj.pop(i)


print(timeit.timeit('pop_dict(dct)', number=1000, globals=globals()))
print(timeit.timeit('pop_dict(ordered_dict)', number=1000, globals=globals()))

print(timeit.timeit('pop_n(dct)', number=10000, globals=globals()))
print(timeit.timeit('pop_n(ordered_dict)', number=10000, globals=globals()))
