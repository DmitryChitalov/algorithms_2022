"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опишите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
from memory_profiler import memory_usage
from time import perf_counter
MEBIBYTE = 1048576  # Bytes


def check(func):
    """
    Декоратор для замера скорости исполнения кода и потребляемой памяти
    (с ипользованием memory_profiler)
    """
    def wrapper(*args, **kwargs):
        memory = memory_usage()
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        memory_2 = memory_usage()
        memory_used = memory_2[0] - memory[0]
        print(f"Функция {func.__name__!r} использовала память:"
              f" {memory_used} Mib или {memory_used * MEBIBYTE} Bytes")
        print(f"Функция {func.__name__!r} выполнена за {run_time:.8f} c")

        return result
    return wrapper


"""
Если вызвать здесь профилирование памяти с помощью функции profile,
то у нас будет столько таблиц, сколько вызовов рекурсивной функции.
"""


# @check
# @profile
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


# @profile
def main():
    # take input from the user
    num = int(input("Enter a number: "))
    print()
    # check is the number is negative
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        print(f"The factorial of {num} is {call_factorial(num)}")


# фунция обёртка для рекурсивной функции
@check
@profile
def call_factorial(num):
    return recur_factorial(num)


"""
Для num = 5:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    68     18.2 MiB     18.2 MiB           1   @check
    69                                         @profile
    70                                         def call_factorial(num):
    71     18.3 MiB      0.0 MiB           1       return recur_factorial(num)


Функция 'call_factorial' использовала память: 0.28125 Mib или 294912.0 Bytes
Функция 'call_factorial' выполнена за 0.08157189 c
"""


if __name__ == "__main__":
    main()
"""
The factorial of 5 is 120
"""
