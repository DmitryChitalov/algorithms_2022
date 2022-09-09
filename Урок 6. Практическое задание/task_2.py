"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""

from random import randint, choice
from memory_profiler import profile

from random import randint, choice
from memory_profiler import profile

"""
проблема прямого профилирования памяти рекурсии заключается в том, происходит замер при каждом вызове.
Для получения данных, по которым можно проводить сравнение, для профелирования рекурсии необходимо использовать 
декоратор или "обёртку".

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35     19.4 MiB     19.4 MiB           1   @profile
    36                                         def wrapper():
    37     20.0 MiB      0.5 MiB           1       res = geometric_progression_short(500)
    38     20.0 MiB      0.0 MiB           1       return res
"""


@profile
def wrapper():
    res = geometric_progression_short(500)
    return res


def geometric_progression_short(n):
    return (-0.5) ** (n - 1) + geometric_progression_short(n - 1) if n else 0


print(wrapper())
