"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from timeit import default_timer
from collections import OrderedDict

some_dict = {}
some_ordered_dict = OrderedDict()
n = 10 ** 7


def time_decorator(some_func):
    """Вычисляет время выполения декорируемой функции"""

    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} '
              f'составило {default_timer() - start}. ')
        return result
    return wrapper


@time_decorator
def fill_dict(dct, num):
    """Заполняет обычный словарь"""
    for i in range(num):
        dct[i] = i


@time_decorator
def fill_ordered_dict(dct, num):
    """Заполняет OrderedDict"""
    for i in range(num):
        dct[i] = i


@time_decorator
def change_dict(dct):
    """Выполняет операции по изменению обычного словаря"""
    for i in range(1000000):
        dct.pop(i)
    for j in range(1000001, 2000002):
        dct[j] = 'fill'
    for k, v in dct.items():
        dct[k] = 'some value'


@time_decorator
def change_ordered_dict(dct):
    """Выполняет операции по изменению OrderedDict"""
    for i in range(1000000):
        dct.pop(i)
    for j in range(1000001, 2000002):
        dct[j] = 'fill'
    for k, v in dct.items():
        dct[k] = 'some value'


fill_dict(some_dict, n)
fill_ordered_dict(some_ordered_dict, n)

"""
Обычный словарь заполняется элементами быстрее, чем OrderedDict. 
Это связано прежде всего с тем, что:
1. OrderedDict реализован на Python, а обычный словарь на С 
и априори должен работать быстрее.
2. OrderedDict был разработан для быстрого переупорядочивания элементов, 
а производительность в части заполнения вторична.
"""

change_dict(some_dict)
change_ordered_dict(some_ordered_dict)

"""
При выполнении операций изменения, итерации и присваивания обычный словарь 
работает гораздо быстрее, чем OrderedDict.
Начиная с версии Python 3.6 обычный словарь также поддерживает запоминание 
порядка добавления пар ключ-значение. Таким
образом в настоящее время использование OrderedDict оправдано, 
если нужны только специфичные для него функции,
такие как move_to_end(key, last=True), popitem(last=True).
"""

NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
NEW_DICT.move_to_end('b', last=True)  # переносит ключ переносит элемент
# с указанным в конец, если last=True, и в начало, если last=False
print(NEW_DICT)
NEW_DICT.popitem(last=True)  # удаляет последний элемент если last=True,
# и первый, если last=False
print(NEW_DICT)



