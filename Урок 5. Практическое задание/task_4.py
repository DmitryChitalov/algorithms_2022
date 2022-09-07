"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import time
from time import perf_counter
from collections import OrderedDict


def function_time(function):
    def wrapped(*args, **kwargs):
        start_time = perf_counter()
        res = function(*args, **kwargs)
        all_time = time.perf_counter() - start_time
        print(f"Время выполнения '{str(function).split(' ')[1]}' составило:", end=' ')
        print(all_time, "секунд")
        return res
    return wrapped


@function_time
def change_simple_dict(some_dict):
    for key in range(10000):
        some_dict.pop(key)
    for key in range(10001, 20002):
        some_dict[key] = 'change'


@function_time
def change_ordered_dict(some_dict):
    for key in range(10000):
        some_dict.pop(key)
    for key in range(10001, 20002):
        some_dict[key] = 'change'


simple_dict = {i: i for i in range(10 ** 5)}
ordered_dict = OrderedDict(simple_dict)

change_simple_dict(simple_dict)
change_ordered_dict(ordered_dict)

# Начиная с версии Python 3.6  использование OrderedDict оправдано, если нужны move_to_end(key, last=True), popitem(last=True))
