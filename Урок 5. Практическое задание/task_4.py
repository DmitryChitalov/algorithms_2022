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
my_odict = OrderedDict()
test_num = 10 ** 5

# add ###########################################
print('#' * 15, "add", '#' * 15, '\n')


def dict_add(dct: dict):
    """Добавление элементов в словарь"""
    for i in range(test_num):
        dct[i] = i


def odict_append(odct: OrderedDict):
    """Добавление элементов в упорядоченный словарь"""
    for i in range(test_num):
        odct[i] = i


print('dict_add()')
print(timeit('dict_add(my_dict)', globals=globals(), number=1000))
print()
print('odict_append()')
print(timeit('odict_append(my_odict)', globals=globals(), number=1000))
print()

# get() ###########################################
print('#' * 15, "get element", '#' * 15, '\n')


def dict_get(dct: dict):
    """Получение элемента по ключу"""
    for i in range(test_num):
        dct[i]


def odict_get(odct: OrderedDict):
    """Получение элемента по ключу"""
    for i in range(test_num):
        odct[i]


print('dict_get()')
print(timeit('dict_get(my_dict)', globals=globals(), number=1000))
print()
print('odict_get()')
print(timeit('odict_get(my_odict)', globals=globals(), number=1000))
print()


# get() ###########################################
print('#' * 15, "pop()", '#' * 15, '\n')


def dict_pop(dct: dict):
    """Извлечение элемента по ключу"""
    for i in range(10000):
        dct.pop(i)


def odict_pop(odct: OrderedDict):
    """Извлечение элемента по ключу"""
    for i in range(10000):
        odct.pop(i)


print('dict_pop()')
print(timeit('dict_pop(my_dict)', globals=globals(), number=1))
print()
print('odict_pop()')
print(timeit('odict_pop(my_odict)', globals=globals(), number=1))
print()


"""
Вывод. Операции над стандартным словарем производятся быстрее, чем над упорядоченным.
Упорядоченный словарь имеет смысл применять в тех случаях, 
когда явно требуется порядок хранимых значений. 
"""