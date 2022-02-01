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


def recursive_reverse_v2(number):
    return ''.join(reversed(str(number)))


print('Изменённая функция recursive_reverse_v2')
print(
    timeit(
        'recursive_reverse_v2(num_100)',
        setup='from __main__ import recursive_reverse_v2, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_v2(num_1000)',
        setup='from __main__ import recursive_reverse_v2, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_v2(num_10000)',
        setup='from __main__ import recursive_reverse_v2, num_10000',
        number=10000))


def recursive_reverse_v3(number):
    return str(number)[::--1]


print('Изменённая функция recursive_reverse_v3')
print(
    timeit(
        'recursive_reverse_v3(num_100)',
        setup='from __main__ import recursive_reverse_v3, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_v3(num_1000)',
        setup='from __main__ import recursive_reverse_v3, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_v3(num_10000)',
        setup='from __main__ import recursive_reverse_v3, num_10000',
        number=10000))

"""
Не оптимизированная функция recursive_reverse
0.19745690800004922
0.050059183000030316
0.10633371699998406
Оптимизированная функция recursive_reverse_mem
0.004626273999974728
0.004737018000014359
0.005974506000029578
Изменённая функция recursive_reverse_v2
0.013215772000080506
0.013652310999987094
0.021831543999951464
Изменённая функция recursive_reverse_v3
0.00829535700006545
0.008709080000016911
0.007885952000037832

Исходная функция с мемоизацией работает быстрее, чем без неё.
Сама мемоизация в данном случае не имеет смысла, т.к. кэш начинает заполняться по мере "сворачивания" рекурсии обратно.
Т.е. по мере того, как срабатывает базовый случай. Также каждый новый запуск функции (не рекурсивный) 
происходит с рандомным числом, т.е. кэш не функционален с таким подходом.
Проблема исходной функции в том, что она решает задачу с помощью рекурсии, эффективнее обойтись без неё (v_2 и v_3).
"""
