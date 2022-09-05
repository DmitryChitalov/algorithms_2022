"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


@profile
def f_profiler(func):
    def wrapper(*args):
        res = func(*args)
        return res
    return wrapper


@f_profiler
def _sum(lst):
    if len(lst) == 1:
        return lst.pop()
    else:
        return lst.pop() + _sum(lst)


total = _sum(list(range(100)))
print(total)


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    15     19.3 MiB     19.3 MiB           1   @profile
    16                                         def f_profiler(func):
    17     19.3 MiB      0.0 MiB           1       def wrapper(*args):
    18                                                 res = func(*args)
    19                                                 return res
    20     19.3 MiB      0.0 MiB           1       return wrapper
    
Выводы: если профилировать рекурсию, получим столько таблиц, сколько будет вызовов функции, как вариант обернуть
функцию в другую и замерить использование памяти для неё
"""
