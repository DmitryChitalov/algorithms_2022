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
for i in range(100000):
    my_dict[i] = i
my_OrderedDict = OrderedDict()
for i in range(100000):
    my_OrderedDict[i] = i


def change_dict(dct):
    for x in range(10001, 20000):
        dct[x] = x
    for key, value in dct.items():
        dct[key] = 'new_value'


def change_ordereddict(dct):
    for x in range(10001, 20000):
        dct[x] = x
    for key, value in dct.items():
        dct[key] = 'new_value'


print(timeit('change_dict(my_dict)', globals=globals(), number=100))
print(timeit('change_ordereddict(my_OrderedDict)', globals=globals(), number=100))

"""
с версии 3.6 есть смысл применять OrderedDict только ради специфических функций
move_to_end(key, last=True) и popitem(last=True).
В остальном обычные словари работают гораздо быстрее
"""
