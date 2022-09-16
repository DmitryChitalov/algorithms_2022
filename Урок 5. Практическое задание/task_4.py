"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


some_dict = {}
some_ordered_dict = OrderedDict()

for i in range(50):
    some_dict[i] = i

for i in range(50):
    some_ordered_dict[i] = i


def fill_dict(some_dict):
    for j in range(51, 1000):
        some_dict[j] = j


def fill_ordered_dict(some_ordered_dict):
    for j in range(51, 1000):
        some_ordered_dict[j] = j


print(timeit("fill_dict(some_dict)", globals=globals(), number=1000))
print(timeit("fill_ordered_dict(some_ordered_dict)", globals=globals(), number=1000))

'''
0.0629968
0.17073739999999998
Обычный словарь заполняется быстрее
'''


def change_dict(some_dict):
    for j in range(50):
        some_dict[j] = j+1


def change_ordered_dict(some_ordered_dict):
    for j in range(50):
        some_ordered_dict[j] = j + 1


print(timeit("change_dict(some_dict)", globals=globals(), number=1000))
print(timeit("change_ordered_dict(some_ordered_dict)", globals=globals(), number=1000))
''' 
0.012369099999999966
0.023375900000000005
Замена элементов в обычном словаре происходит чуть быстрее
'''


def pop_dict(some_dict):
    for k in range(25):
        some_dict.popitem()


def pop_ordered_dict(some_ordered_dict):
    for k in range(25):
        some_ordered_dict.popitem()


print(timeit("pop_dict(some_dict)", globals=globals(), number=1))
print(timeit("pop_ordered_dict(some_ordered_dict)", globals=globals(), number=1))

'''
5.6400000000011996e-05
2.4299999999977118e-05
Удаление элементов из упорядоченного словаря просиходит намного быстрее, чем из обычного

С версии Python 3.6 обычный словарь так же, как и упорядоченный запомниаент порядок добавдения элементов(ключ: значение).
Поэтому упорядоченный словарь оправднно использовать, если нужны его специальные функции move_to_end(), popitem(last=True)
'''