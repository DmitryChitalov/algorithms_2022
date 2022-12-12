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
nums = 200000


def dict_append():
    for i in range(nums):
        my_dict[i] = i
    return my_dict


dict_append()


def ordereddict_append():
    for i in range(nums):
        my_ordereddict[i] = i
    return my_ordereddict


ordereddict_append()


def dict_pop():
    for i in range(200000):
        my_dict.pop(i)
    return my_dict


dict_pop()


def ordereddict_pop():
    for i in range(200000):
        my_ordereddict.pop(i)
    return my_ordereddict


ordereddict_pop()
print(dict_append.__name__, timeit('dict_append()', globals=globals(), number=10))
print(ordereddict_append.__name__, timeit('ordereddict_append()', globals=globals(), number=10))
print(dict_pop.__name__, timeit('dict_pop()', globals=globals(), number=1))
print(ordereddict_pop.__name__, timeit('ordereddict_pop()', globals=globals(), number=1))

'''
В новых версиях Python OrderedDict стал неактуальным, потому что словари в Python стали упорядочеными,
так же OrderedDict занимает большее время на выполнение операций. 
У OrderedDict есть два метода которые могут быть полезными:
1) popitem() возвращает и удаляет пару ключ-значение. Ключ-значение возвращаются в порядке LIFO, если аргумент last=True
или в порядке FIFO, если last=False.
2) move_to_end() перемещает существующий ключ в начало или конец упорядоченного словаря в зависимости
 от аргумента last=True или last=False.
'''
