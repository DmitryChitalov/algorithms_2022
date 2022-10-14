"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from timeit import timeit
from collections import OrderedDict

my_dict = dict()
my_orderddict = OrderedDict()
n = 10 ** 4


# заполнение словаря dict
def fill_dict(some_dict):
    for i in range(n):
        some_dict[i] = i
    return some_dict


# заполнение словаря OrderedDict
def fill_orderddict(some_dict):
    for i in range(n):
        some_dict[i] = i
    return some_dict


print(timeit("fill_dict(my_dict)", globals=globals(), number=100))  # 0.03961089998483658
print(timeit("fill_orderddict(my_orderddict)", globals=globals(), number=100))  # 0.059832300059497356

"""
Быстрее отрабатывает заполнение обычного словаря.
"""


# удаление элемента словаря dict
def del_el_dict(some_dict):
    for i in range(n):
        del some_dict[i]
    return some_dict


# удаление элемента словаря OrderedDict
def del_el_orderddict(some_dict):
    for i in range(n):
        del some_dict[i]
    return some_dict


print(timeit("del_el_dict(my_dict.copy())", globals=globals(), number=100))  # 0.04172770003788173
print(timeit("del_el_orderddict(my_dict.copy())", globals=globals(), number=100))  # 0.04133079992607236

"""
На удаление элементов из словарей затрачивается почти одно и то же время.
"""


# изменение элементов словаря dict
def change_dict(some_dict):
    for i in range(n):
        some_dict[i] = "NY"
    return some_dict


# изменение элементов словаря OrderedDict
def change_orderddict(some_dict):
    for i in range(n):
        some_dict[i] = "LA"
    return some_dict


print(timeit("change_dict(my_dict.copy())", globals=globals(), number=100))  # 0.03278899996075779
print(timeit("change_orderddict(my_dict.copy())", globals=globals(), number=100))  # 0.033067099982872605

"""
Заполнение обычного словаря происходит быстрее, 
так как словарь dict был разработан для быстрых операций добавления, 
извлечения и обновления данных.
Класс collections.OrderedDict() был разработан для частыx операций переупорядочивания.
Это делает его подходящим для отслеживания недавних обращений например, в кеш LRU. 
Эффективность использования памяти, 
скорость итераций и производительность операций обновления были второстепенными.
Необходимость использовать OrderedDict возникает, когда нам необходимо применить его уникальные методы:
.popitem() и .move_to_end()
"""
