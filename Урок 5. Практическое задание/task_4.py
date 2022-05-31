"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

def dict1():
    my_dict = {}
    my_dict['apple'] = 3

def dict2():
    my_dict = {'apple': 3}
    my_dict.pop('apple')

def dict3():
    my_dict = {'apple': 3}
    my_new_dict = my_dict.copy()

def order_dict1():
    my_dict = OrderedDict()
    my_dict['apple'] = 4

def order_dict2():
    my_dict = OrderedDict({'apple': 4})
    my_dict.pop('apple')

def order_dict3():
    my_dict = OrderedDict({'apple': 4})
    my_new_dict = my_dict.copy()

if __name__ == '__main__':
    print 'Сравниваем три функции (добавление элемента, pop и copy) для dict и OrderDict: '
    print 'dict:'
    print timeit('dict1()', setup='from main import dict1', number=10000)
    print timeit('dict2()', setup='from main import dict2', number=10000)
    print timeit('dict3()', setup='from main import dict3', number=10000)
    """
    Вывод:
    dict:
        0.001327
        0.0021453
        0.0028345
    Самая быстрая функция - получение элемента
    """
    print 'OrderDict:'
    print timeit('order_dict1()', setup='from main import order_dict1', number=10000)
    print timeit('order_dict2()', setup='from main import order_dict2', number=10000)
    print timeit('order_dict3()', setup='from main import order_dict3', number=10000)
    """
    Вывод:
    OrderDict:
        0.0450079
        0.0652484
        0.1093582
    Функции OrderDict намного медленее чем у обычного dict
    """
