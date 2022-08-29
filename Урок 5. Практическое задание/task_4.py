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
ord_dict = OrderedDict()


def append_dict():
    for i in range(10000):
        my_dict[i] = i


def append_ord_dict():
    for i in range(10000):
        ord_dict[i] = i


print(f'Append_dict: {timeit(append_dict, number=1000)}')
print(f'Append_ord_dict: {timeit(append_ord_dict, number=1000)}')


def get_val_dict():
    for k in my_dict:
        my_dict.get(k)


def get_val_ord_dict():
    for k in ord_dict:
        ord_dict.get(k)


print(f'Get val dict: {timeit(get_val_dict, number=1000)}')
print(f'Get val ord dict: {timeit(get_val_ord_dict, number=1000)}')


def popitem_dict():
    simple_dict_copy = my_dict.copy()
    for k in range(1000):
        simple_dict_copy.popitem()


def popitem_ord_dict():
    order_dict_copy = ord_dict.copy()
    for k in range(1000):
        order_dict_copy.popitem()


print(f'Pop dict: {timeit(popitem_dict, number=1000)}')
print(f'Pop ord dict: {timeit(popitem_ord_dict, number=1000)}')

"""
Append_dict: 0.6180092999711633
Append_ord_dict: 0.9693370000459254
Get val dict: 0.5339409000007436
Get val ord dict: 0.745209899963811
Pop dict: 0.10674199997447431
Pop ord dict: 0.893286700011231

Смысла использовать OrderedDict практически нет, так как он проигрывает по скорости исполнения обычному словарю.
Мы можем использовать OrderedDict, если нам важен порядок, однако с python 3.6 обычный словарь выводит элементы не в разнобой.
Для OrderedDict есть полезные методы, такие как popitem, move_to_end. Popitem может удалять первый и последний элемент,
если указать аргумент last=True или False. Так же и с move_to_end. Только он перемещает ключ и значение в начало или в конец.

"""