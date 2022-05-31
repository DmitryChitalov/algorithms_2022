"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

n = 10 ** 4
data1= {}
data2 = OrderedDict()


def fill_dict(data1, n):
    for i in range(n):
        data1[i] = i


def fill_ordered_dict(data2, n):
    for i in range(n):
        data2[i] = i

print(timeit('fill_dict(data1.copy(), 10 ** 4)', globals=globals(), number=100))
print(timeit('fill_ordered_dict(data2.copy(), 10 ** 4)', globals=globals(), number=100))

"""
0.0837007
0.1273596

Судя по времени выполнения смысла использовать OrderedDict нет
"""