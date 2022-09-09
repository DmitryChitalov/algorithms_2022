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
ord_my_dict = OrderedDict()
name = [i for i in range(100000)]

def fill_dict(el, f_name):
    for elem in f_name:
        el[elem] = str(elem)


print('наполнение словарей: ')
print('fill_dir:', round(timeit("fill_dict(my_dict, name)", globals=globals(), number=10), 3))
print('orderdict:', round(timeit("fill_dict(ord_my_dict, name)", globals=globals(), number=10), 3))


def pop_dict(el):
       for i in range(10):
        el.popitem()


print('\n' 'удаление элементов из словарей: ')
print('pop dict:', round(timeit("pop_dict(my_dict)", globals=globals(), number=100), 5))
print('pop orderdict:', round(timeit("pop_dict(ord_my_dict)", globals=globals(), number=100), 5))


def get_dict(el, my_lst=[]):
    for elem in el.values():
        my_lst.append(elem)


print('\n''получение элемента:')
print('get_dict', round(timeit("get_dict(my_dict)", globals=globals(), number=100), 3))
print('get_orderdict', round(timeit("get_dict(ord_my_dict)", globals=globals(), number=100), 3))
# Поллучение, удаление и заполнение обычного словаря быстрее, чем упорядоченного словаря.
# В Python 3.6+ OrderedDict не имеет смысла использовать, т.к. в версиях 3.6+ словари упорядочены,
# но если в задаче нужно указать: важность порядка элемента, или оперативно переупорядочить элементы,
# или проверить словари на равенство, то применяем OrderedDict.