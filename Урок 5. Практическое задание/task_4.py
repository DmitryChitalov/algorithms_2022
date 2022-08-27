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
my_ordereddict = OrderedDict()

def create_dict(my_dict):
    for i in range(10000):
        my_dict[i] = i
    return my_dict
create_dict(my_dict)

def create_ord_dict(my_ordereddict):
    for i in range(10000):
        my_ordereddict[i] = i
    return my_ordereddict
create_ord_dict(my_ordereddict)

print(timeit('create_dict(my_dict)', globals=globals(), number = 100))  # 0.2542186
print(timeit('create_ord_dict(my_ordereddict)', globals=globals(), number=100))  # 0.37593449999999995

# Операция создания словаря быстрее чем OrderedDict

def pop_elem(my_dict):
    for i in range(len(my_dict)):
        my_dict.pop(i)
    return my_dict

def pop_elem_ord(my_ordereddict):
    for i in range(len(my_ordereddict)):
        my_ordereddict.pop(i)
    return my_ordereddict

print(timeit('pop_elem(my_dict)', globals=globals(), number=100))
print(timeit('pop_elem_ord(my_ordereddict)', globals=globals(), number=100))

""" Удаление элемента с словаре быстрее чем в OrderedDict

Думаю использовать OrderedDict не нужно,так как в python вурсии 3.6 и выше 
обычный словарь тоже может запоминать порядок добавления пар,
если только ружны специфические операции как popitem и move_to_end
"""










