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

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(randint(10000, 1000000))",
        setup='from __main__ import recursive_reverse, randint',
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
        'recursive_reverse_mem(randint(10000, 1000000))',
        setup='from __main__ import recursive_reverse_mem, randint',
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
Мемоизация не нужна в этом случае, randint создаёт значение и передаёт его функции в timeit
и это значение гоняется number раз, соответственно оно достаётся из кеша, раз оно одно,
но стоит randint загнать в аргумент функции, всё меняется, время сравнивается лиш в некоторых случаях
с мемоизацией чуть быстрее, так как randint периодически может выдать одинаковые значения

Это результат когда randint вне аргумента функции:
Не оптимизированная функция recursive_reverse
0.021261800000502262
0.023765399993862957
0.04039659999398282
Оптимизированная функция recursive_reverse_mem
0.001625899996724911
0.0015977000002749264
0.0016661000045132823

Это результат когда в первую функцию randint передал аргументом функции:
Не оптимизированная функция recursive_reverse
0.03807680000318214
0.033891899991431274
0.05702300000120886
Оптимизированная функция recursive_reverse_mem
0.0386175000021467
0.0016899000038392842
0.0026708000077633187
"""
