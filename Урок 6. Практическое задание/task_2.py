"""
Задание 2.

Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.

Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.

Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import memory_usage
from pympler import asizeof
from memory_profiler import memory_usage
from memory_profiler import profile


'''
На примере рекрсии числа Фибоначчи.
@profile
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(10))
если просто навесить декоратор профилирования рекурсии,
то будет результат будет возвращаться столько раз, сколько раз рекурсия вызовет саму себя.
В таком случае нужно обернуть функцию в декоратор с методом memory_usage из модуля memory_profiler
либо обернуть функцию в ещё одну функцию и уже на обёрнутую ф-ию навесить декоратор профилирования
@profile
'''

'''
вариант №1 Фибоначчи в обёртке
'''
@profile
def recur(num=25):
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)
    return fib(num)

#print(recur())


'''
вариант №2 декоратор с методом memory_usage из модуля memory_profiler
'''
def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return mem_diff

    return wrapper


@decor
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))







