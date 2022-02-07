"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from itertools import islice
from timeit import default_timer
from collections import OrderedDict
ord_dict = OrderedDict()
just_dict = {}


def time_it(n):
    def deco(func):
        def wrapper(*args, **kwargs):
            t_sum = 0
            for el in range(n):
                start_time = default_timer()
                func(*args, **kwargs)
                delta = default_timer() - start_time
                t_sum += delta
            return f'{func.__name__}: {t_sum}'
        return wrapper
    return deco


@time_it(1000)
def ord_dict_filling(number):
    for i in range(number):
        ord_dict[i] = i
    return ord_dict


@time_it(1000)
def dict_filling(number):
    for i in range(number):
        just_dict[i] = i
    return just_dict


@time_it(1000)
def ord_dict_changing(number):
    for i in range(number):
        ord_dict[i] = '1'
    return ord_dict


@time_it(1000)
def dict_changing(number):
    for i in range(number):
        just_dict[i] = '1'
    return just_dict


@time_it(1)
def ord_dict_pop(number):
    for i in range(number):
        ord_dict.pop(i)
    return ord_dict


@time_it(1)
def dict_pop(number):
    for i in range(number):
        just_dict.pop(i)
    return just_dict


print(ord_dict_filling(10000))
print(dict_filling(10000), '\n')
print(ord_dict_changing(10000))
print(dict_changing(10000), '\n')
print(ord_dict_pop(10000))
print(dict_pop(10000), '\n')

print('Вывод: обычный словарь работает быстрее во всех приведенных операциях, чем OrderedDict. \n'
      'В нынешних версиях Python словарь сам выстраивается по порядку, \n'
      'но все же я считаю что OrderedDict нужен, по таким причинам, как: \n'
      '1. Позволяет указать что у этого словаря важен порядок\n'
      '2. Позволяет перемещать элементы с конца в начало и наоборот удобным методом move_to_end\n'
      '3. Позволяет удалять элементы с конца и с начала удобным методом popitem\n'
      '4. При сравнении двух одинаковых обычных словарей с разным порядком, будет True, \n'
      'а при сравнении таких же одинаковых OrderedDict с разным порядком, будет False')
