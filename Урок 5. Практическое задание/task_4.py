"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit
from random import randint

lst = [n * randint(1, 10) for n in range(1,  1000)]
simple_dict = dict()
ordered_dict = OrderedDict()

for i in lst:
    simple_dict.setdefault(i, i)

simple_dict_set = """
for i in lst:
    simple_dict.setdefault(i, i)"""

print(timeit(simple_dict_set, globals=globals(), number=10000), 'dict_set')

for i in lst:
    ordered_dict.setdefault(i, i)

ordered_dict_set = """
for i in lst:
    ordered_dict.setdefault(i, i)"""

print(timeit(ordered_dict_set, globals=globals(), number=10000), 'ordered_dict_set')

for i in simple_dict:
    simple_dict.get(i)

simple_dict_get = """
for i in range(1, 1000):
    simple_dict.get(i)"""

print(timeit(simple_dict_get, globals=globals(), number=10000), 'simple_dict_get')

for i in ordered_dict:
    ordered_dict.get(i)

ordered_dict_get = """
for i in range(1, 1000):
    ordered_dict.get(i)"""

print(timeit(ordered_dict_get, globals=globals(), number=10000), 'ordered_dict_get')

for i in simple_dict:
    simple_dict[i] = 1

simple_dict_change_el = """
for i in simple_dict:
    simple_dict[i] = 1"""

print(timeit(simple_dict_change_el, globals=globals(), number=10000), 'simple_dict_change_el')

for i in simple_dict:
    ordered_dict[i] = 1

ordered_dict_change_el = """
for i in simple_dict:
    ordered_dict[i] = 1"""

print(timeit(ordered_dict_change_el, globals=globals(), number=10000), 'ordered_dict_change_el')

while simple_dict:
    simple_dict.popitem()

simple_dict_pop = """
while simple_dict:
    simple_dict.popitem()"""

print(timeit(simple_dict_pop, globals=globals(), number=10000), 'simple_dict_popitem')

while ordered_dict:
    ordered_dict.popitem()

ordered_dict_pop = """
while simple_dict:
    ordered_dict.popitem()"""

print(timeit(ordered_dict_pop, globals=globals(), number=10000), 'ordered_dict_popitem')

# 0.5369257000274956 dict_set
# 0.5574484001845121 ordered_dict_set
# 0.5250731001142412 simple_dict_get
# 0.552956499857828 ordered_dict_get
# 0.3583094000350684 simple_dict_change_el
# 0.45563089987263083 ordered_dict_change_el
# 0.00016870000399649143 simple_dict_popitem
# 0.00017079990357160568 ordered_dict_popitem

# Вывод: в целом OrderedDict работает медленнее обычного словаря,
# Нет необходимости исползовать OrderedDict в обычных ситуациях, кроме случаев
# где требуется контроль очередности заполнения элементов

