"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import timeit
from collections import OrderedDict


order_dict = OrderedDict()
for i in range(1000):
    order_dict[i] = str(i)

smpl_dict = {}
for i in range(1000):
    smpl_dict[i] = str(i)


def order_change(order_dict):
    for i in range(len(order_dict)):
        order_dict[i] = 'pass'
    return order_dict


def dict_change(smpl_dict):
    for i in range(len(smpl_dict)):
        smpl_dict[i] = 'pass'
    return smpl_dict


print(timeit.timeit('order_change(order_dict)', globals=globals(), number=1000))
print(timeit.timeit('dict_change(smpl_dict)', globals=globals(), number=1000))
# 0.3303174003958702
# 0.31883540004491806

'''Ордер дикт медленнее, я не вижу применять его, если нет строгой необходимости в 
последовательности элементов, и необходимости перемещать элементы в словаре'''