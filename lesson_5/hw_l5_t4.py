"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def add_el(user_dict, num):
    for i in range(num):
        user_dict[i] = i


u_dict = {}
o_dict = {}
o_dict = OrderedDict(o_dict)

print('Заполнение обычного словаря ', timeit("add_el(u_dict, 1000)", globals=globals(), number=10000))
print('Заполнение OrderedDict словаря ', timeit("add_el(o_dict, 1000)", globals=globals(), number=10000))

del_last_u = u_dict.popitem()
del_last_o = o_dict.popitem()
del_fst_u = u_dict.pop(list(u_dict.keys())[0])
del_fst_o = o_dict.popitem(False)

print('Удаление последненого элмента обычного словаря ', timeit("del_last_u", globals=globals(), number=10000))
print('Удаление последненого элмента OrderedDict словаря ', timeit("del_last_o", globals=globals(), number=10000))
print('Удаление первого элмента обычного словаря ', timeit("del_fst_u", globals=globals(), number=10000))
print('Удаление первого элмента OrderedDict словаря ', timeit("del_fst_o", globals=globals(), number=10000))

copy_u_dict = u_dict.copy()
copy_o_dict = o_dict.copy()

print('Копирование обычного словаря ', timeit('copy_u_dict', globals=globals(), number=10000))
print('Копирование OrderedDict словаря ', timeit('copy_o_dict', globals=globals(), number=10000))

#Заподнение словаря необходимо без использования коллекции, использование коллекции позволяет расширить интерфейс и увиличить читаймость и скорость кода