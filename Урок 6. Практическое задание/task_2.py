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
def mem(f):
    def cont(*args, **kwargs):
        return f(args[0])

    return cont


@mem
def fac(n):
    return n if n <= 1 else n * fac(n - 1)


print(fac(6))

"""
основная проблема профилирования рекурсивной функции в том, что
количество таблиц с замерами получается раным глубине рекурсии.
удалось решить это через двойное декорирование:
1. собственный декоратор, который служит как бы контейнером для рекурсивной функции
2. @profile из модуля memory_profiler для замера получившегося контейнера.

в моём примере получились вот такие результаты:
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     16.2 MiB     16.2 MiB           1   @profile()
     5                                         def mem(f):
     6     16.2 MiB      0.0 MiB           1       def wrapper(*args, **kwargs):
     7                                                 m1 = memory_usage()
     8                                                 res = f(args[0])
     9                                                 m2 = memory_usage()
    10                                                 mem_dif = m2[0] - m1[0]
    11                                                 # print(f'Время выплнения: {mem_dif}')
    12                                                 return res
    13     16.2 MiB      0.0 MiB           1       return wrapper
"""



