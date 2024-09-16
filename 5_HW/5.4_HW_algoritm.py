"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit


my_order = OrderedDict((i, i*2) for i in range(1000))
my_dict = {i: i*2 for i in range(1000)}
count = 1000


# ______________________________________________________Заполнение____________________________________________________
# заполнение словаря быстрее
# add_el_dict ---- 0.008675700000000001
def add_el_dict(some_dict):
    for i in range(count):
        some_dict['i'] = i * 2
        return some_dict


add_el_dict(my_dict.copy())


# заполнения ордердикт дольше
# add_el_order ---- 0.097232
def add_el_order(some_order):
    for i in range(count):
        some_order['i'] = i * 2
        return some_order


add_el_order(my_order.copy())

# ______________________________________________________Изменение____________________________________________________
# изменение словаря быстрее
# change_el_dict ---- 0.008292500000000008
def change_el_dict(some_dict):
    for i in range(count):
        some_dict[i] = i * 3
        return some_dict


change_el_dict(my_dict.copy())


# заполнения ордердикт дольше
# change_el_order ---- 0.10410999999999998
def change_el_order(some_order):
    for i in range(count):
        some_order[i] = i * 3
        return some_order


change_el_order(my_order.copy())

# ______________________________________________________взятие по ключу____________________________________________________
# взятие по ключу словаря быстрее
# get_el_dict ---- 0.07565120000000003
def get_el_dict(some_dict):
    for i in range(count):
        a = some_dict[i]


get_el_dict(my_dict.copy())


# взятие по ключу ордердикт дольше
# get_el_order ---- 0.15230130000000003
def get_el_order(some_order):
    for i in range(count):
        a = some_order[i]


get_el_order(my_order.copy())


# ______________________________________________________удаление пары____________________________________________________
# удаление пары словаря быстрее
# get_el_dict ---- 0.07565120000000003
def pop_el_dict(some_dict):
    for _ in range(count):
        some_dict.popitem()


pop_el_dict(my_dict.copy())


# удаление пары ордердикт дольше
# get_el_order ---- 0.15230130000000003
def pop_el_order(some_order):
    for _ in range(count):
        some_order.popitem()


pop_el_order(my_order.copy())
print(f'add_el_dict ---- {timeit("add_el_dict(my_dict.copy())", globals=globals(), number=1000)}')
print(f'add_el_order ---- {timeit("add_el_order(my_order.copy())", globals=globals(), number=1000)}')

print(f'change_el_dict ---- {timeit("change_el_dict(my_dict.copy())", globals=globals(), number=1000)}')
print(f'change_el_order ---- {timeit("change_el_order(my_order.copy())", globals=globals(), number=1000)}')

print(f'get_el_dict ---- {timeit("get_el_dict(my_dict.copy())", globals=globals(), number=1000)}')
print(f'get_el_order ---- {timeit("get_el_order(my_order.copy())", globals=globals(), number=1000)}')

print(f'pop_el_dict ---- {timeit("pop_el_dict(my_dict.copy())", globals=globals(), number=1000)}')
print(f'pop_el_order ---- {timeit("pop_el_order(my_order.copy())", globals=globals(), number=1000)}')

"""во всех примерах словарь быстрее. Использование orderdict огично при необходимости в методах: move_to_end, popitem
   и если нужно проверить исходный ордердикт с другим на соответствия порядка """