"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100000)}
my_od = OrderedDict({i: i for i in range(100000)})


def add_dict():
    for i in range(100000, 300000):
        my_dict[i] = i


def add_od():
    for i in range(100000, 300000):
        my_od[i] = i


def red_dict():
    for i in range(100000, 300000):
        my_dict[i] = 0


def red_od():
    for i in range(100000, 300000):
        my_od[i] = 0


print('Добавление в dict: ', timeit('add_dict()', globals=globals(), number=100))
print('Добавление в Ordereddict: ', timeit('add_od()', globals=globals(), number=100))

print('Редактирование dict: ', timeit('red_dict()', globals=globals(), number=100))
print('Редактирование Ordereddict: ', timeit('red_od()', globals=globals(), number=100))

"""
Добавление в dict:  0.7341949999999997
Добавление в Ordereddict:  0.9527887080002984
Редактирование dict:  0.6838120419997722
Редактирование Ordereddict:  0.8875835829994685

Вывод Ordereddict работает значительно медленнее dict, его нет смысла использовать в Python 3.6 и более поздних версиях
"""