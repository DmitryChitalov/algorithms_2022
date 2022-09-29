"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
import random
import sys
import time
import timeit
from copy import deepcopy

from memory_profiler import memory_usage
from memory_profiler import profile
from pympler.asizeof import asizeof


def mem_decor(f):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = time.time()
        func_res = f(*args)
        m2 = memory_usage()
        mem = m2[0] - m1[0]
        res_time = time.time() - t1
        return f'{res_time} == {mem}'

    return wrapper


@mem_decor
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_10000 = random.randint(100000000, 10000000000)
print(recursive_reverse(num_10000))


@mem_decor
def recursive_reverse_opti(number):
    def wrapper(number):
        if number == 0:
            return str(number % 10)
        return f'{str(number % 10)}{wrapper(number // 10)}'

    r = wrapper(number)
    return r


print(recursive_reverse_opti(num_10000))

@mem_decor
def fact_profile(n):
    def fact(n):
        if (n <= 1):
            return 1
        else:
            return (n * fact(n - 1))

    f = fact(n)
    return f

@mem_decor
def fact(n):
    if (n <= 1):
        return 1
    else:
        return (n * fact(n - 1))


t1 = time.time()
fact(10)
print(time.time() - t1)
t1 = time.time()
print(fact_profile(10))
print(time.time() - t1)
"""
2.1940019130706787 == 0.015625
0.10527706146240234 == 0.0

Получаются такие данный. Не понимаю почему так происходит.
"""
