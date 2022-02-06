"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


def dict_fill():
    my_dict = {1: 1, 2: 2, 3: 3}


def ordered_dict_fill():
    my_ordered_dict = OrderedDict([(1, 1), (2, 2), (3, 3)])


def dict_pop():
    my_dict = {'a': 1}
    my_dict.popitem()


def ordered_dict_pop():
    my_ordered_dict = OrderedDict({'a': 1})
    my_ordered_dict.popitem()


def dict_sort():
    my_dict = {'a': 1, 'c': 3, 'b': 2}
    my_list = sorted(my_dict)


def ordered_dict_sort():
    my_dict = OrderedDict({'a': 1, 'c': 3, 'b': 2})
    my_list = sorted(my_dict)


print("dict test")
print(timeit("dict_fill()", setup="from __main__ import dict_fill", number=100000))
print(timeit("dict_pop()", setup="from __main__ import dict_pop", number=100000))
print(timeit("dict_sort()", setup="from __main__ import dict_sort", number=100000))
print("ordered dict test")
print(timeit("ordered_dict_fill()", setup="from __main__ import ordered_dict_fill", number=100000))
print(timeit("ordered_dict_pop()", setup="from __main__ import ordered_dict_pop", number=100000))
print(timeit("ordered_dict_sort()", setup="from __main__ import ordered_dict_sort", number=100000))

"""
В python начиная с версии 3.6 появилась а с 3.7 официально объявлена в документации реализация dict,
которая сохраняет порядок элементов словаря.
Словари класса OrderedDict никакого выйгрыша в производительности не дают
Использовать OrderedDict можно:
 - при сравнении словарей, если важен порядок элементов 
 - для обозначения смысла кода
 - в OrderedDict проще переупорядочить элементы move_to_end(Last=True) и popitem(Last=True)
"""
