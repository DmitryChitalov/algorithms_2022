"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
############################################################################
from collections import OrderedDict
from timeit import timeit


# Операция заполнения словаря

def fill_dict(us_dict, us_num):
    for i in range(us_num):
        us_dict[i] = i


num = 10 ** 4
simple_dict = dict()
ordered_dict = OrderedDict()

print('Операции заполнения словарей:')
print(timeit("fill_dict(simple_dict, num)", globals=globals(), number=1000))
print(timeit("fill_dict(ordered_dict, num)", globals=globals(), number=1000))
print()


# Операция изменения словаря

def change_dict(us_dict, us_num):
    for i in range(us_num):
        us_dict.pop(i)
    for j in range(us_num):
        us_dict[j] = 'fill'


print('Операции изменения словарей:')
print(timeit("change_dict(simple_dict, num)", globals=globals(), number=1000))
print(timeit("change_dict(ordered_dict, num)", globals=globals(), number=1000))

'''
Аналитика:
    Исходя из полученных результатов, мы можем сказать, что обычный словарь 
операции заполнения и изменения выполняет быстрее.
    Смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях есть, если
нам важен именно порядок следования элементов. А также возможность 
оперативного переупорядочивания элементов.
'''
