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

# print('Не оптимизированная функция recursive_reverse')
# print(
#     timeit(
#         "recursive_reverse(num_100)",
#         setup='from __main__ import recursive_reverse, num_100',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_1000)",
#         setup='from __main__ import recursive_reverse, num_1000',
#         number=10000))
# print(
#     timeit(
#         "recursive_reverse(num_10000)",
#         setup='from __main__ import recursive_reverse, num_10000',
#         number=10000))


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


# print('Оптимизированная функция recursive_reverse_mem')
# print(
#     timeit(
#         'recursive_reverse_mem(num_100)',
#         setup='from __main__ import recursive_reverse_mem, num_100',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_1000)',
#         setup='from __main__ import recursive_reverse_mem, num_1000',
#         number=10000))
# print(
#     timeit(
#         'recursive_reverse_mem(num_10000)',
#         setup='from __main__ import recursive_reverse_mem, num_10000',
#         number=10000))

'''
Во всех замерах выше мы берем и передаём 10000 одно и тоже случайное число в функцию, что приводит к искажению
результатов замера. Для более точного и наглядного исследования надобности мемоизации для функции recursive_reverse
предлагаю передавать не одно и тоже случайное число, а каждый раз разные случайные числа из тех же диапазонов.
'''
print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(randint(10000, 1000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))
print(
    timeit(
        "recursive_reverse(randint(1000000, 10000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))
print(
    timeit(
        "recursive_reverse(randint(100000000, 10000000000000))",
        setup='from __main__ import recursive_reverse, randint',
        number=10000))

print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(randint(10000, 1000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(randint(1000000, 10000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem(randint(100000000, 10000000000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
        number=10000))


'''
Не оптимизированная функция recursive_reverse
0.04229019989725202
0.03618469997309148
0.0589693000074476
Оптимизированная функция recursive_reverse_mem
0.05849959992337972
0.04384319996461272
0.1314450999489054

Наглядно видно, что в некоторых случаях мемоизацию не то, что не даёт прибавки по времени,
а наоборот, замедляет работу функции
'''