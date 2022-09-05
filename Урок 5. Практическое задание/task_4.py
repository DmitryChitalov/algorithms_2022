"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
import random
from collections import OrderedDict
from timeit import timeit

usual_dict = {}
ordered_dict = OrderedDict()
test_num = random.randint(-100, 100)


def add_to_dct(dct, test_num):
    for i in range(1000):
        dct[i] = test_num


def change_dct(dct, test_num):
    for i in range(1000):
        dct[i] = test_num


def pop_dct(dct):
    for i in range(200, 800):
        dct.pop(i)


print('add_to_dct - usual')
print(timeit("add_to_dct(usual_dict, test_num)", globals=globals(), number=10000))

print('add_to_dct - ordered')
print(timeit("add_to_dct(ordered_dict, test_num)", globals=globals(), number=10000))

print('---------------------------------')
test_num = random.randint(-100, 100)

print('change_dct - usual')
print(timeit("change_dct(usual_dict, test_num)", globals=globals(), number=10000))

print('change_dct - ordered')
print(timeit("change_dct(ordered_dict, test_num)", globals=globals(), number=10000))

print('----------------------------------')

print('pop_dct - usual')
print(timeit("pop_dct(usual_dict)", globals=globals(), number=1))

print('pop_dct - ordered')
print(timeit("pop_dct(ordered_dict)", globals=globals(), number=1))

# Упорядоченный словарь проигрывает обычному при всех стандартных операциях, очевидно, он имеет смысл только при
# необходимости специфических операций применимых только к нему.
