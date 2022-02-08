"""Класс collections.defaultdict()"""
from collections import defaultdict
from timeit import timeit


def check_1():
    dict_of_lst = defaultdict(list)
    dict_of_lst["model"]
    return dict_of_lst


def check_2():
    dict_of_lst = dict()
    dict_of_lst.setdefault("model", list())
    return dict_of_lst


print(check_1())  # -> defaultdict(<class 'list'>, {'model': []})
print(check_2())  # -> {'model': []}


print(
    'defaultdict: ',
    timeit(
        'check_1()',
        globals=globals()))
print(
    'setdefault: ',
    timeit(
        'check_2()',
        globals=globals()))


"""
defaultdict:  0.430548269
setdefault:  0.262938792
"""
