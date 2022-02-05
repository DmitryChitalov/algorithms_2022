"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение.
"""
from memory_profiler import profile


@profile
def wrapper_fact(n):
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    return factorial(n)


print(wrapper_fact(10))


@profile
def wrapper_reverse(n):
    def recursive_reverse(number):
        if number == 0:
            return ''
        return f'{str(number % 10)}{recursive_reverse(number // 10)}'

    return recursive_reverse(n)


print(wrapper_reverse(1234))

"""
вычисления факториала и разворота числа есть проблема многократного вывода профиля,
решается добавлением необходимой для замера функции в функцию-обертку.
При этом удобно, что в колонке "Occurences" показывается число вызовов строк.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    4     19.7 MiB     19.7 MiB           1   @profile
     5                                         def wrapper_fact(n):
     6     19.7 MiB      0.0 MiB          11       def factorial(n):
     7     19.7 MiB      0.0 MiB          10           if n == 1:
     8     19.7 MiB      0.0 MiB           1               return 1
     9                                                 else:
    10     19.7 MiB      0.0 MiB           9               return n * factorial(n - 1)
    11                                         
    12     19.7 MiB      0.0 MiB           1       return factorial(n)

3628800

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     19.7 MiB     19.7 MiB           1   @profile
    19                                         def wrapper_reverse(n):
    20     19.7 MiB      0.0 MiB           6       def recursive_reverse(number):
    21     19.7 MiB      0.0 MiB           5           if number == 0:
    22     19.7 MiB      0.0 MiB           1               return ''
    23     19.7 MiB      0.0 MiB           4           return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    24                                         
    25     19.7 MiB      0.0 MiB           1       return recursive_reverse(n)
4321
"""
