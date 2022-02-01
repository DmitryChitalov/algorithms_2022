from time import time

n = 10 ** 5


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'время выполнения функции {func.__name__}'
              f' составило {end - start}')
        return result

    return timer


@time_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)  # сложность операции О(1)


some_list = []
fill_list_append(some_list, n)
print('_' * 100)


# время выполнения функции fill_list_append составило 0.012765884399414062


@time_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)  # сложность операции О(n)


some_list = []
fill_list_insert(some_list, n)
print('_' * 100)


# время выполнения функции fill_list_insert составило 4.056518793106079


@time_decorator
def fill_dict(dct, num):
    for i in range(num):  # сложность операции О(1)
        dct[i] = i


some_dict = {}
fill_dict(some_dict, n)
print('_' * 100)
# время выполнения функции fill_dict составило 0.015194892883300781
"""
время выполнения функции fill_list_append составило 0.012765884399414062 (константная сложность)
____________________________________________________________________________________________________
время выполнения функции fill_list_insert составило 4.056518793106079 (линейная сложность)
____________________________________________________________________________________________________
время выполнения функции fill_dict составило 0.015194892883300781 (константная сложность)
_____________________________________________________________________
скорость заполнения у списка меньше [], чем у словаря{}
"""


@time_decorator
def change_list(lst):
    for i in range(10000):
        lst.pop(i)  # сложность операции О(n)
    for j in range(1000):
        lst[j] = lst[j + 1]  # сложность операции О(1)


change_list(some_list)
print('_' * 100)


@time_decorator
def change_dict(dct):
    for i in range(10000):  # сложность операции О(1)
        dct.pop(i)
    for j in range(1001, 2002):  # сложность операции О(1)
        dct[j] = 'fill'


change_dict(some_dict)
print('_' * 100)
"""
время выполнения функции change_list составило 0.26422595977783203   линейная сложность
____________________________________________________________________________________________________
время выполнения функции change_dict составило 0.001567840576171875    константная сложность
____________________________________________________________________________________________________
скорость удаления элементов у словаря меньше, чем у списка
функция по изменению словаря срабатывает гораздо быстрее
"""
