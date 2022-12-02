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
import cProfile


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

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
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import memoize,recursive_reverse_mem, num_100',
        number=100))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=1000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))




"""
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

Меморизация создает обратыный номер для каждой подстроки + в примерах выше не учитывалось те действия которые происходят в 
декораторе (добавление ключь значение). 
из примеров ниже видно что чем меньше вызовов тем больше время скорее рекурсия здесь не нужна 

"""

print('Оптимизированная функция recursive_reverse_mem FINAL')
print(
    timeit(
        'memoize(recursive_reverse_mem(num_100))',
        setup='from __main__ import memoize, recursive_reverse_mem, num_100',
        number=100))

print(
    timeit(
        'memoize(recursive_reverse_mem(num_1000))',
        setup='from __main__ import memoize, recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'memoize(recursive_reverse_mem(num_10000))',
        setup='from __main__ import memoize, recursive_reverse_mem, num_10000',
        number=10000))

print(
    timeit(
        'memoize(recursive_reverse_mem(num_10000))',
        setup='from __main__ import memoize, recursive_reverse_mem, num_10000',
        number=10000))
