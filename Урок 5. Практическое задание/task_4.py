"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import timeit
from collections import OrderedDict

dct = {}
dct_ordered = OrderedDict()
n = 10 ** 4


def fill_dct(dct):
    for i in range(n):
        dct[i] = i
        return dct


def change_iter_dct(dct):
    for k, v in dct.items():
        dct[k] = 'hello'


def change_dct(dct):
    for j in range(n - 2000, n - 1000):
        dct[j] = 'bye'


print('Fill:')
print(timeit('fill_dct(dct)', globals=globals(), number=1000))
print(timeit('fill_dct(dct_ordered)', globals=globals(), number=1000))

print('Change_iter:')
print(timeit('change_iter_dct(dct)', globals=globals(), number=1000))
print(timeit('change_iter_dct(dct_ordered)', globals=globals(), number=1000))

print('Change:')
print(timeit('change_dct(dct)', globals=globals(), number=1000))
print(timeit('change_dct(dct_ordered)', globals=globals(), number=1000))

"""
Fill:
0.00020150000273133628
0.00020489999951678328
Change_iter:
0.00014680000094813295
0.0001843999998527579
Change:
0.0328098999998474
0.0506013999984134
"""

"""
Смысла в OrderDict нет наоборот тратит больше времени, но если только в том случае, если порядок элементов нам не важен
"""