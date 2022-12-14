"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


def create_dict():
    return {i: i * 2 for i in range(1000)}


def create_order_dict():
    return OrderedDict({i: i * 2 for i in range(1000)})


print(timeit('create_dict()', globals=globals(), number=1000))
print(timeit('create_order_dict()', globals=globals(), number=1000))

my_dict = {i: i * 2 for i in range(1000)}
my_order_dict = OrderedDict({i: i * 2 for i in range(1000)})


def chenge_dict(my_dict):
    for i in my_dict.keys():
        my_dict[i] = i * 3
    return my_dict


def chenge_order_dict(my_order_dict):
    for i in my_order_dict.keys():
        my_dict[i] = i * 3
    return my_order_dict


print(timeit('chenge_dict(my_dict)', globals=globals(), number=1000))
print(timeit('chenge_order_dict(my_order_dict)', globals=globals(), number=1000))


"""как показали замеры скорости выполнения простых операций со словарями - обычный словарь лучше по скорости работы, а 
на Python версии выше 3.6 в использовании OrderDict вообще нет никакой необходимости так как обычный словарь тоже
запоминает порядок добавления новых ключей. Единственное применение для OrderDict на современных версиях пайтон, как по
мне это использование его методов: opitem(last=True) - 
удаляет последний элемент если last=True, и первый, если last=False.
move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.  
"""
