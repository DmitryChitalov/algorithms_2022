"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit


the_dict = {}
the_ord_dict = OrderedDict()


def fill_dict(a_dict):
    for i in range(100000):
        a_dict[i] = i


def fill_ord_dict(an_ord_dict):
    for i in range(100000):
        an_ord_dict[i] = i


def update_dict(a_dict):
    for i in range(100000):
        a_dict.update({i: i})


def update_ord_dict(an_ord_dict):
    for i in range(100000):
        an_ord_dict.update({i: i})


def get_dict_el(a_dict):
    for i in range(100000):
        return a_dict[i]


def get_ord_dict_el(an_ord_dict):
    for i in range(100000):
        return an_ord_dict[i]


print(f'Время выполнения функции {fill_dict.__name__}: ',
      timeit('fill_dict(the_dict)', 'from __main__ import fill_dict, the_dict', number=1000))
print(f'Время выполнения функции {fill_ord_dict.__name__}: ',
      timeit('fill_ord_dict(the_ord_dict)', 'from __main__ import fill_ord_dict, the_ord_dict', number=1000))
print(f'Время выполнения функции {update_dict.__name__}: ',
      timeit('update_dict(the_dict)', 'from __main__ import update_dict, the_dict', number=1000))
print(f'Время выполнения функции {update_ord_dict.__name__}: ',
      timeit('update_ord_dict(the_ord_dict)', 'from __main__ import update_ord_dict, the_ord_dict', number=1000))
print(f'Время выполнения функции {get_dict_el.__name__}: ',
      timeit('get_dict_el(the_dict)', 'from __main__ import get_dict_el, the_dict', number=1000))
print(f'Время выполнения функции {get_ord_dict_el.__name__}: ',
      timeit('get_ord_dict_el(the_ord_dict)', 'from __main__ import get_ord_dict_el, the_ord_dict', number=1000))


# Время выполнения функции fill_dict:  8.250002699999868
# Время выполнения функции fill_ord_dict:  12.840192699999989
# Время выполнения функции update_dict:  22.71242469999993
# Время выполнения функции update_ord_dict:  44.31177109999999
# Время выполнения функции get_dict_el:  0.0003549000000475644
# Время выполнения функции get_ord_dict_el:  0.00034989999994650134
#
# Заполнение и обновление упорядоченного словаря заимает больше времени,
# чем выполнение соответствующих операций с обычным словарем, получение
# элемента по ключу осуществляется одинаково быстро.
# В целом работа с упорядоченным словарем требует больше времени, и его
# использование оправдано лишь в том случае, когда порядок элементов
# имеет принципиальное значение, и есть необходимость в использовании
# специальных методов упорядоченного словаря.
