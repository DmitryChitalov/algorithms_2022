"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

def pop_dic(dict):
    for i in range(len(dict)):
        dict.pop(i)




my_dict = {i:f'test_{i}' for i in range(10000)}
my_od = OrderedDict([(i,f'test_{i}') for i in range(10000)])

print(f'Получение элемента словарь: {timeit("my_dict.get(100)",number=100000,globals=globals())}')
print(f'Получение элемента OrderedDict: {timeit("my_od.get(100)",number=100000,globals=globals())}')

print(f'метод pop словарь: {timeit("pop_dic(my_dict)",number=1,globals=globals())}')
print(f'метод pop OrderedDict: {timeit("pop_dic(my_od)",number=1,globals=globals())}')

print(f'метод items() словарь: {timeit("my_dict.items()",number=1000,globals=globals())}')
print(f'метод items() OrderedDict: {timeit("my_od.items()",number=1000,globals=globals())}')

"""
По итогам замеров OrderedDict практически идентичен словарю и так как с версии 3.6 словарь сохраняет порядок, то 
особого смысла использовать OrderedDict нет
"""

