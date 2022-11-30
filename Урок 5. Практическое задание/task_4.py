"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

my_order_dict = OrderedDict()
my_dict = {}


# Заполнение
def fill_dict(reg_dict, n):
    for i in range(n):
        reg_dict[i] = i * i
    return reg_dict


def fill_ord_dict(order_dict, n):
    for i in range(n):
        order_dict[i] = i * i
    return order_dict


#  перемещение в конец
def to_end_ord_dict(order_dict, key):
    order_dict.move_to_end(key, last=True)
    return order_dict


def to_end_dict(reg_dict, key):
    to_move = {key: reg_dict[key]}
    reg_dict.pop(key)
    reg_dict.update(to_move)
    return reg_dict


# перемещение в начало
def to_start_ord_dict(order_dict, key):
    order_dict.move_to_end(key, last=False)
    return order_dict


def to_start_dict(reg_dict, key):
    cp = reg_dict.copy()
    new_d = {key: cp[key]}
    cp.pop(key)
    new_d.update(cp)
    reg_dict = new_d
    return reg_dict


# удаление и получение последнего элемента
def get_last_ord_dict(order_dict):
    el = order_dict.popitem(last=True)
    return el


def get_last_dict(reg_dict):
    reg_el = reg_dict.popitem()
    return reg_el


# удаление и получение первого элемента
def del_fst_ord_dict(order_dict):
    el = order_dict.popitem(last=False)
    return el


def del_fst_dict(reg_dict):
    lst = list(reg_dict)
    el = (lst[0], reg_dict[lst[0]])
    reg_dict.pop(lst[0])
    return el


print(f'Заполнение orderdict занимает время: '
      f'{timeit("fill_ord_dict(my_order_dict, 1000)", globals=globals(), number=1000)}')
print(f'Заполнение dict занимает время: '
      f'{timeit("fill_dict(my_dict, 1000)", globals=globals(), number=1000)}')
print('-' * 10)
print(f'Перемещение пары ключ-значение в конец orderdict занимает время: '
      f'{timeit("to_end_ord_dict(my_order_dict, 1)", globals=globals(), number=1000)}')
print(f'Перемещение пары ключ-значение в конец dict занимает время: '
      f'{timeit("to_end_dict(my_dict, 1)", globals=globals(), number=1000)}')
print('-' * 10)
print(f'Перемещение пары ключ-значение в начало orderdict занимает время: '
      f'{timeit("to_start_ord_dict(my_order_dict, 3)", globals=globals(), number=1000)}')
print(f'Перемещение пары ключ-значение в начало dict занимает время: '
      f'{timeit("to_start_dict(my_dict, 3)", globals=globals(), number=1000)}')
print('-' * 10)
print(f'Получение и удаление последнего элемента orderdict занимает время: '
      f'{timeit("get_last_ord_dict(my_order_dict)", globals=globals(), number=1000)}')
print(f'Получение и удаление последнего элемента dict занимает время: '
      f'{timeit("get_last_dict(my_dict)", globals=globals(), number=1000)}')
print('-' * 10)

fill_dict(my_dict, 1000)
fill_ord_dict(my_order_dict, 1000)

print(f'Получение и удаление первого элемента orderdict занимает время: '
      f'{timeit("del_fst_ord_dict(my_order_dict)", globals=globals(), number=1000)}')
print(f'Получение и удаление первого элемента dict занимает время: '
      f'{timeit("del_fst_dict(my_dict)", globals=globals(), number=1000)}')






"""
Вывод:
Использование OrderedDict оправдано только в том случае если есть необходимость менять в словаре порядок 
элементов(пар ключ-значение), получать / удалять элементы не с конца словаря. 
"""
