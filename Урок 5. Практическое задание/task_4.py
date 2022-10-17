"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from timeit import default_timer
from collections import OrderedDict

dict_x = {}
ordered_dict_x = OrderedDict()
n = 10 ** 7


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} '
              f'составляет {default_timer() - start}. ')
        return result
    return wrapper


@time_decorator
def fill_dict(dict_x, n):
    for i in range(n):
        dict_x[i] = i


fill_dict(dict_x, n)


@time_decorator
def fill_ordered_dict(ordered_dict_x, n):
    for i in range(n):
        ordered_dict_x[i] = i


fill_ordered_dict(ordered_dict_x, n)

"""
Обычный словарь заполняется элементами быстрее, чем OrderedDict. 
Это связано прежде всего с тем, что:
1. OrderedDict реализован на Python, а обычный словарь на С 
и априори должен работать быстрее.
2. OrderedDict был разработан для быстрого переупорядочивания элементов, 
а производительность в части заполнения вторична.
Время выполенения функции fill_dict составляет 0.9594245. 
Время выполенения функции fill_ordered_dict составляет 1.4219535840000002. 
"""


@time_decorator
def change_dict(dict_x):
    for i in range(1000000):
        dict_x.pop(i)
    for j in range(1000001, 2000002):
        dict_x[j] = 'x'
    for k, v in dict_x.items():
        dict_x[k] = 'value'


change_dict(dict_x)


@time_decorator
def change_ordered_dict(ordered_dict_x):
    for i in range(1000000):
        ordered_dict_x.pop(i)
    for j in range(1000001, 2000002):
        ordered_dict_x[j] = 'x'
    for k, v in ordered_dict_x.items():
        ordered_dict_x[k] = 'value'


change_ordered_dict(ordered_dict_x)

"""
При выполнении операций изменения, итерации и присваивания обычный словарь 
работает гораздо быстрее, чем OrderedDict.
Начиная с версии Python 3.6 обычный словарь также поддерживает запоминание 
порядка добавления пар ключ-значение. Таким
образом в настоящее время использование OrderedDict оправдано, 
если нужны только специфичные для него функции,
такие как move_to_end(key, last=True), popitem(last=True).
Время выполенения функции change_dict составляет 0.8417294169999998. 
Время выполенения функции change_ordered_dict составляет 1.1986609169999998. 
"""



