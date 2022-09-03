"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
# from time import perf_counter_ns
import time
from time import perf_counter
from collections import OrderedDict


def time_of_function(function):
    def wrapped(*args, **kwargs):
        start_time = perf_counter()  # gives the integer value of time in seconds.
        res = function(*args, **kwargs)
        all_time = time.perf_counter() - start_time
        print(f"Время выполнения функции '{str(function).split(' ')[1]}' составило:", end=' ')
        print(all_time, "секунд")
        return res
    return wrapped


@time_of_function
def change_simple_dict(some_dict):
    for key in range(10000):
        some_dict.pop(key)  # удаление 10000 ключей
    for key in range(10001, 20002):
        some_dict[key] = 'change'  # модификация 10000 значений


@time_of_function
def change_ordered_dict(some_dict):
    for key in range(10000):
        some_dict.pop(key)  # удаление 10000 ключей
    for key in range(10001, 20002):
        some_dict[key] = 'change'  # модификация 10000 значений


# Создание простого словаря
simple_dict = {i: i for i in range(10 ** 5)}

# Создание упорядоченного словаря
ordered_dict = OrderedDict(simple_dict)

change_simple_dict(simple_dict)
change_ordered_dict(ordered_dict)
"""
Время выполнения функции 'change_simple_dict' составило: 0.0017635879999999965 секунд
Время выполнения функции 'change_ordered_dict' составило: 0.0034418660000000018 секунд


Начиная с версии Python 3.6 обычный словарь также поддерживает запоминание 
порядка добавления пар ключ-значение. В настоящее время использование
OrderedDict оправдано, если нужны только специфичные для него функции, 
такие как move_to_end(key, last=True), popitem(last=True)
"""
