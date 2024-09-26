"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import collections
from collections import OrderedDict
from timeit import timeit

simple_dict = {i:i**2 for i in range(100)}
ord_dict = OrderedDict(simple_dict)


def add_item(x):
    for i in range(100000):
        x[100+i] = i
    return x


def popitem_last(x):
    for i in range(10):
        x.popitem()
    return x


def popitem_first(x):
    for i in range(10):
        x.popitem(last=False)
    return x


def popitem_first_simple(x):
    for i in range(10):
        x.pop(list(x)[0])
    return x


def simple_move_to_end(x):
    for i in range(10):
        el = x.pop(list(x)[0])
        x[list(x)[0]] = el
    return x


def ord_move_to_end(x):
    for i in range(10):
        x.move_to_end(list(x)[0])
    return x


print('добавление элемента simple_d: ', timeit("add_item(simple_dict)", number=1, globals=globals()))
print('добавление элемента ordered_d: ', timeit("add_item(ord_dict)", number=1, globals=globals()))
print('удаление последнего элемента simple_d: ', timeit("popitem_last(simple_dict)", number=1000, globals=globals()))
print('удаление последнего элемента ordered_d: ', timeit("popitem_last(ord_dict)", number=1000, globals=globals()))
print('удаление первого элемента simple_d: ', timeit("popitem_first_simple(simple_dict)", number=100, globals=globals()))
print('удаление первого элемента ordered_d: ', timeit("popitem_first(ord_dict)", number=100, globals=globals()))
print('перемещение в конец simple_d: ', timeit("simple_move_to_end(simple_dict)", number=100, globals=globals()))
print('перемещение в конец ordered_d: ', timeit("ord_move_to_end(ord_dict)", number=100, globals=globals()))

# По результатам замеров OrderedDict дает заметное преимущество по скорости в операции удаления из словаря первого элемента.
# Поэтому может быть полезен в работе. Остальные функции примерно равны по времени.
