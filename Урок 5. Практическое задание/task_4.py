"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

n = 100
ordinary_dict = {}
ordered_dict = OrderedDict()


def test_1_ordinary(num):
    for i in range(n):
        ordinary_dict[i] = i


def test_1_ordered(num):
    for i in range(n):
        ordered_dict[i] = i


print(f'Время выполнения функции test_1_ordinary = {timeit("test_1_ordinary(n)", globals=globals(), number=10000)}')
print(f'Время выполнения функции test_1_ordered = {timeit("test_1_ordered(n)", globals=globals(), number=10000)}')


"""
Время выполнения функции test_1_ordinary = 0.05769730000000001
Время выполнения функции test_1_ordered = 0.0836299
"""


def test_2_ordinary(num):
    for i in range(n):
        ordinary_dict[i] = i ** 2


def test_2_ordered(num):
    for i in range(n):
        ordered_dict[i] = i ** 2


print(f'Время выполнения функции test_2_ordinary = {timeit("test_2_ordinary(n)", globals=globals(), number=10000)}')
print(f'Время выполнения функции test_2_ordered = {timeit("test_2_ordered(n)", globals=globals(), number=10000)}')

"""
Время выполнения функции test_2_ordinary = 0.4033707999999999
Время выполнения функции test_2_ordered = 0.3983774000000001
"""


def test_3_ordinary():
    for i in range(len(ordinary_dict)):
        ordinary_dict.pop(i)


def test_3_ordered():
    for i in range(len(ordered_dict)):
        ordered_dict.pop(i)


print(f'Время выполнения функции test_3_ordinary = {timeit("test_3_ordinary()", globals=globals(), number=10000)}')
print(f'Время выполнения функции test_3_ordered = {timeit("test_3_ordered()", globals=globals(), number=10000)}')
"""
Время выполнения функции test_3_ordinary = 0.0024671000000000554
Время выполнения функции test_3_ordered = 0.002377700000000038
"""


"""
Выводы:
По замерам понятно что смысла исп-ть OrderedDict в Python 3.6 и более поздних версиях нет.
"""