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
from cProfile import run


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10_000, 1_000_000)
num_1000 = randint(1_000_000, 10_000_000)
num_10000 = randint(100_000_000, 10_000_000_000_000)

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

print('-' * 100)
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
Не оптимизированная функция recursive_reverse
0.010731833000000003
0.01461812500000001
0.028535000000000005

Оптимизированная функция recursive_reverse_mem
0.0010305830000000016
0.0010378339999999875
0.0010770420000000003
"""

# for i in range(0, 10_000):
#     recursive_reverse(num_100)
#
# for i in range(0, 10_000):
#     recursive_reverse(num_1000)
#
# for i in range(0, 10_000):
#     recursive_reverse(num_10000)
print('-' * 100)
print('Альтернативный замер')
print('recursive_reverse')
print(
    timeit("""for i in range(0, 10_000): recursive_reverse(num_100)""",
        globals=globals(),
        number=1))
print(
    timeit("""for i in range(0, 10_000): recursive_reverse(num_1000)""",
        globals=globals(),
        number=1))
print(
    timeit("""for i in range(0, 10_000): recursive_reverse(num_10000)""",
        globals=globals(),
        number=1))
print('recursive_reverse_mem')
print(
    timeit("""for i in range(0, 10_000): recursive_reverse_mem(num_100)""",
        globals=globals(),
        number=1))
print(
    timeit("""for i in range(0, 10_000): recursive_reverse_mem(num_1000)""",
        globals=globals(),
        number=1))
print(
    timeit("""for i in range(0, 10_000): recursive_reverse_mem(num_10000)""",
        globals=globals(),
        number=1))

print('-' * 100)
print('Данные run:')
run('for i in range(0, 10_000): recursive_reverse(num_100)')
run('for i in range(0, 10_000): recursive_reverse(num_1000)')
run('for i in range(0, 10_000): recursive_reverse(num_10000)')
print('-' * 100)
run('for i in range(0, 10_000): recursive_reverse_mem(num_100)')
run('for i in range(0, 10_000): recursive_reverse_mem(num_1000)')
run('for i in range(0, 10_000): recursive_reverse_mem(num_10000)')

"""
Вот моя версия:
без декоратора количество вызовов за счёт рекурсии составлят 70000/10000 до 130000/10000,
(полагаю, что 10к - первичные вызовы, остальные - глубина рекурсии)
в то время, как с кэшированием количество вызовов составляет просто 10000.
как я понял, замеры не верны потому что они измеряют разные вещи, и
вроде запуск с декоратором считает кэширование - вызовы исключительно декоратора, а не рекурсивные вызовы.
но буду ждать разбора, чтобы узнать как на самом деле всё обстоит.
"""

