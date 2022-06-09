"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(my_dict, num):
    for i in range(num):
        my_dict[i] = i


num = 10 ** 4
dict_1 = dict()
dict_2 = OrderedDict()

print('Заполнение словарей:')
print(timeit("fill_dict(dict_1, num)", globals=globals(), number=1000))
print(timeit("fill_dict(dict_2, num)", globals=globals(), number=1000))
print()


def change_dict(my_dict, num):
    for i in range(num):
        my_dict.pop(i)
    for j in range(num):
        my_dict[j] = 'fill'


print('Изменение словарей:')
print(timeit("change_dict(dict_1, num)", globals=globals(), number=1000))
print(timeit("change_dict(dict_2, num)", globals=globals(), number=1000))

'''
Итог: Первый словарь заполнение и изменение выполняет быстрее.
А смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях есть, 
если нам важен именно порядок последовательности элементов. 
И возможность оперативного переупорядочивания элементов.
'''
