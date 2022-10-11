"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


def fill_dict(num):
    return dict.fromkeys(range(num))


def fill_ordered_dict(num):
    return OrderedDict.fromkeys(range(num))


n = 1000
my_dict = fill_dict(n)
my_ordered_dict = fill_ordered_dict(n)

print(f'Время выполнения функции fill_dict = {timeit("fill_dict(n)", globals=globals(), number=1000)}')
print(f'Время выполнения функции fill_ordered_dict = {timeit("fill_ordered_dict(n)", globals=globals(), number=1000)}')


# Время выполнения функции fill_dict = 0.0515350999776274
# Время выполнения функции fill_ordered_dict = 0.09996700007468462


def copy_dict():
    test_dict = my_dict.copy()


def copy_ordered_dict():
    test_dict = my_ordered_dict.copy()


print(f'Время выполнения функции copy_dict = {timeit("copy_dict()", globals=globals(), number=1000)}')
print(f'Время выполнения функции copy_ordered_dict = {timeit("copy_ordered_dict()", globals=globals(), number=1000)}')


# Время выполнения функции copy_dict = 0.006106900051236153
# Время выполнения функции copy_ordered_dict = 0.08645859989337623


def pop_dict():
    test_dict = my_dict.copy()
    for i in range(len(test_dict)):
        test_dict.pop(i)


def pop_ordered_dict():
    test_dict = my_ordered_dict.copy()
    for i in range(len(test_dict)):
        test_dict.pop(i)


print(f'Время выполнения функции pop_dict = {timeit("pop_dict()", globals=globals(), number=1000)}')
print(f'Время выполнения функции pop_ordered_dict = {timeit("pop_ordered_dict()", globals=globals(), number=1000)}')


# Время выполнения функции pop_dict = 0.10286689992062747
# Время выполнения функции pop_ordered_dict = 0.27157720015384257

def del_dict():
    test_dict = my_dict.copy()
    for i in range(len(test_dict)):
        del test_dict[i]


def del_ordered_dict():
    test_dict = my_ordered_dict.copy()
    for i in range(len(test_dict)):
        del test_dict[i]


print(f'Время выполнения функции del_dict = {timeit("del_dict()", globals=globals(), number=1000)}')
print(f'Время выполнения функции del_ordered_dict = {timeit("del_ordered_dict()", globals=globals(), number=1000)}')

# Время выполнения функции del_dict = 0.0716858000960201
# Время выполнения функции del_ordered_dict = 0.18702919990755618


# В целом у OrderedDict более низкая производительность, чем у обычных словарей. Но при определенных задачах
#  есть смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях:
# напр. move_to_end и popitem работают быстрее или если требуется сравнить порядок элементов в разных объектах.

# Возможность оперативного переупорядочивания элементов: у ordereddict существует специальный метод  .popitem(),
# который позволяет удалять и возвращать элемент либо из конца, либо из начала базового упорядоченного словаря.
