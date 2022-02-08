from timeit import default_timer
from collections import OrderedDict

some_dict = {}
some_ordered_dict = OrderedDict()
n = 10 ** 7


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} '
              f'составило {default_timer() - start}. ')

        return result

    return wrapper


@time_decorator
def fill_dict(some_dict, n):
    for i in range(n):
        some_dict[i] = i


@time_decorator
def fill_ordered_dict(some_ordered_dict, n):
    for i in range(n):
        some_ordered_dict[i] = i


fill_dict(some_dict, n)
fill_ordered_dict(some_ordered_dict, n)

# Время выполенения функции fill_dict составило 1.268242876.
# Время выполенения функции fill_ordered_dict составило 1.9507380429999999.


"""
Обычный словарь заполняется элементами быстрее, чем OrderedDict. 
"""


@time_decorator
def change_dict(dct):
    for i in range(1000000):
        dct.pop(i)
    for j in range(1000001, 2000002):
        dct[j] = 'fill'
    for k, v in dct.items():
        dct[k] = 'some value'


@time_decorator
def change_ordered_dict(dct):
    for i in range(1000000):
        dct.pop(i)
    for j in range(1000001, 2000002):
        dct[j] = 'fill'
    for k, v in dct.items():
        dct[k] = 'some value'


change_dict(some_dict)
change_ordered_dict(some_ordered_dict)

# Время выполенения функции change_dict составило 0.9021570019999996.
# Время выполенения функции change_ordered_dict составило 1.0924670399999998.

"""
При выполнении операций изменения обычный словарь работает гораздо быстрее, чем OrderedDict.
"""
