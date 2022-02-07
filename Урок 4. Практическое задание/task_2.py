"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
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

'''
Данная попытка попытка оптимизировать решение мемоизацией бессмысленна. Количество выполнений функции 10000.
С одним и тем же числом. За первое выполнение функции cache в memoize заполнится нужными значениями и будет 
выдавать их 9999 раз из словаря очень быстро. В реальности числа разные. Если в функции задавать разные 
значения - время выполнения оптимизированной не будет отличаться от неоптимизированной. Что и показал
эксперимент.
Не оптимизированная функция recursive_reverse с разными числами
0.02254110000000001
Оптимизированная функция recursive_reverse_mem  с разными числами
0.022547400000000023
'''


def get_func0():
    num = randint(100000, 1000000)
    return recursive_reverse(num)


def get_func1():
    num = randint(100000, 1000000)
    return recursive_reverse_mem(num)


print('Не оптимизированная функция recursive_reverse с разными числами')
print(
    timeit(
        "get_func0()",
        setup='from __main__ import get_func0',
        number=10000))
print('Оптимизированная функция recursive_reverse_mem  с разными числами')
print(
    timeit(
        'get_func1()',
        setup='from __main__ import get_func1',
        number=10000))
