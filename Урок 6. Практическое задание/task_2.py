"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile

# @profile
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


# print(recursive_reverse_mem(10000000000000))

# Solve
@profile
def overflow():
    print(recursive_reverse_mem(100000000000000000000000))


overflow()
"""
Функция профилируется каждый вызов в рекурсии
Необходимо обернуть и запустить

00000000000001

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     19.3 MiB     19.3 MiB           1   @profile
    25                                         def overflow():
    26     19.3 MiB      0.0 MiB           1       print(recursive_reverse_mem(100000000000000000000000))
"""
