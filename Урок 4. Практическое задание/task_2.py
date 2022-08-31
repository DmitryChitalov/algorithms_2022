"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


def recursive_reverse(number):
    """
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
    """
    quotient, remainder = divmod(number, 10)  # частное, остаток
    if not quotient:
        return str(remainder)
    else:
        return str(remainder) + str(recursive_reverse(quotient))


num_fib = 20

print('Не оптимизированная функция fib')
print(
    timeit(
        "fib(num_fib)",
        setup='from __main__ import fib, num_fib',
        number=1000))

num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

"""
print(f'num_100 =', num_100)
print(f'num_1000 =', num_1000)
print(f'num_10000 =', num_10000)
"""

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            print(cache)
            return cache[args]
    return decorate


@memoize
def fib_mem(n):
    if n < 2:
        return n
    return fib_mem(n-2) + fib_mem(n-1)


@memoize
def recursive_reverse_mem(number):
    """
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'
    """
    quotient, remainder = divmod(number, 10)  # частное, остаток
    if not quotient:
        return str(remainder)
    else:
        return str(remainder) + str(recursive_reverse_mem(quotient))


print('Оптимизированная функця fib_mem')
print(
    timeit(
        "fib_mem(num_fib)",
        setup='from __main__ import fib_mem, num_fib',
        number=1000))


print('Оптимизированная функция recursive_reverse_mem')
print(f'num_100 =', num_100)
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(f'num_1000 =', num_1000)
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(f'num_10000 =', num_10000)
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))
"""
При одном запуске мемоизация не имеет смысла,
при многочисленных запусках смысл есть, когда есть 
интенсивное обращение к кэшу.
Очень наглядным с этой точки зрения является реализация
последовательности Фиьбоначчи.
"""