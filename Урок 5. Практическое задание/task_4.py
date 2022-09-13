"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


some_dict = {i: i ** 2 for i in range(10000)}
some_ordered = OrderedDict({i: i ** 2 for i in range(10000)})


def change_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict[i] = i
    return some_dict_orderdict


def pop_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict.pop(i)
    return some_dict_orderdict


print('Изменение dict: ', timeit('pop_dict(some_dict.copy())', globals=globals(), number=100))
print('Изменение Ordereddict: ', timeit('pop_dict(some_ordered.copy())', globals=globals(), number=100))

print('Удаление dict: ', timeit('pop_dict(some_dict.copy())', globals=globals(), number=100))
print('Удаление Ordereddict: ', timeit('pop_dict(some_ordered.copy())', globals=globals(), number=100))


'''
Изменение dict:  0.053043333000459825
Изменение Ordereddict:  0.10107379199962452
Удаление dict:  0.041406166999877314
Удаление Ordereddict:  0.09898566700030642

Выполнение операция с dict происходит быстрее чем с Ordereddict. В версии Python 3.7 и выше обычные словари также 
стали поддерживать запоминание порядка добавления элементов, поэтому использование Ordereddict имеет смысл
только в специфичных ситуациях, связанных с методfvb, специализированных для изменения порядка элемента словаря .
'''