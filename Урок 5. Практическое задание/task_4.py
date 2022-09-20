"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
import timeit


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__} - {timeit.default_timer() - start}')
        return res
    return wrapper


dict_1 = {}
order_dict_1 = OrderedDict()


@time_decorator
def filling_dict(dict_1):
    for i in range(1, 1000000):
        dict_1[i] = i ** 2


@time_decorator
def filling_odict(orderdict_1):
    for i in range(1, 1000000):
        orderdict_1[i] = i ** 2


filling_dict(dict_1)
filling_odict(order_dict_1)


@time_decorator
def change_dict(dict_1):
    for k, v in dict_1.items():
        dict_1[k] = v ** 2


@time_decorator
def change_order_dict(order_dict_1):
    for k, v in order_dict_1.items():
        order_dict_1[k] = v ** 2


change_dict(dict_1)
change_order_dict(order_dict_1)

"""Операции с обычным словарём быстрее чем с OrderedDict, 
обычный словарь dict был разработан для быстрых операций добавления, извлечения и обновления данных. 
Однако OrderedDict имеет место быть, так как в нём есть методы которые работают по другому в отличие от 
обычного словаря, и есть методы которых в обычном словаре нет """
