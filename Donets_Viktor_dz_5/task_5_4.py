"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def func_1():
    d_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    while d_dict != {}:
        d_dict.popitem()


def func_2():
    d_order_dict = OrderedDict({'banana': 3, 'apple': 4, 'pear': 1,
                                'orange': 2})
    while d_order_dict != {}:
        d_order_dict.popitem(last=True)


print(f'{timeit("func_1()", globals=globals(), number=1000)} - удаление из '
      f'словаря')
print(f'{timeit("func_2()", globals=globals(), number=1000)} - удаление из '
      f'OrderedDict')

"""
0.0005679000000782253 - удаление из словаря
0.0017905999998220068 - удаление из OrderedDict
"""

"""
Из выше полученных данных видно что удаление заначений из словаря происходит 
быстрее чем из коллекции OrderedDict. Смысл использоватьть OrderedDict для 
удаления значений в Python выше версии 3.6 нет
"""