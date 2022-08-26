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

"""
Идея такая:
Подвох в параметре number timeit. Мы задаём number=10000, мемоизация тогда отрабатывает и сохраняет данные

Возьмём number поменьше, например, 1000:

Не оптимизированная функция recursive_reverse
0.0025554900003044168
0.0026453730006323894
0.004311122000217438
Оптимизированная функция recursive_reverse_mem
0.00016689699987182394
0.00015658799929951783
0.00017213299906870816

Возьмём number ещё меньше, 100:

Не оптимизированная функция recursive_reverse
3.563999962352682e-05
3.087900040554814e-05
5.658900045091286e-05
Оптимизированная функция recursive_reverse_mem
1.5077999705681577e-05
1.073500061465893e-05
2.055200093309395e-05

Ну а теперь возьмём вообще number=1:

Не оптимизированная функция recursive_reverse
9.589999535819516e-06
6.782000127714127e-06
1.0425999789731577e-05
Оптимизированная функция recursive_reverse_mem
1.367799995932728e-05
8.564999006921425e-06
1.8459999409969896e-05

ВЫВОД: на одном прогоне от мемоизации толку ноль
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
        number=1))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=1))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=1))


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
        number=1))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=1))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=1))
