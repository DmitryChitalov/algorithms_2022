"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
from sys import setrecursionlimit
setrecursionlimit(100000)


def get_sum(lst_obj):
    if len(lst_obj) == 1:
        return lst_obj[0]
    else:
        return lst_obj[0] + get_sum(lst_obj[1:])


@profile
def prof_get_sum(lst_obj):
    get_sum(lst_obj)


@profile
def mody_get_sum(lst_obj):
    res = 0
    for el in lst_obj:
        res = res + el
    return res


prof_get_sum([i for i in range(1000)])
mody_get_sum([i for i in range(1000)])