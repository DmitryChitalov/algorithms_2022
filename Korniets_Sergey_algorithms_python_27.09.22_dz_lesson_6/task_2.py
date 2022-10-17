"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from memory_profiler import profile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

@profile
def rev(nums):
    res = revers(nums)
    return  res

nums = 123456789 ** 50

rev(nums)

"""
Проблема заключается в том, что профилировщик вызывается столько же раз, сколько выполняется рекурсия
Для корректных замеров функции с рекурсией ее необходимо вызвать во внешней функции, а  декоратор
профилирования памяти применить к внешней функции.

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    13     19.5 MiB     19.5 MiB           1   @profile
    14                                         def rev(nums):
    15     20.2 MiB      0.7 MiB           1       res = revers(nums)
    16     20.2 MiB      0.0 MiB           1       return  res


"""
