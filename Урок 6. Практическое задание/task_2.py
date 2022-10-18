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
Проблема прямого профилирования памяти рекурсии заключается в том,
что мы получим отчёт с каждого вызова.

Чтобы сделать нормальный замер памяти,
нужно либо писать свой декоратор и вешать его на функцию,
либо делать обёртку и профилировать её.

Вывод программы:
Filename: /home/fox/Рабочий стол/algorithms_2022/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    39     19.4 MiB     19.4 MiB           1   @profile
    40                                         def wrapper():
    41     19.9 MiB      0.5 MiB           1       res = geometric_progression_short(500)
    42     19.9 MiB      0.0 MiB           1       return res


0.6666666666666667
"""


@profile
def wrapper():
    res = geometric_progression_short(500)
    return res


def geometric_progression_short(n):
    return (-0.5) ** (n - 1) + geometric_progression_short(n - 1) if n else 0


print(wrapper())