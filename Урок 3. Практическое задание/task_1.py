"""
Задание 1.

Реализуйте:

a) заполнение списка, оцените сложность в O-нотации.
   заполнение словаря, оцените сложность в O-нотации.
   сделайте аналитику, что заполняется быстрее и почему.
   сделайте замеры времени.

b) выполните со списком и словарем операции: изменения и удаления элемента.
   оцените сложности в O-нотации для операций
   получения и удаления по списку и словарю
   сделайте аналитику, какие операции быстрее и почему
   сделайте замеры времени.


ВНИМАНИЕ: в задании два пункта - а) и b)
НУЖНО выполнить оба пункта

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

from functools import wraps
from time import time


def timeit(f):
    def timed(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()

        print('func:%r took: %2.4f sec' % \
              (f.__name__, te - ts))
        return result

    return timed


lst = [z for z in range(100000)]
dct = {z for z in range(100000)}


@timeit
def double_lst(lst):
    return [num * 2 for num in lst]


double_lst(lst)


@timeit
def double_dict(lst):
    return {num: num * 2 for num in lst}


double_dict(lst)


@timeit
def get_el_lst(lst):
    return [num for num in lst if num != 999]


get_el_lst(lst)


@timeit
def get_el_dct(lst):
    return {num for num in lst if num != 999}


get_el_dct(lst)


@timeit
def change_el_lst(lst):

    return


change_el_lst(lst)


@timeit
def change_el_dct(lst):
    return


change_el_dct(lst)
