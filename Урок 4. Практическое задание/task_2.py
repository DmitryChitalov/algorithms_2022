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
print(f"Для аргумента {num_100}:", end=" ")
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print(f"Для аргумента {num_1000}:", end=" ")
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print(f"Для аргумента {num_10000}:", end=" ")
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


def memoize(f):
    cache = {}

    def decorate(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(f"Для аргумента {num_100}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        globals=globals(),
        number=10000))
print(f"Для аргумента {num_1000}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        globals=globals(),
        number=10000))
print(f"Для аргумента {num_10000}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(),
        number=10000))

# обновим значения аргументов
num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Оптимизированная функция с новыми значениями recursive_reverse_mem')
print(f"Для аргумента {num_100}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        globals=globals(),
        number=10000))
print(f"Для аргумента {num_1000}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        globals=globals(),
        number=10000))
print(f"Для аргумента {num_10000}:", end=" ")
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        globals=globals(),
        number=10000))



"""
Не оптимизированная функция recursive_reverse
Для аргумента 931005: 0.017736833000000004
Для аргумента 6295801: 0.017499
Для аргумента 5312849987060: 0.030270207999999993
Оптимизированная функция recursive_reverse_mem
Для аргумента 931005: 0.0010566250000000055
Для аргумента 6295801: 0.0010989170000000048
Для аргумента 5312849987060: 0.0010726250000000076
Оптимизированная функция с новыми значениями recursive_reverse_mem
Для аргумента 957984: 0.001022374999999992
Для аргумента 8533355: 0.0010396249999999885
Для аргумента 4341463412960: 0.0010710830000000005

При многократном вызове функции в кеше накапливаются значения, что ускоряет её последующие вызовы с тем же значением.
Поскольку timeit многократо вызывает функцию с одним и тем же аргументом, использование @memoize приводит к тому, что
сама рекурентная функция вызывает только при первом прогоне, а все последующие вызовы берут значение из кеша. Это 
существенно улучшает результаты измерений.
"""