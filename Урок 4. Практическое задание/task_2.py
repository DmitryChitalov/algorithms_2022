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


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)

num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
print(num_10000)

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
        #if cache.get(args):
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
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

"""
время минимальное при мемоизации, тк. результат обработанного числа уже в кэше (после 1го прохождения)
и повторно подаётся тоже самое число - результат берётся из кэша, сама функция ничего не делает.
проверим время  при подаче разных значений в функции:
"""

rand_mass = [randint(1000, 100000) for i in range(100)]
#print(rand_mass)


def test_func():
    for i in rand_mass:
        recursive_reverse(i)


def test_mem():
    for i in rand_mass:
        recursive_reverse_mem(i)


print('время при подаче разных значений')
print(timeit('test_func()', globals=globals(), number=1))
print(timeit('test_mem()', globals=globals(), number=1))

"""
Вывод: мемоизация эффективна только если функция будет повторно обрабатывать 
одно и то же число( либо список часто повторяющихся). При подаче разных значений,
она затрачивает больше времени, чем обычная рекурсивная ф-ция
"""